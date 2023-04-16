## Цель и постановка задачи
Цель: изучить основные возможности языка Python для разработки программных систем с интерфейсом командной строки (CLI)

## Вариант 1 
### Модель банкомата
Для реализации были созданы 4 базы данных: <br>
info_of_client_now – хранит данные о карте, которая сейчас находится в банкомате.<br>
user_bd – хранит информацию о всех пользователях.<br>
card_bd – хранит информацию о всех картах (id, cvv, дата выпуска).<br>
bank_bd – хранит информацию о счетах в банке (id карты, баланс, пароль, id владельца).<br>
### Main
<details>
<summary>Раскрыть</summary>
В main.py мы, используя библиотеку click, реализуем cli. 
Создаем группу команд cli.
 
Создаем такие команды как:
1)	авторизация <br>
![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/authorization.jpg)<br>
2)	пополнение баланса<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/add_money.jpg)<br>
3)	снятие денег<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/withdraw.jpg)<br>
4)	перевод на другую карту<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/transfer.jpg)<br>
5)	получение баланса<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/balance.jpg)<br>
6)	перевод на телефонный номер<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/transfer_to_phone.jpg)<br>
7)	регистрация новой карты<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/register.jpg)<br>
Потом добавляем  все команды в группу<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/add_to_group.jpg)<br>
И main-функция<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/main/main.jpg)<br>
</details>

### Cash machine
<details>
<summary>Раскрыть</summary>
В cash_machine.py мы, реализуем основную логику программы. Здесь мы производим все операции с базами данных 
 
Создаем такие команды как:
1)	авторизация <br>
![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/authorization.jpg)<br>
2)	пополнение баланса<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/add_money.jpg)<br>
3)	снятие денег<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/withdraw.jpg)<br>
4)	перевод на другую карту<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/transfer.jpg)<br>
5)	получение баланса<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/get_balance.jpg)<br>
6)	регистрация новой карты<br>
 ![alt text](https://github.com/aleshkey/PPOIS-labs-spring-2023/blob/lw1/LR1/images/cash_machine/register.jpg)<br>
</details>