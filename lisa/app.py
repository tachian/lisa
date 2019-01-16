import falcon

from .bank_agencies import Resource as ResourceBankAgency


api = application = falcon.API()

bank_agencies = ResourceBankAgency()
api.add_route('/bank_agencies', bank_agencies)