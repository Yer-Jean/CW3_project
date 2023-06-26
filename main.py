from cw3.models.repository import Repository
from cw3.models.transaction import Transaction


def main():
    #  Инициализируем класс с данными по трансакциям
    repository: Repository = Repository()
    # Используя его методы получаем список из последних пяти успешных трансакций
    last_five_transaction: list[dict] = repository.get_last_five_transactions()
    # Инициализируем пять экземпляров класса Transaction
    for transaction in last_five_transaction:
        transaction = Transaction(transaction_id=transaction['id'],
                                  transaction_date=transaction['date'],
                                  transaction_description=transaction['description'],
                                  transaction_amount=transaction['operationAmount'],
                                  transaction_to=transaction['to'],
                                  transaction_from=transaction.get('from'))
        print(transaction)  # Одновременно выводим на печать вновь созданный экземпляр, используя метод класса __str__


if __name__ == '__main__':
    main()
