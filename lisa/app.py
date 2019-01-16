import falcon

from .bank_agencies import Resource


api = application = falcon.API()

bank_agencies = Resource()
api.add_route('', {'Favor definir qual pesquisa deseja efetuar.'})
api.add_route('/bank_agencies', bank_agencies)