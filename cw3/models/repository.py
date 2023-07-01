import json

from settings import DATA_PATH


class Repository:
    """
    Класс Repository содержит всё, что необходимо для чтения данных из
    файла и их подготовке для дальнейшей работы программы
    """
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
            exit(2)

    def get_all_transactions(self) -> list[dict]:
        """
        Метод возвращает в виде списка словарей все трансакции из json-файла
        """
        return self.read_json()

    def remove_empty_transactions(self, all_transactions: list[dict]) -> list[dict]:
        """
        Метод удаляет пустые записи из всех полученных трансакций
        и возвращает только непустые
        """
        # all_transactions.remove({})
        # return all_transactions

        # Изменил код после проверки, так как remove упадет, если не найдет пустой список
        return list(filter(None, all_transactions))

    def get_executed_transactions(self, non_empty_transactions: list[dict]) -> list[dict]:
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
        # Получаем из файла все записи трансакций
        all_transactions: list[dict] = self.get_all_transactions()
        # Удаляем из полученных записей пустые
        non_empty_transaction: list[dict] = self.remove_empty_transactions(all_transactions)
        # Фильтруем эти записи по признаку выполнения (EXECUTED)
        executed_transactions: list[dict] = self.get_executed_transactions(non_empty_transaction)
        # И возвращаем пять последних трансакций, отсортировав список по дате
        return sorted(executed_transactions, key=lambda dictionary: dictionary['date'], reverse=True)[:5]
