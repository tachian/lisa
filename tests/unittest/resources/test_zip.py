# -*- coding: utf-8 -*-

import falcon

from tests import TestCase
from lisa.models.zip import Zip


class TestZip(TestCase):

    def test_get_zip_commom(self):
        expect_response = [{'zip': '05658020', 'city': u'São Paulo'}]

        zip = Zip(zip='05658020', city=u'São Paulo')
        zip.save()

        response = self.client().simulate_get('/zip', params={'zip': '05658020'})

        assert response.json == expect_response
        assert response.status == falcon.HTTP_OK

    def test_get_zip_invalid_parameters(self):
        
        response = self.client().simulate_get('/zip')
        assert response.json == {'title': 'Missing parameter', 'description': 'The "zip" parameter is required.'}
        assert response.status == falcon.HTTP_BAD_REQUEST

    def test_get_occupation_empty_response(self):
        
        zip = Zip(zip='05658020')
        zip.save()

        response = self.client().simulate_get('/zip', params={'zip': 'XXX'})

        assert response.json == []
        assert response.status == falcon.HTTP_OK