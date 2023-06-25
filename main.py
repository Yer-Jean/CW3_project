from cw3.models.repository import Repository
from cw3.models.transaction import Transaction


def main():
    repository: Repository = Repository()
    last_five_transaction = repository.last_five_transactions()
    for transaction in last_five_transaction:
        transaction = Transaction(transaction_id=transaction['id'],
                                  transaction_date=transaction['date'],
                                  transaction_description=transaction['description'],
                                  transaction_amount=transaction['operationAmount'],
                                  transaction_to=transaction['to'],
                                  transaction_from=transaction.get('from'))
        print(transaction)


if __name__ == '__main__':
    main()
