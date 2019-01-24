# -*- coding: utf-8 -*-

import falcon

from tests import TestCase
from lisa.models.occupation import Occupation


class TestOccupation(TestCase):

    def test_get_occupation_commom(self):
        expect_response = [{'post': u'teste ocupação', 'code': '999'}]

        occupation = Occupation(post=u'teste ocupação', code='999')
        occupation.save()

        response = self.client().simulate_get('/occupation', params={'post': u'teste ocupação'})

        assert response.json == expect_response
        assert response.status == falcon.HTTP_OK

    def test_get_occupation_invalid_parameters(self):
        
        response = self.client().simulate_get('/occupation')
        assert response.json == {'title': 'Missing parameter', 'description': 'The "post" parameter is required.'}
        assert response.status == falcon.HTTP_BAD_REQUEST

    def test_get_occupation_empty_response(self):
        
        occupation = Occupation(post='teste 123')
        occupation.save()

        response = self.client().simulate_get('/occupation', params={'post': 'XXX'})

        assert response.json == []
        assert response.status == falcon.HTTP_OK
