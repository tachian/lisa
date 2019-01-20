import falcon

from .resources.bank_branches import BankBranchResource

api = application = falcon.API()

api.add_route('/bank_branches', BankBranchResource())