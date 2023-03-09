## **Установка необходимых зависимостей**

    pip install kivymd

## **Описание проекта**

Приложение содержит таблицу со списком студентов. В таблице содержатся колонки:

1. ФИО студентов
2. Курс
3. Группа
4. Общее количество работ
5. Количество выполненных работ
6.  Язык программирования

!['base_view.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/base_view.jpg)

## **Окно добавления новых записей**

Окно добавление содежит поля:

1. ФИО - ограничение 100 **символов**
2. Курс - ограничение 1 **цифра**
3. Группа - ограничени 6 **цифр**
4. Общее количество работ - только **цифры**
5. Количество выполненных работ - только **цифры**
6.  Язык программирования - ограничени 100 **символов**

!['add_new.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/add_new.jpg)

При ошибке добавления открывается диалоговое окно с ошибкой:

!['error.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/error.jpg)

## **Окно фильтра записей**

!['filter.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/filter.jpg)

Поля **Количество выполненных работ** и **Язык программирования** собраются системой и выводятся выпадающим списком

## **Результаты поиска студентов**

!['filter_result.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/filter_result.jpg)

## **Удаление записей**

Для удаление записей необходимо отметить необходимые строки и подтвердить их удаление.

!['delete.jpg'](https://github.com/KonstantinS343/Kivy_table/raw/master/img/delete.jpg)
