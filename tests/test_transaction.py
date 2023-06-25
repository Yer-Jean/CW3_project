from cw3.models.transaction import Transaction


def test_executed_transaction(data_for_tests):
    transactions = []
    for transaction in data_for_tests:
        transactions.append(Transaction(transaction['id'], transaction['date'], transaction['description'],
                                        transaction['operationAmount'], transaction['to'], transaction.get('from')))
    assert isinstance(transactions, list)
    assert len(transactions) == 8
    assert transactions[0].transaction_id == 716496732
    assert transactions[1].transaction_date == '08.12.2019'
    assert transactions[2].transaction_from == 'Visa Platinum 1246 37** **** 3588'
    assert transactions[3].transaction_to == 'Счет **3493'
