import falcon

from .resources.bank_branches import BankBranchResource
from .resources.occupations import OccupationResource
from .resources.zips import ZipResource

api = application = falcon.API()

api.add_route('/bank_branch', BankBranchResource())
api.add_route('/occupation', OccupationResource())
api.add_route('/zip', ZipResource())