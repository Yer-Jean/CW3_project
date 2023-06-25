import json

from settings import DATA_PATH


class Repository:
    def __init__(self):
        self.data_path: str = DATA_PATH

    def read_json(self) -> list[dict]:
        """
        Метод считывает все записи из json-файла.
        Если файл не найден, то программа заканчивает работу
        """
        try:
            with open(self.data_path) as file:
                return json.load(file)
        except FileNotFoundError:
            print('\nНе найден файл с данными\n')
            exit()

    def get_all_transactions(self) -> list[dict]:
        """
        Метод возвращает в виде списка словарей все трансакции из json-файла
        """
        return self.read_json()

    @staticmethod
    def remove_empty_transactions(all_transactions: list[dict]) -> list[dict]:
        """
        Метод удаляет пустые записи из всех полученных трансакций
        и возвращает только непустые
        """
        all_transactions.remove({})
        return all_transactions

    @staticmethod
    def get_executed_transactions(non_empty_transactions: list[dict]) -> list[dict]:
        """
        Метод фильтрует трансакции по признаку EXECUTED (выполненные)
        и возвращает только их
        """
        return list(filter(lambda dic: (dic['state'] == 'EXECUTED'), non_empty_transactions))

    def get_last_five_transactions(self) -> list[dict]:
        """
        Метод возвращает пять последних по времени трансакций. Предварительно вычистив все
        трансакции от ошибочных, и отфильтровав их по выполненным
        """
        all_transactions: list[dict] = self.get_all_transactions()
        non_empty_transaction: list[dict] = self.remove_empty_transactions(all_transactions)
        executed_transactions: list[dict] = self.get_executed_transactions(non_empty_transaction)
        # Возвращаем пять последних трансакций, отсортировав список по дате
        return sorted(executed_transactions, key=lambda dictionary: dictionary['date'], reverse=True)[:5]
