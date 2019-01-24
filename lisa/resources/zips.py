import falcon

from lisa.models.zip import Zip


class ZipResource(object):

    def on_get(self, req, resp):
        
        zip = req.get_param('zip', required=True)

        response = Zip.objects(zip=zip).exclude("id")
        
        resp.body = response.to_json()