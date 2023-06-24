import json

from settings import DATA_PATH


class Repository:
    def __init__(self):
        self.data_path: str = DATA_PATH

    def read_json(self) -> list[dict]:
        with open(self.data_path) as file:
            return json.load(file)

    def last_five_transactions(self) -> list[dict]:
        all_transactions: list[dict] = self.read_json()
        all_transactions.remove({})
        executed_transactions: list[dict] = list(filter(lambda dic: (dic['state'] == 'EXECUTED'), all_transactions))
        return sorted(executed_transactions, key=lambda dictionary: dictionary['date'], reverse=True)[:5]
