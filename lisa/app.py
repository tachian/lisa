import falcon

from .resources.bank_agencies import BankAgencyResource


api = application = falcon.API()

api.add_route('/bank_agencies', BankAgencyResource())