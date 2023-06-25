import pytest

from cw3.models.repository import Repository
from settings import DATA_PATH

def test_correct_data():
    all_transactions = Repository().all_transactions()
    assert isinstance(all_transactions, list)
    assert len(all_transactions) == 101

# def test_read_json():
#     data_path = DATA_PATH
#     # data_path = 'operations123.json'
#     with pytest.raises(FileNotFoundError):
#         Repository(data_path).read_json()
#
# def test_executed_transaction(data_for_tests):
#     # transactions = Repository().all_transactions()
#     transactions = Repository()
#     oper = transactions.all_transactions()
#     data = data_for_tests
#     assert len(transactions) == 101

def test_get_all_transaction(data_for_tests):
    # transactions = Repository().all_transactions()
    transactions = Repository()
    oper = transactions.all_transactions()
    data = data_for_tests
    assert len(data) == 8

def test_last_five_transactions(data_for_tests):
    last_five_transactions = Repository().last_five_transactions()
    assert len(last_five_transactions) == 5
    # assert last_five_transactions[0].

