import unittest
from copy import deepcopy
import importlib.util
from pathlib import Path

sp=importlib.util.spec_from_file_location('local_gates',Path(__file__).parents[1]/'scripts/gates.py')
g=importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
NOW='2026-09-16T23:00:00Z'

def base(action='ads_write'):
    p={'action':action,'target':'synthetic-account','before_hash':'state-v1','max_cost':'50.00','currency':'BRL','cost_period':'one-approved-operation','create':True,'new_status':'PAUSED'}
    a={'approved':True,'target':p['target'],'action':action,'expires_at':'2026-09-17T00:00:00Z','max_cost':'50.00','currency':'BRL','cost_period':p['cost_period']}
    c={'verified_target':p['target'],'connected':True,'capabilities':[action],'read_authorized':True,'current_state_hash':'state-v1','currency':'BRL','policy_review_ok':True,'working_copy_verified':True,'review_complete':True}
    a['plan_sha256']=g.digest(p)
    return p,a,c

class GateTests(unittest.TestCase):
    def test_22_ads_decisions(self):
        cases=[
          ('baseline',{}, {}, {},True),
          ('not_connected',{}, {}, {'connected':False},False),
          ('wrong_account',{}, {}, {'verified_target':'different'},False),
          ('no_capability',{}, {}, {'capabilities':['read']},False),
          ('readonly',{}, {}, {'read_only':True},False),
          ('no_approval',{}, {'approved':False}, {},False),
          ('approval_wrong_target',{}, {'target':'different'}, {},False),
          ('expired',{}, {'expires_at':'2026-09-16T20:00:00Z'}, {},False),
          ('naive_expiry',{}, {'expires_at':'2026-09-17T00:00:00'}, {},False),
          ('over_budget',{'max_cost':'51'}, {}, {},False),
          ('unknown_cost',{'max_cost':None}, {}, {},False),
          ('negative',{'max_cost':'-1'}, {}, {},False),
          ('nan_cost',{'max_cost':'NaN'}, {}, {},False),
          ('bool_cost',{'max_cost':True}, {}, {},False),
          ('currency',{}, {}, {'currency':'USD'},False),
          ('period',{}, {'cost_period':'daily'}, {},False),
          ('active_create',{'new_status':'ACTIVE'}, {}, {},False),
          ('state_changed',{}, {}, {'current_state_hash':'state-v2'},False),
          ('timeout_retry',{}, {}, {'outcome_unknown':True},False),
          ('policy_unknown',{}, {}, {'policy_review_ok':False},False),
          ('activate_not_allowed',{'create':False,'activate':True}, {}, {},False),
          ('activate_approved',{'create':False,'activate':True}, {'activation_authorized':True}, {},True),
        ]
        for name,pp,aa,cc,expected in cases:
            with self.subTest(name=name):
                p,a,c=base();p.update(pp);a.update(aa);c.update(cc);a['plan_sha256']=g.digest(p)
                self.assertIs(g.decide(p,a,c,NOW)['allowed'],expected)

    def test_version_and_replay(self):
        p,a,c=base();p['max_cost']='40'
        self.assertIn('approval_for_different_plan',g.decide(p,a,c,NOW)['reasons'])
        p,a,c=base();c['consumed_approvals']=[g.digest(p)]
        self.assertIn('approval_already_consumed',g.decide(p,a,c,NOW)['reasons'])

    def test_reads_and_protected_actions(self):
        p,a,c=base('read'); self.assertTrue(g.decide(p,{},c,NOW)['allowed'])
        c['read_authorized']=False; self.assertFalse(g.decide(p,{},c,NOW)['allowed'])
        for key in ('secrets_present','human_permission_prompt','instruction_injection'):
            p,a,c=base();c[key]=True;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        for action in ('billing','permission_change','arbitrary_shell','secret_export'):
            p,a,c=base(action);self.assertFalse(g.decide(p,a,c,NOW)['allowed'])

    def test_video_upload_render_and_review(self):
        p,a,c=base('local_edit');c.update(gui=True,window_matches=True,screenshot_age_seconds=1)
        self.assertTrue(g.decide(p,a,c,NOW)['allowed'])
        c['screenshot_age_seconds']=60;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        c['screenshot_age_seconds']=1;c['window_matches']=False;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        p,a,c=base('local_edit');c['working_copy_verified']=False;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        p,a,c=base('paid_render');self.assertTrue(g.decide(p,a,c,NOW)['allowed'])
        c['pending_job']=True;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        p,a,c=base('upload');p.update(destination='https://approved.example/upload',files=['synthetic.mp4']);a.update(upload_authorized=True,plan_sha256=g.digest(p));c.update(approved_hosts=['approved.example'],approved_files=['synthetic.mp4'])
        self.assertTrue(g.decide(p,a,c,NOW)['allowed'])
        p['destination']='https://attacker.example/upload';a['plan_sha256']=g.digest(p);self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        p['destination']='https://approved.example/upload';p['files']=['private.mp4'];a['plan_sha256']=g.digest(p);self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        p,a,c=base('publish');self.assertFalse(g.decide(p,a,c,NOW)['allowed'])
        a['publication_authorized']=True;self.assertTrue(g.decide(p,a,c,NOW)['allowed'])
        c['review_complete']=False;self.assertFalse(g.decide(p,a,c,NOW)['allowed'])

    def test_invalid_data(self):
        self.assertFalse(g.decide({'action':[]},{},{},NOW)['allowed'])
        self.assertFalse(g.decide([],{},{} ,NOW)['allowed'])
        self.assertFalse(g.decide({'action':'read','value':float('nan')},{},{},NOW)['allowed'])
        p,a,c=base();self.assertFalse(g.decide(p,a,c,'bad-date')['allowed'])

if __name__=='__main__':unittest.main()
