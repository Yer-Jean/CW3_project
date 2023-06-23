# Курсовая работа №3
### Курс "Основы backend-разработки"


## Код для виджета «Операции по счетам»
> IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.

## Задача
Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>


### Пример вывода для одной операции:

> 14.10.2018 Перевод организации
> 
> Visa Platinum 7000 79** **** 6361 -> Счет **9638
> 
> 82771.72 руб.

### Требования

- Последние 5 выполненных (EXECUTED) операций выведены на экран.
- Операции разделены пустой строкой.
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Сверху списка находятся самые последние операции (по дате).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX 
(видны только последние 4 цифры номера счета).

### Данные
По каждой операции есть следующие данные в файле operations.json:

- `id` — id транзакции
- `date` — информация о дате совершения операции
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутствовать)
- `to` — куда

### Критерии выполнения

- [ ]  Проект выложили на GitHub.
- [ ]  Есть файл .gitignore
- [ ]  Оформили файл README.md.
- [ ]  В проекте есть минимум 2 ветки, причем разработка ведется в `develop`, а стабильная версия на момент сдачи проекта лежит в ветке `main`.
- [ ]  Разработка проекта ведется в виртуальном окружении, в проекте есть информация о требованиях проекта (зависимостях).
- [ ]  К проекту написали тесты с покрытием не менее 80%.
- [ ]  Тесты написали на `pytest` или `unittest`.
- [ ]  Проект структурированный, читаемый, каждая функция — не более 50 строк.
- [ ]  Работа с файлом ведется через библиотеку json
