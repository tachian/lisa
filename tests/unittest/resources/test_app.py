import pytest
import falcon

from falcon import testing
from lisa.app import api
from lisa.models.bank_branch import BankBranch

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_get_branch(client):

    bank_branch = BankBranch(bank='001', branch='0001')
    bank_branch.save()

    response = client.simulate_get('/bank_branches', ['bank'='001', 'branch'='0001'])
    import pdb; pdb.set_trace()

    assert response.json == ''
    assert response.status == falcon.HTTP_OK