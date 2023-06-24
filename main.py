from cw3.models.repository import Repository


def main():
    repository: Repository = Repository()
    last_five_transaction = repository.last_five_transactions()
    print(last_five_transaction)


if __name__ == '__main__':
    main()
