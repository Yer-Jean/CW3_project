import re
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
        self.transaction_from: str = self.numbers_masking(transaction_from) if transaction_from else ''
        self.transaction_to: str = self.numbers_masking(transaction_to)
        self.transaction_amount: str = transaction_amount['amount']
        self.transaction_currency: str = transaction_amount['currency']['name']

        self.separator: str = ' -> ' if transaction_from else ''

    def convert_datetime_to_date(self, transaction_date: str) -> str:
        date_: datetime = datetime.fromisoformat(transaction_date)
        return date_.strftime("%d.%m.%Y")

    def numbers_masking(self, account_number: str) -> str:
        if re.findall(r'(\d{20})', account_number):
            return re.sub(r'\d{16}(\d{4})', r'**\1', account_number)
        return re.sub(r'(\d{4})(\d{2})\d{6}(\d{4})', r'\1 \2** **** \3', account_number)

    def __repr__(self) -> str:
        return f'ID: {self.transaction_id}\n' \
               f'Date: {self.transaction_date}\n' \
               f'Description: {self.transaction_description}\n' \
               f'From: {self.transaction_from}\n' \
               f'To: {self.transaction_to}\n' \
               f'Amount: {self.transaction_amount} {self.transaction_currency}\n'

    def __str__(self) -> str:
        return f'{self.transaction_date } {self.transaction_description}\n' \
               f'{self.transaction_from}{self.separator}{self.transaction_to}\n' \
               f'{self.transaction_amount} {self.transaction_currency}\n'


if __name__ == '__main__':
    transaction = Transaction(596171168, "2018-07-11T02:26:18.671407", "Перевод организации",
                              {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
                              "Счет 72731966109147704472", "Visa Gold 5999414228426353")
    print(repr(transaction))
    print(transaction)
