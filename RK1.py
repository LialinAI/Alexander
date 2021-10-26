# используется для сортировки
from operator import itemgetter
 
class Disk:
    """CD-disk"""
    def __init__(self, id, name, type, description, amount, lib_id):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.amount = amount
        self.lib_id = lib_id
 
class Lib:
    """Library Of CD-disks"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DiskLib:
    """
    'CD-disks in the library' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lib_id, disk_id):
        self.lib_id = lib_id
        self.disk_id = disk_id
 
# Libraries
Libs = [
    Lib(1, 'Films lib'),
    Lib(2, 'Music lib'),
    Lib(3, 'Software utilities lib'),
]
 
# CD-disks
Disks = [
    Disk(1, 'Seven', 'film', 'thriller', 5, 1 ),
    Disk(2, 'Gorillaz', 'music', 'pop', 10, 2),
    Disk(3, 'Baobab', 'software', 'linux', 3, 3),
    Disk(4, 'CCleaner', 'software', 'windows', 2, 3),
    Disk(5, 'Slipknot', 'music', 'rock', 4, 2),
    Disk(6, 'Aphex Twin', 'music', 'electronic', 1, 2),
    Disk(7, 'The Big Lebowski', 'film', 'comedy', 6, 1),
    Disk(8, 'American history X', 'film', 'drama', 7, 1),
]
 
Disks_Libs = [
    DiskLib(1,1),
    DiskLib(2,2),
    DiskLib(3,3),
    DiskLib(3,4),
    DiskLib(2,5),
    DiskLib(2,6),
    DiskLib(1,7),
    DiskLib(1,8),
]
 
def main():
    """Main"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(e.name, e.type, e.description, e.amount, d.name) 
        for d in Libs 
        for e in Disks 
        if e.lib_id==d.id]

    # print(one_to_many)
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.lib_id, ed.disk_id) 
        for d in Libs 
        for ed in Disks_Libs 
        if d.id==ed.lib_id]
    # print(many_to_many_temp)
    
    many_to_many = [(e.name, e.description, e.amount, lib_name) 
        for lib_name, lib_id, disk_id in many_to_many_temp
        for e in Disks if e.id==disk_id]
    # print(many_to_many)
 
    print('Task Г1')
    res_11 = [(e.description, e.name, d.name)
                for d in Libs
                for e in Disks
                if (e.lib_id == d.id)&(d.name[0] == 'M')]
    print(res_11)

    print('\nTask Г2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for d in Libs:
        # Список дисков библиотеки
        d_disks = list(filter(lambda i: i[4]==d.name, one_to_many))
        # print(d_disks)
        # Если библиотека не пусая       
        if len(d_disks) > 0:
            # Количество дисков
            d_amount = [amount for _, _,_,amount,_ in d_disks]
            # Наибольшее количество одинаковых дисков в библиотеке
            d_amount_max = max(d_amount)
            res_12_unsorted.append((d.name, d_amount_max))
 
    # Сортировка по наибольшему количеству одинаковых дисков в библиотеке
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
 
    print('\nTask Г3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)

if __name__ == '__main__':
    main()

