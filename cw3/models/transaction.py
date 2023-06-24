from datetime import datetime


class Transaction:
    def __init__(self, transaction_id: int,
                 transaction_date: str,
                 transaction_description: str,
                 transaction_amount: dict,
                 transaction_to: str,
                 transaction_from: str = None) -> None:
        self.transaction_id: int = transaction_id
        self.transaction_date: str = self.convert_datetime_to_date(transaction_date)
        self.transaction_description: str = transaction_description
        self.transaction_from: str = transaction_from if transaction_from else None
        self.transaction_to: str = transaction_to
        self.transaction_amount: str = transaction_amount['amount']
        self.transaction_currency: str = transaction_amount['amount']['currency']['name']

        self.separator: str = ' -> ' if transaction_from else None

    def convert_datetime_to_date(self, transaction_date: str) -> str:
        date_ = datetime.fromisoformat(transaction_date)
        return date_.strftime("%d.%m.%Y")

    def __repr__(self) -> str:
        return f'Transaction Date: {self.transaction_date}\n' \
               f'Transaction Description: {self.transaction_description}\n' \
               f'Transaction Amount: {self.transaction_amount}\n'

    def __str__(self) -> str:
        return f'{self.transaction_date } {self.transaction_description}\n' \
               f'{self.transaction_from}{self.separator}{self.transaction_to}\n' \
               f'{self.transaction_amount} {self.transaction_currency}\n'
