import falcon

from tests import TestCase
from lisa.models.bank_branch import BankBranch


class BankAgency(TestCase):

    def test_get_branch_commom(self):
        expect_response = [{'bank': '001', 'branch': '0001'}]

        bank_branch = BankBranch(bank='001', branch='0001')
        bank_branch.save()

        response = self.client().simulate_get('/bank_branches', params={'bank': '001', 'branch': '0001'})

        assert response.json == expect_response
        assert response.status == falcon.HTTP_OK

    def test_get_branch_invalid_parameters(self):
        
        # Without branch
        response = self.client().simulate_get('/bank_branches', params={'bank': '001'})
        assert response.json == {'title': 'Missing parameter', 'description': 'The "branch" parameter is required.'}
        assert response.status == falcon.HTTP_BAD_REQUEST

        # Without bank
        response = self.client().simulate_get('/bank_branches', params={'branch': '0001'})
        assert response.json == {'title': 'Missing parameter', 'description': 'The "bank" parameter is required.'}
        assert response.status == falcon.HTTP_BAD_REQUEST