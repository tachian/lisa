import pytest
import falcon

from tests import TestCase
from tests.conftest import client
from lisa.models.bank_branch import BankBranch


class BankAgency(TestCase):

    def test_get_branch(self):
        expect_response = [{'bank': '001', 'branch': '0001'}]

        bank_branch = BankBranch(bank='001', branch='0001')
        bank_branch.save()

        response = client().simulate_get('/bank_branches', params={'bank': '001', 'branch': '0001'})

        assert response.json == expect_response
        assert response.status == falcon.HTTP_OK