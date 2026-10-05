"""Oracle distribution v3: bounded, signed, complete snapshots; no source execution.

The private signing key and the content/license review stay outside the release.
Packages are JSON records, not archives: extraction cannot create links or devices.
The signed payload contains every package digest and every installed-file digest.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import unicodedata

from catalog_safety import check_publication_bytes, publication_rule_counts

SCHEMA = 3
DOMAIN = b'oracle-distribution-v3\x00'
PIN = '2efaaf8f8a817b5b82e023383618fdcdb1cc5f7d'
VERSION = '0.48.4.0'
ROOTS = {'skills': 'specialists', 'prompts': 'prompts', 'tutoriais': 'tutorials'}
TARGETS = {'skills': 'skills', 'recursos-skills': 'recursos-skills', 'prompts': 'prompts', 'tutoriais': 'Tutoriais'}
DEPARTMENTS = {'codigo':'code','conteudo':'content','conversao':'conversao','entrega':'entrega','leads':'leads','marketing':'marketing','oferta':'oferta','sistemas':'sistemas','trafego':'trafego','vendas':'sales'}
MAX_FILE = 32_000_000
MAX_PACKAGE_BYTES = 32_000_000
MAX_PACKAGE_FILES = 1000
MAX_FILES = 30_000
MAX_BYTES = 512_000_000
TEXT_EXTENSIONS = set('md txt json yaml yml py js ts sh toml css html csv sql svg mjs cjs mts go mod sum ps1 xml cff lock jsonl golden manifest timer service tmpl pub cmd fedora arch ubuntu claude-network-none yar example'.split())
RESOURCE_EXTENSIONS = set('png jpg jpeg webp gif mp3 mp4 gz pdf woff woff2 ttf otf ico'.split())
LICENSE_NAMES = {'LICENSE', 'LICENCE', 'NOTICE', 'COPYING', 'LICENSE-MIT', 'LICENSE-APACHE'}


class Refused(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Refused(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def unique_json(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, 'Duplicate JSON key')
        value[key] = item
    return value


def decode(data):
    return json.loads(data, object_pairs_hook=unique_json)


def path_key(path):
    return unicodedata.normalize('NFC', path).lower()


def safe_path(path, hidden=False):
    require(isinstance(path, str) and 0 < len(path.encode()) <= 700, 'Invalid path length')
    require(not path.startswith('/') and '\\' not in path and not any(ord(c) < 32 or ord(c) == 127 for c in path), 'Unsafe relative path')
    parts = path.split('/')
    require(all(p not in ('', '.', '..') and (hidden or not p.startswith('.')) for p in parts), 'Unsafe path component')
    try:
        check_publication_bytes('source-path', path.encode())
    except ValueError:
        raise Refused('Credential-like filename; matching value omitted') from None
    return path


def file_limit(path):
    return 2_000_000 if PurePosixPath(path).suffix.lower() == '.md' else MAX_FILE


def stamp(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns, info.st_mode, getattr(info, 'st_flags', 0))


def directory_fd(path):
    """Open all ancestors without following links; never request cloud hydration."""
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in Path(os.path.abspath(path)).parts[1:]:
            safe_path(part, hidden=True)
            info = os.stat(part, dir_fd=fd, follow_symlinks=False)
            require(stat.S_ISDIR(info.st_mode) and not getattr(info, 'st_flags', 0) & 0x40000000, 'Symlink/non-directory/dataless ancestor')
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            require(stamp(os.fstat(child)) == stamp(info), 'Directory changed during open')
            os.close(fd)
            fd = child
        answer, fd = fd, -1
        return answer
    finally:
        if fd >= 0:
            os.close(fd)


def read_stable(path, info=None):
    info = info or path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, 'Symlink/nonregular/hardlinked source')
    require(not getattr(info, 'st_flags', 0) & 0x40000000, 'Dataless file; download through macOS before packaging')
    require(info.st_size <= file_limit(str(path)), 'File exceeds supported limit')
    parent = directory_fd(path.parent)
    try:
        fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | getattr(os, 'O_NONBLOCK', 0), dir_fd=parent)
        with os.fdopen(fd, 'rb') as stream:
            require(stamp(os.fstat(stream.fileno())) == stamp(info), 'Source changed before read')
            data = stream.read(file_limit(str(path)) + 1)
            require(stamp(os.fstat(stream.fileno())) == stamp(info), 'Source changed during read')
        require(stamp(os.stat(path.name, dir_fd=parent, follow_symlinks=False)) == stamp(info) and len(data) == info.st_size, 'Source replaced during read')
        return data
    finally:
        os.close(parent)


def inventory(source):
    """Metadata inventory reports every exclusion instead of silently dropping it."""
    rows, problems, directories = [], [], {}
    roots = dict(ROOTS)
    if (source / "SISTEMA/recursos-skills").exists():
        roots["recursos-skills"] = "specialists"
    for name, kind in roots.items():
        root = source / 'SISTEMA' / name
        try:
            fd = directory_fd(root)
            os.close(fd)
        except (OSError, Refused) as error:
            problems.append({'path': 'SISTEMA/' + name, 'code': 'root_unavailable', 'reason': str(error)})
            continue
        def onerror(error):
            problems.append({'path': name, 'code': 'enumeration_failed', 'reason': type(error).__name__})
        for parent, dirs, files in os.walk(root, followlinks=False, onerror=onerror):
            parent = Path(parent)
            directories[parent.relative_to(source).as_posix()] = stamp(parent.lstat())
            for child in list(dirs):
                path = parent / child
                if path.is_symlink() or getattr(path.lstat(), 'st_flags', 0) & 0x40000000:
                    problems.append({'path': path.relative_to(source).as_posix(), 'code': 'unavailable_directory'})
                    dirs.remove(child)
            for filename in sorted(files):
                path = parent / filename
                relative = path.relative_to(source).as_posix()
                try:
                    safe_path(relative, hidden=True)
                    info = path.lstat()
                    target = 'SISTEMA/' + TARGETS[name] + '/' + path.relative_to(root).as_posix()
                    row = {'source_path': relative, 'path': target, 'kind': kind, 'size': info.st_size,
                           'mode': 0o755 if info.st_mode & 0o111 else 0o644, 'stamp': stamp(info)}
                    rows.append(row)
                    if getattr(info, 'st_flags', 0) & 0x40000000:
                        problems.append({'path': relative, 'code': 'dataless'})
                    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                        problems.append({'path': relative, 'code': 'nonregular_or_linked'})
                    if info.st_size > file_limit(relative):
                        problems.append({'path': relative, 'code': 'file_size_limit'})
                    if any(part in {'.git', '.env', '.DS_Store', 'node_modules', '.gbrain'} for part in PurePosixPath(relative).parts):
                        problems.append({'path': relative, 'code': 'private_or_dependency_metadata'})
                    ext = path.suffix.lower().lstrip('.')
                    if ext and ext not in TEXT_EXTENSIONS | RESOURCE_EXTENSIONS and path.name.upper() not in LICENSE_NAMES:
                        problems.append({'path': relative, 'code': 'unreviewed_format'})
                except (OSError, Refused) as error:
                    problems.append({'path': '[redacted]' if 'Credential' in str(error) else relative, 'code': 'invalid_file', 'reason': str(error)})
    keys = set()
    for row in rows:
        key = path_key(row['path'])
        if key in keys:
            problems.append({'path': row['source_path'], 'code': 'portable_path_collision'})
        keys.add(key)
    counts = {kind: {'files': sum(r['kind'] == kind for r in rows), 'bytes': sum(r['size'] for r in rows if r['kind'] == kind)} for kind in ROOTS.values()}
    for kind, count in counts.items():
        if not count['files']:
            problems.append({'path': kind, 'code': 'empty_required_library'})
    if len(rows) > MAX_FILES or sum(r['size'] for r in rows) > MAX_BYTES:
        problems.append({'path': '.', 'code': 'distribution_budget_exceeded'})
    return {'schema_version': SCHEMA, 'source': str(source), 'files': sorted(rows, key=lambda r: r['path']),
            'directories': directories, 'counts': counts, 'problems': problems, 'complete': not problems}


def frontmatter(data):
    import yaml
    text = data.decode('utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    require(match is not None, 'SKILL.md requires delimited YAML frontmatter')
    require(len(match[1]) <= 32_000, 'Skill frontmatter exceeds bounded metadata size')
    try:
        require(not any(isinstance(token, (yaml.tokens.AliasToken, yaml.tokens.AnchorToken)) for token in yaml.scan(match[1])), 'YAML aliases are unsupported')
        node = yaml.compose(match[1], Loader=yaml.SafeLoader)
        require(isinstance(node, yaml.MappingNode), 'Frontmatter must be a mapping')
        keys = [key.value for key, _ in node.value]
        require(len(keys) == len(set(keys)), 'Duplicate frontmatter key')
        require(all(key.value != 'name' or (isinstance(value, yaml.ScalarNode) and value.style not in ('|', '>')) for key, value in node.value), 'Skill name must be a single-line scalar')
        fields = yaml.safe_load(match[1])
    except yaml.YAMLError:
        raise Refused('Invalid YAML frontmatter') from None
    name, description = fields.get('name'), fields.get('description')
    require(isinstance(name, str) and re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', name), 'Skill requires portable name')
    require(isinstance(description, str) and 0 < len(description.strip()) <= 4096, 'Skill requires description')
    return text, name


def approved_departments():
    manifest = decode((Path(__file__).resolve().parent.parent / 'Resources/catalog/departments.json').read_bytes())
    return {collection: row['id'].removeprefix('department/') for row in manifest['departments']
            if row['id'] != 'department/other' for collection in row['collection_ids']}


def apply_reviewed_adaptations(blobs, review):
    """Exact, private text edits; retain only digests and reasons in public provenance."""
    adaptations, seen = [], set()
    for edit in review.get('file_adaptations', []):
        path = safe_path(edit.get('path', ''), hidden=True)
        require(path in blobs and path not in seen, 'Adaptation file absent or duplicated')
        seen.add(path)
        data = blobs[path]
        require(sha(data) == edit.get('source_sha256'), 'Adaptation source changed since review')
        require(isinstance(edit.get('reason'), str) and 0 < len(edit['reason'].strip()) <= 1000, 'Adaptation requires a bounded reason')
        check_publication_bytes('adaptation reason', edit['reason'].encode())
        require(PurePosixPath(path).suffix.lower().lstrip('.') in TEXT_EXTENSIONS, 'Only text adaptations are supported')
        text = data.decode('utf-8')
        replacements = edit.get('replacements')
        require(isinstance(replacements, list) and 0 < len(replacements) <= 1000, 'Adaptation requires bounded exact replacements')
        for replacement in replacements:
            before, after, count = replacement.get('before'), replacement.get('after'), replacement.get('count')
            require(isinstance(before, str) and before and isinstance(after, str) and type(count) is int and count > 0, 'Invalid text replacement')
            require(text.count(before) == count, 'Adaptation occurrence count changed since review')
            text = text.replace(before, after)
        adapted = text.encode('utf-8')
        require(adapted != data and len(adapted) <= file_limit(path), 'Adaptation is unchanged or exceeds file budget')
        require(sha(adapted) == edit.get('result_sha256'), 'Adaptation result differs from reviewed bytes')
        if path.lower().endswith('.json'):
            decode(adapted)
        # The normal audit still checks the edited bytes for secrets, links and frontmatter.
        blobs[path] = adapted
        adaptations.append({'path': path, 'field': 'content', 'source_sha256': sha(data),
                            'result_sha256': sha(adapted), 'reason': edit['reason']})
    return adaptations


def add_reviewed_supplements(rows, blobs, review):
    additions, keys = [], {path_key(path) for path in blobs}
    entries = review.get('supplemental_files', [])
    require(isinstance(entries, list) and len(entries) <= 1000, 'Supplement inventory exceeds its limit')
    for entry in entries:
        path = safe_path(entry.get('path', ''), hidden=True)
        parts = PurePosixPath(path).parts
        require(len(parts) >= 3 and parts[0] == 'SISTEMA' and parts[1] in TARGETS.values(), 'Supplement outside approved libraries')
        require(path_key(path) not in keys, 'Supplement collides with a source file')
        require(entry.get('purpose') in {'author-license', 'upstream-license', 'distribution-notice', 'preserved-upstream-template'}, 'Unknown supplement purpose')
        require(PurePosixPath(path).suffix.lower() in {'.md', '.txt'} or PurePosixPath(path).name in LICENSE_NAMES, 'Supplement must be a notice or template')
        require(isinstance(entry.get('reason'), str) and 0 < len(entry['reason'].strip()) <= 1000, 'Supplement needs reviewed provenance')
        data = base64.b64decode(entry.get('content_base64', ''), validate=True)
        require(0 < len(data) <= 2_000_000 and sha(data) == entry.get('sha256'), 'Supplement digest/size mismatch')
        data.decode('utf-8')
        if entry['purpose'] == 'preserved-upstream-template':
            source = next((r for r in rows if r['path'] == entry.get('original_path')), None)
            require(source and source['source_sha256'] == sha(data), 'Preserved template is not the exact original source')
        kind = {'skills': 'specialists', 'prompts': 'prompts', 'Tutoriais': 'tutorials'}[parts[1]]
        rows.append({'path': path, 'source_path': path, 'kind': kind, 'size': len(data), 'mode': 0o644,
                     'source_sha256': sha(data), 'supplemental': True})
        blobs[path] = data
        keys.add(path_key(path))
        additions.append({key: value for key, value in entry.items() if key != 'content_base64'})
    return additions


def audit_portability(rows, blobs, review):
    problems, adaptations, items = [], [], []
    by_path = {row['path']: row for row in rows}
    known = set(by_path)
    names = set()
    mapping = review.get('items', {})
    defaults = approved_departments()
    structured = review.get('skills_layout') == 'department-specialist-skill'
    for row in rows:
        path, data = row['path'], blobs[row['path']]
        try:
            check_publication_bytes(path, data, review.get('publication_examples'))
        except ValueError:
            problems.append({'path': path, 'code': 'credential_pattern'})
            # A blocked file must still be represented in the item/license inventory.
        if PurePosixPath(path).suffix.lower().lstrip('.') in TEXT_EXTENSIONS:
            try:
                text = data.decode('utf-8')
            except UnicodeError:
                problems.append({'path': path, 'code': 'invalid_text_encoding'})
                continue
            if re.search(r'(?:/Users/[^\s/]+/|/home/[^\s/]+/|[A-Z]:\\Users\\)', text):
                finding_review = review.get('machine_path_reviews', {}).get(path, {})
                if not (finding_review.get('sha256') == sha(data)
                        and finding_review.get('classification') in {'test-fixture', 'documentation-example', 'upstream-maintainer-source', 'historical-upstream-record'}
                        and isinstance(finding_review.get('reason'), str) and 0 < len(finding_review['reason'].strip()) <= 1000):
                    problems.append({'path': path, 'code': 'machine_absolute_path'})
            if path.lower().endswith('.md'):
                # Examples inside code are not document/resource references.
                prose = re.sub(r'(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', '', text)
                prose = re.sub(r'`[^`\n]*`', '', prose)
                for match in re.finditer(r'!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)', prose):
                    ref = match[1].strip('<>').split('#')[0]
                    if not ref or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', ref) or ref.startswith('#'):
                        continue
                    from urllib.parse import unquote
                    target = os.path.normpath(str(PurePosixPath(path).parent / unquote(ref)))
                    if target not in known and not any(p.startswith(target.rstrip('/') + '/') for p in known):
                        problems.append({'path': path, 'code': 'missing_relative_reference', 'reference': ref})
                for ref in re.findall(r'\[\[([^\]|#]+)', prose):
                    target = ref if ref.lower().endswith('.md') else ref + '.md'
                    matches = [p for p in known if p == target or p.endswith('/' + target)]
                    if len(matches) != 1:
                        problems.append({'path': path, 'code': 'ambiguous_or_missing_wikilink', 'reference': ref})
        skill_document = PurePosixPath(path).name == 'SKILL.md' and path.startswith('SISTEMA/skills/') and row['kind'] == 'specialists'
        parts = PurePosixPath(path).parts
        reviewed_nested = False
        if skill_document and structured and len(parts) != 6:
            # Nested templates/resources already owned by a canonical skill stay
            # resources. A new phase/skill hierarchy has no such owner: silently
            # packaging it without discoverable items would misreport delivery.
            owner = '/'.join(parts[:5]) + '/SKILL.md'
            classification = mapping.get(path, {})
            classified = (classification.get('source_sha256') == sha(data)
                and classification.get('license_reviewed') is True
                and classification.get('dependencies_reviewed') is True
                and isinstance(classification.get('reason'), str)
                and 0 < len(classification['reason'].strip()) <= 1000)
            if classification.get('entry_role') == 'skill':
                # The phase/skill contract is explicit in the signed item. Older
                # apps are excluded by minimum_oracle; arbitrary deeper trees
                # remain unsupported until separately qualified.
                if len(parts) != 7 or not classified:
                    problems.append({'path': path, 'code': 'nested_skill_review_required'})
                    continue
                reviewed_nested = True
            elif len(parts) > 6 and owner in known:
                continue
            elif classification.get('entry_role') == 'resource' and classified:
                continue
            else:
                problems.append({'path': path, 'code': 'skill_entry_classification_required'})
                continue
        kind = 'skill' if skill_document else {'prompts': 'prompt', 'tutorials': 'tutorial'}.get(row['kind']) if path.lower().endswith('.md') else None
        if not kind:
            continue
        info = mapping.get(path, {})
        item_id = info.get('id', kind + '-' + sha(path.encode())[:20])
        require(re.fullmatch(r'[a-z0-9][a-z0-9-]{0,54}', item_id) is not None, 'Invalid stable item ID')
        required = [p for p in known if p.startswith(str(PurePosixPath(path).parent) + '/')] if kind == 'skill' else [path]
        if kind == 'skill':
            for dependency in info.get('required_files', []):
                require(dependency in known, 'Missing declared skill resource: ' + dependency)
                require(not reviewed_nested or dependency.startswith(str(PurePosixPath(path).parent) + '/'),
                        'Reviewed nested skill resources must stay inside its entry directory')
                required.append(dependency)
        item = {'id': item_id, 'kind': kind, 'name': info.get('name', PurePosixPath(path).parent.name if kind == 'skill' else PurePosixPath(path).stem),
                'entry': path, 'required_files': sorted(set(required)), 'department_id': info.get('department_id', defaults.get(PurePosixPath(path).parts[2], 'unassigned') if kind == 'skill' else 'unassigned'),
                'dependencies': info.get('dependencies', [])}
        if kind == 'skill':
            if reviewed_nested:
                item['entry_layout'] = 'reviewed-nested'
            item['specialist_id'] = PurePosixPath(path).parts[3 if structured else 2]
            if structured:
                require(PurePosixPath(path).parts[2] in DEPARTMENTS, 'Unknown structured department')
                item['department_id'] = DEPARTMENTS[PurePosixPath(path).parts[2]]
            if len(item['specialist_id'].encode())>64 or not re.fullmatch(r'[a-z][a-z0-9]*(?:[-_][a-z0-9]+)*',item['specialist_id']):
                problems.append({'path':path,'code':'invalid_specialist_identity'})
            try:
                text, original_name = frontmatter(data)
                host_name = 'oracle-' + item_id
                require(host_name not in names, 'Duplicate host skill name')
                names.add(host_name)
                # The canonical OS never changes: adapt only bytes of this snapshot.
                adapted_text = re.sub(r'(?m)^name:[^\n\r]*', 'name: ' + host_name, text, count=1).replace('\r\n', '\n')
                header_end = re.match(r'\A---\n.*?\n---(?:\n|$)', adapted_text, re.S).end()
                if 'Modified for Oracle distribution' not in adapted_text[header_end:header_end + 300]:
                    adapted_text = adapted_text[:header_end] + '<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->\n' + adapted_text[header_end:]
                adapted = adapted_text.encode()
                if adapted != data:
                    adaptations.append({'path': path, 'field': 'name', 'from': original_name, 'to': host_name, 'source_sha256': sha(data)})
                    blobs[path] = adapted
                item['host_name'] = host_name
            except (Refused, UnicodeError) as error:
                problems.append({'path': path, 'code': 'invalid_skill_frontmatter', 'reason': str(error)})
        if info.get('license_reviewed') is not True or info.get('dependencies_reviewed') is not True:
            problems.append({'path': path, 'code': 'item_license_or_dependencies_unreviewed'})
        items.append(item)
    departments = {}
    for item in items:
        if item['department_id'] not in {'code','design','marketing','sales','research','content','unassigned',*DEPARTMENTS.values()}:
            problems.append({'path':item['entry'],'code':'invalid_department'})
        specialist = item.get('specialist_id')
        if specialist:
            if specialist in departments and departments[specialist] != item['department_id']:
                problems.append({'path':item['entry'],'code':'conflicting_specialist_department'})
            departments[specialist] = item['department_id']
    renamed = set()
    for rename in review.get('renames', []):
        item = next((item for item in items if item['id'] == rename.get('id')),None)
        require(item is not None and rename['id'] not in renamed and safe_path(rename.get('from','')) not in known and rename.get('to') == item['entry'], 'Rename requires a unique stable item and a matching new entry')
        renamed.add(rename['id'])
    require(len({item['id'] for item in items}) == len(items), 'Duplicate stable item identity')
    return items, adaptations, problems


def source_snapshot(repository):
    """Read pinned Git objects; working-tree changes and hooks are never executed."""
    def git(args, data=None):
        result = subprocess.run(['git', '-C', str(repository), *args], input=data, check=True, capture_output=True, timeout=120,
                                env={'PATH': '/usr/bin:/bin', 'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': '/dev/null', 'GIT_OPTIONAL_LOCKS': '0'})
        return result.stdout
    require(git(['rev-parse', PIN + '^{commit}']).decode().strip() == PIN, 'GBrain pin unavailable')
    rows, blobs, objects = [], {}, []
    for record in git(['ls-tree', '-rzl', PIN]).split(b'\0'):
        if not record:
            continue
        meta, name = record.split(b'\t', 1)
        mode, kind, object_id, size = meta.decode().split()
        require(kind == 'blob' and mode in ('100644', '100755'), 'Upstream snapshot contains unsupported links/submodules')
        path = safe_path(name.decode(), hidden=True)
        require(int(size) <= MAX_FILE, 'Upstream file exceeds package budget')
        objects.append((object_id, path, int(size), int(mode, 8) & 0o777))
    require(len(objects) <= MAX_FILES and sum(row[2] for row in objects) <= MAX_BYTES, 'Upstream snapshot exceeds budget')
    batch = git(['cat-file', '--batch'], ''.join(row[0] + '\n' for row in objects).encode())
    offset = 0
    for object_id, path, size, mode in objects:
        end = batch.index(b'\n', offset)
        require(batch[offset:end].decode() == object_id + ' blob ' + str(size), 'Upstream object stream does not match pinned inventory')
        data = batch[end + 1:end + 1 + size]
        require(len(data) == size and batch[end + 1 + size:end + 2 + size] == b'\n', 'Truncated upstream object stream')
        offset = end + 2 + size
        target = 'sources/gbrain/' + PIN + '/' + path
        rows.append({'path': target, 'source_path': path, 'kind': 'gbrain-source', 'size': len(data), 'mode': mode, 'source_sha256': sha(data)})
        blobs[target] = data
    require(offset == len(batch), 'Unexpected upstream object stream suffix')
    require(any(PurePosixPath(r['path']).name in LICENSE_NAMES for r in rows), 'Upstream license is missing')
    return rows, blobs


def make_packages(rows, blobs, release_id, base_url):
    packages, payloads, batch, total = [], {}, [], 0
    def flush():
        nonlocal batch, total
        if not batch:
            return
        kind = batch[0]['kind']
        package_id = kind + '-' + str(len(packages)).zfill(4)
        records = [{**{k: r[k] for k in ('path', 'sha256', 'size', 'mode')}, 'content_base64': base64.b64encode(blobs[r['path']]).decode()} for r in batch]
        data = canonical({'schema_version': SCHEMA, 'release_id': release_id, 'id': package_id, 'files': records})
        require(len(data) <= 44_000_000, 'Encoded package exceeds download limit')
        asset = package_id + '.json'
        payloads[asset] = data
        packages.append({'id': package_id, 'kind': kind, 'repository': 'https://github.com/garrytan/gbrain' if kind == 'gbrain-source' else 'https://github.com/nitroxinteligence/ORACLE-SKILLS',
                         'commit': PIN if kind == 'gbrain-source' else release_id, 'url': base_url + '/' + asset, 'asset': asset,
                         'bytes': len(data), 'expanded_bytes': total, 'sha256': sha(data), 'files': [r['path'] for r in batch], 'dependencies': []})
        for row in batch:
            row['package_id'] = package_id
        batch, total = [], 0
    for row in sorted(rows, key=lambda r: (r['kind'], r['path'])):
        if batch and (row['kind'] != batch[0]['kind'] or len(batch) == MAX_PACKAGE_FILES or total + row['size'] > MAX_PACKAGE_BYTES):
            flush()
        batch.append(row)
        total += row['size']
    flush()
    return packages, payloads


def build(source, release_id, sequence, review, gbrain_source, base_url):
    initial = inventory(source)
    report = {'schema_version': SCHEMA, 'inventory': initial, 'published': False, 'problems': list(initial['problems'])}
    excluded = {}
    for exclusion in review.get('exclusions', []):
        path = exclusion.get('path', '')
        row = next((r for r in initial['files'] if r['source_path'] == path), None)
        require(row is not None and path not in excluded, 'Excluded file absent or duplicated')
        require(exclusion.get('reason') and any(p['path'] == path and p['code'] == 'private_or_dependency_metadata' for p in initial['problems']), 'Only explicitly reported non-content metadata may be excluded')
        metadata_only = PurePosixPath(path).name == '.DS_Store' or ('node_modules' in PurePosixPath(path).parts and PurePosixPath(path).name in {'.package-map.json', '.pnpm-workspace-state-v1.json'})
        if exclusion.get('metadata_only') is True:
            require(metadata_only and row['size'] == exclusion.get('size'), 'Metadata-only exclusion is not an approved non-content file')
        else:
            require(sha(read_stable(source / path)) == exclusion.get('sha256'), 'Excluded metadata changed since review')
        excluded[path] = exclusion
    report['resolved_exclusions'] = list(excluded.values())
    report['problems'] = [p for p in report['problems'] if not (p['path'] in excluded and p['code'] in {'private_or_dependency_metadata', 'dataless'})]
    if report['problems']:
        return None, {}, report
    blobs, rows, source_hashes = {}, [], {}
    for source_row in initial['files']:
        if source_row['source_path'] in excluded:
            continue
        data = read_stable(source / source_row['source_path'])
        source_hashes[source_row['source_path']] = sha(data)
        blobs[source_row['path']] = data
        rows.append({k: v for k, v in source_row.items() if k != 'stamp'})
        rows[-1]['source_sha256'] = sha(data)
    report['source_inventory_sha256'] = sha(canonical(source_hashes))
    if review.get('source_inventory_sha256') != report['source_inventory_sha256'] or review.get('content_reviewed') is not True:
        report['problems'].append({'path': '.', 'code': 'exact_content_review_required'})
    content_adaptations = apply_reviewed_adaptations(blobs, review)
    additions = add_reviewed_supplements(rows, blobs, review)
    items, adaptations, problems = audit_portability(rows, blobs, review)
    adaptations = content_adaptations + adaptations
    report['problems'] += problems
    report['adaptations'] = adaptations
    report['items'] = items
    report['supplemental_files'] = additions
    # Export the review against final (including host-name adaptation) bytes for
    # the separate source mirror. No matching credential value is exported.
    report['publication_examples'] = {}
    report['machine_path_reviews'] = {}
    for path, data in blobs.items():
        original = next((a['source_sha256'] for a in adaptations if a['path'] == path and a['field'] == 'name'), sha(data))
        if original in review.get('publication_examples', {}):
            evidence = dict(review['publication_examples'][original])
            evidence['rule_counts'] = publication_rule_counts(data)
            check_publication_bytes(path, data, {sha(data): evidence})
            report['publication_examples'][sha(data)] = evidence
        evidence = review.get('machine_path_reviews', {}).get(path)
        if evidence and evidence.get('sha256') == original:
            report['machine_path_reviews'][path] = {**evidence, 'sha256': sha(data)}
    # Final membership + metadata scan catches additions, removals and changed ancestors.
    require(inventory(source) == initial, 'Inventory changed while reading; no release written')
    if report['problems']:
        return None, {}, report
    upstream_rows, upstream_blobs = source_snapshot(gbrain_source)
    rows += upstream_rows
    blobs.update(upstream_blobs)
    for row in rows:
        row['sha256'], row['size'] = sha(blobs[row['path']]), len(blobs[row['path']])
        owners = [item['id'] for item in items if row['path'] in item['required_files']]
        row['item_ids'] = owners
        row['type'] = 'markdown' if row['path'].lower().endswith('.md') else 'resource'
    require(len(rows) <= MAX_FILES and sum(r['size'] for r in rows) <= MAX_BYTES, 'Complete distribution exceeds supported budget')
    packages, payloads = make_packages(rows, blobs, release_id, base_url)
    counts = {kind: {'files': sum(r['kind'] == kind for r in rows), 'bytes': sum(r['size'] for r in rows if r['kind'] == kind), 'items': sum(i['kind'] == {'specialists': 'skill', 'prompts': 'prompt', 'tutorials': 'tutorial'}.get(kind) for i in items)} for kind in sorted({r['kind'] for r in rows})}
    minimum_oracle = '0.3.14' if any(i.get('entry_layout') == 'reviewed-nested' for i in items) else '0.3.3' if review.get('skills_layout') == 'department-specialist-skill' else '0.3.0'
    manifest = {'schema_version': SCHEMA, 'release_id': release_id, 'sequence': sequence, 'minimum_oracle': minimum_oracle,
                'adapter_commit': PIN, 'gbrain_version': VERSION, 'gbrain_commit': PIN, 'packages': packages, 'files': rows, 'items': items,
                'counts': counts, 'inventory_sha256': sha(canonical(rows)), 'source_inventory_sha256': report['source_inventory_sha256'],
                'licenses': review.get('licenses', []), 'adaptations': adaptations, 'supplemental_files': additions, 'renames': review.get('renames', []),
                'publication_examples': report['publication_examples'], 'machine_path_reviews': report['machine_path_reviews'],
                'capabilities': ['files', 'keyword-search', 'explicit-links', 'canonical-editing'],
                'components': {'runtime': {'source': 'signed-app-bundle', 'version': VERSION}, 'gbrain-method': {'source': 'signed-app-bundle', 'commit': PIN}}}
    if review.get('skills_layout') == 'department-specialist-skill':
        manifest['skills_layout'] = 'department-specialist-skill'
    require(manifest['licenses'], 'Distribution needs reviewed license inventory')
    return manifest, payloads, report


def sign_manifest(manifest, key_path, key_id):
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    info = key_path.lstat()
    require(not stat.S_IMODE(info.st_mode) & 0o077, 'Private signing key must be owner-only')
    key = serialization.load_pem_private_key(read_stable(key_path), password=None)
    require(isinstance(key, Ed25519PrivateKey), 'Distribution requires an Ed25519 signing key')
    payload = canonical(manifest)
    return canonical({'schema_version': SCHEMA, 'key_id': key_id, 'payload_base64': base64.b64encode(payload).decode(),
                      'signature_base64': base64.b64encode(key.sign(DOMAIN + payload)).decode()})


def write_reviewed_snapshot(manifest, payloads, output):
    """A separate publication tree; source OS and unsigned review stay untouched."""
    require(not output.exists() and not output.is_symlink(), 'Snapshot requires a new directory')
    output.mkdir(parents=True, exist_ok=False)
    fd = directory_fd(output)
    os.close(fd)
    expected = {row['path']: row for row in manifest['files'] if row['kind'] != 'gbrain-source'}
    written = {}
    for metadata in manifest['packages']:
        data = payloads[metadata['asset']]
        require(sha(data) == metadata['sha256'], 'Snapshot package digest mismatch')
        for row in decode(data)['files']:
            if row['path'] not in expected:
                continue
            record = expected[row['path']]
            content = base64.b64decode(row['content_base64'], validate=True)
            require(sha(content) == record['sha256'] and len(content) == record['size'], 'Snapshot file digest mismatch')
            target = output / safe_path(row['path'], hidden=True)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            target.chmod(record['mode'])
            written[row['path']] = sha(read_stable(target))
    require(set(written) == set(expected), 'Snapshot is incomplete')
    return {'schema_version': SCHEMA, 'release_id': manifest['release_id'], 'files': written, 'complete': True, 'published': False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--inventory-only', action='store_true')
    parser.add_argument('--version')
    parser.add_argument('--sequence', type=int)
    parser.add_argument('--review', type=Path)
    parser.add_argument('--gbrain-source', type=Path)
    parser.add_argument('--signing-key', type=Path)
    parser.add_argument('--key-id')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--snapshot', type=Path, help='Optional new reviewed tree for source-mirror --libraries all')
    args = parser.parse_args(argv)
    source = Path(os.path.abspath(args.source))
    require(not args.report.absolute().is_relative_to(source), 'Report must stay outside canonical source')
    # Output parents are checked before creating any files, including reports.
    args.report.parent.mkdir(parents=True, exist_ok=True)
    fd = directory_fd(args.report.parent)
    os.close(fd)
    require(not args.report.exists() and not args.report.is_symlink(), 'Choose a new report path; existing evidence is preserved')
    if args.inventory_only:
        report = inventory(source)
        args.report.write_bytes(canonical(report))
        print(json.dumps({'complete': report['complete'], 'counts': report['counts'], 'problems': len(report['problems']), 'report': str(args.report)}))
        return 0 if report['complete'] else 2
    require(args.version and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,79}', args.version), 'A portable immutable release ID is required')
    require(args.sequence and 0 < args.sequence <= 2**53 - 1 and args.review and args.gbrain_source and args.output, 'Sequence, review, GBrain source and output are required')
    require(not args.output.absolute().is_relative_to(source) and not args.output.exists(), 'Output must be a new directory outside source')
    if args.snapshot:
        require(not args.snapshot.absolute().is_relative_to(source) and not args.snapshot.exists(), 'Snapshot must be new and outside source')
    manifest, payloads, report = build(source, args.version, args.sequence, decode(read_stable(args.review)), args.gbrain_source,
                                     'https://github.com/nitroxinteligence/ORACLE-SKILLS/releases/download/' + args.version)
    if manifest is not None and (not args.signing_key or not args.key_id):
        report['problems'].append({'path': '.', 'code': 'signing_configuration_required'})
    args.report.write_bytes(canonical(report))
    if report['problems']:
        print(json.dumps({'ready': False, 'problems': len(report['problems']), 'report': str(args.report), 'published': False}))
        return 2
    require(re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', args.key_id) is not None, 'Invalid signing key ID')
    signed = sign_manifest(manifest, args.signing_key, args.key_id)
    args.output.mkdir(parents=True, exist_ok=False)
    fd = directory_fd(args.output)
    os.close(fd)
    for name, data in {**payloads, 'oracle-distribution.json': signed}.items():
        with (args.output / name).open('xb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    if args.snapshot:
        snapshot_receipt = write_reviewed_snapshot(manifest, payloads, args.snapshot)
        (args.output / 'snapshot-receipt.json').write_bytes(canonical(snapshot_receipt))
    # This marker is written last; the publisher must require it and every asset hash.
    (args.output / 'release-receipt.json').write_bytes(canonical({'schema_version': SCHEMA, 'release_id': args.version,
        'manifest_sha256': sha(signed), 'assets': {name: sha(data) for name, data in payloads.items()}, 'complete': True, 'published': False}))
    print(json.dumps({'ready': True, 'files': len(manifest['files']), 'packages': len(payloads), 'output': str(args.output), 'published': False}))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (Refused, OSError, ValueError, subprocess.SubprocessError) as error:
        print('Distribution refused: ' + str(error), file=sys.stderr)
        sys.exit(2)
