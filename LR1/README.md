## Цель и постановка задачи
Цель: изучить основные возможности языка Python для разработки программных систем с интерфейсом командной строки (CLI)

## Вариант 1 
### Модель банкомата
Для реализации были созданы 4 базы данных: 
info_of_client_now – хранит данные о карте, которая сейчас находится в банкомате.
user_bd – хранит информацию о всех пользователях.
card_bd – хранит информацию о всех картах (id, cvv, дата выпуска).
bank_bd – хранит информацию о счетах в банке (id карты, баланс, пароль, id владельца).
### Main
<details>
<summary>Раскрыть</summary>
В main.py мы, используя библиотеку click, реализуем cli. 
Создаем группу команд cli.
 
Создаем такие команды как:
1)	авторизация
![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/authorization.jpg)
2)	пополнение баланса
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/add_money.jpg)
3)	снятие денег
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/withdrow.jpg)
4)	перевод на другую карту
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/transfer.jpg)
5)	получение баланса
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/get_balance.jpg)
6)	перевод на телефонный номер
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/transfer_to_phone.jpg)
7)	регистрация новой карты
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/register.jpg)
Потом добавляем  все команды в группу
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/add_to_group.jpg)
И main-функция
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/main.jpg)
</details>