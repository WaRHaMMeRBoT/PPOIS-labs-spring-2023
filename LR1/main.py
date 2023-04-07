from Make import Make
from Run import Run
import click
import copy

@click.command()
@click.option('-w', required=True, help='File for way')  # имя файла с путями
@click.option('-p', required=True, help='File for products')  # (-p products) имя файла с продуктами
@click.option('-s', required=True, help='Start')  # -s start
@click.option('-m', default='', help='For automatic operation')  # для автоматической работы жд (-m myself)
@click.option('-d', default=0, help='How many day')  # кол-во дней
@click.option('-n', default=False, help='No generate new trains/station?')  # для создания новых поездов и станций и удаляет предыдущие
def main(p, w, s, m, d, n):
    # Читаем пути
    f = open(w, 'r')
    way = []
    w = []
    temp = f.readlines()
    for i in temp:
        for j in range(len(i)):
            if not i[j] == '\n' and not i[j] == ',' and not i[j] == ' ':
                w.append(int(i[j]))
        way.append(list(w))
        w.clear()
    f.close()

    # Читаем продукты
    f = open(p)
    products = f.readlines()
    for i in range(len(products)):
        if products[i][-1] == '\n':
            products[i] = products[i][0:len(products[i]) - 1]
    f.close()

    if n == False:
        #Чтение поездов из файла
        f = open('trains')
        lines = f.read().splitlines()
        f.close()

        dic = {}

        trains = []

        for line in lines:
            if line == '===':
                dic_1 = copy.deepcopy(dic)
                trains.append(dic_1)
                dic.clear()
                continue
            temp = line.split(';')
            key = temp[0]
            value = temp[1]
            dic.update({key: value})

        for temp in trains:
            data_dict = eval(temp['train'])
            temp['train'] = data_dict
            data_list = []
            for i in temp['list']:
                if not i == '[' and not i == ']' and not i == ' ' and not i == ',':
                    data_list.append(int(i))
            temp['list'] = data_list
            if temp['make'] == 'True':
                temp['make'] = True
            else:
                temp['make'] = False
        #Чтение станции из файла
        f = open('station')
        lines = f.read().splitlines()
        f.close()

        dic = {}
        station = []

        for line in lines:
            if line == '===':
                dic_1 = copy.deepcopy(dic)
                station.append(dic_1)
                dic.clear()
                continue
            temp = line.split(';')
            key = temp[0]
            value = temp[1]
            dic.update({key: value})

        for temp in station:
            a = int(temp['number'])
            temp['number'] = a
            data_dict = eval(temp['storage'])
            temp['storage'] = data_dict
            data_list = []
            for i in temp['queue']:
                if not i == '[' and not i == ']' and not i == ',' and not i == ' ':
                    data_list.append(int(i))
            temp['queue'] = data_list
            data_list1 = []
            for i in temp['roads']:
                if not i == '[' and not i == ']' and not i == ',' and not i == ' ':
                    data_list1.append(int(i))
            temp['roads'] = data_list1
            b = int(temp['train_number'])
            temp['train_number'] = b

        task = str(str(s) + ' ' + str(m) + ' ' + str(d))
        run = Run(station, trains, task)
        run.handler()
        # Запись поездоф в файл
        f = open('trains', 'w')
        for i in run.train_list:
            for key, item in i.items():
                f.write('{};{}\n'.format(key, item))
            f.write("===\n")
        f.close()
        # Запись станций в файл
        f = open('station', 'w')
        for i in run.station_list:
            for key, value in i.items():
                f.write('{};{}\n'.format(key, value))
            f.write('===\n')
        f.close()

    else:
        make = Make(products, way)
        task = str(str(s) + ' ' + str(m) + ' ' + str(d))
        run = Run(make.Make_Station_list(), make.Make_Trane_list(), task)
        run.handler()
        # Запись поездов в файл
        f = open('trains', 'w')
        for i in run.train_list:
            for key, item in i.items():
                f.write('{};{}\n'.format(key, item))
            f.write("===\n")
        f.close()
        # Запись станций в файл
        f = open('station', 'w')
        for i in run.station_list:
            for key, value in i.items():
                f.write('{};{}\n'.format(key, value))
            f.write('===\n')
        f.close()

if __name__ == '__main__':
    main()
