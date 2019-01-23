import falcon

from lisa.models.occupation import Occupation


class OccupationResource(object):

    def on_get(self, req, resp):
        
        post = req.get_param('post', required=True)

        occupation = Occupation.objects(post=post).exclude("id")
        
        resp.body = occupation.to_json()