import falcon

from lisa.models.bank_branch import BankBranch


class BankBranchResource(object):

    def on_get(self, req, resp):

        doc = []
        errors = []
        
        bank = req.get_param('bank', required=True)
        branch = req.get_param('branch', required=True)

        bankBranch = BankBranch.objects(bank=bank, branch=branch)
        doc = bankBranch.to_json()
        
        resp.body = doc
