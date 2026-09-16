"""Cenários sintéticos do auxiliar de decisão; não são execuções de LLM ou publicação."""
import unittest
from gates import evaluate

BASE = {'context_validated':True, 'brief_approved':True, 'claims_supported':True, 'copy_approved':True}
IMAGE = {**BASE, 'visual_brief_approved':True, 'generation_requested':True, 'image_tool':True}
PUBLISH = {**BASE, 'artifacts_available':True, 'final_review':True, 'publication_authorized':True, 'publication_tool':True}
CASES = [
 ({'mode':'context'},'request-context'),
 ({'mode':'context','vault_access':True},'map-authorized-context'),
 ({'mode':'research'},'clarify-research-scope'),
 ({'mode':'research','research_question':True},'research-ready'),
 ({'mode':'audit'},'request-profile-material'),
 ({'mode':'audit','profile_material':True},'clarify-audit-scope'),
 ({'mode':'audit','profile_material':True,'audit_scope':True},'public-audit-only'),
 ({'mode':'audit','profile_material':True,'audit_scope':True,'private_metrics':True},'authorized-audit-ready'),
 ({'mode':'editorial'},'resolve-context'),
 ({'mode':'editorial','context_validated':True},'approve-brief'),
 ({'mode':'editorial','context_validated':True,'brief_approved':True},'verify-claims'),
 ({**BASE,'mode':'editorial'},'editorial-draft-ready'),
 ({**BASE,'mode':'visual-brief','copy_approved':False},'approve-copy'),
 ({**BASE,'mode':'visual-brief'},'visual-brief-ready'),
 ({**BASE,'mode':'image'},'approve-visual-brief'),
 ({**IMAGE,'mode':'image','is_edit':True},'request-edit-target'),
 ({**IMAGE,'mode':'image','user_portrait':True},'request-user-photo'),
 ({**IMAGE,'mode':'image','generation_requested':False},'brief-only'),
 ({**IMAGE,'mode':'image','image_tool':False},'generation-not-executed'),
 ({**IMAGE,'mode':'image'},'image-operation-ready'),
 ({**BASE,'mode':'review'},'request-artifacts'),
 ({**BASE,'mode':'review','artifacts_available':True,'critical_defects':True},'block-critical-defects'),
 ({**BASE,'mode':'review','artifacts_available':True},'review-ready'),
 ({**PUBLISH,'mode':'publish','final_review':False},'require-final-review'),
 ({**PUBLISH,'mode':'publish','publication_authorized':False},'require-publication-authorization'),
 ({**PUBLISH,'mode':'publish','publication_tool':False},'publication-not-executed'),
 ({**PUBLISH,'mode':'publish'},'authorized-publication-ready'),
]

class GateTests(unittest.TestCase):
    def test_27_workflow_scenarios(self):
        for data,expected in CASES:
            with self.subTest(expected=expected):
                result=evaluate(data)
                self.assertEqual(result['status'],expected)
                self.assertFalse(result['publication_executed'])
                self.assertFalse(result['tool_executed'])
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError): evaluate([])
        with self.assertRaises(ValueError): evaluate({'mode':'unknown'})
        self.assertEqual(evaluate({**BASE,'mode':'editorial','context_validated':'true'})['status'],'resolve-context')
    def test_privacy_and_unsupported_claims(self):
        self.assertEqual(evaluate({**BASE,'mode':'editorial','private_export_requested':True})['status'],'redact-context')
        self.assertEqual(evaluate({**BASE,'mode':'editorial','unsupported_personal_claim':True})['status'],'remove-unsupported-claims')

if __name__ == '__main__':
    unittest.main(verbosity=2)
