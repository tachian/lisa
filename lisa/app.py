import falcon

from .resources.bank_branches import BankBranchResource
from .resources.occupations import OccupationResource

api = application = falcon.API()

api.add_route('/bank_branches', BankBranchResource())
api.add_route('/occupations', OccupationResource())