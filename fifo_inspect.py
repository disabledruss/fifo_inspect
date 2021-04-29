import os

# инспектор файлов и каталогов
print('Где будем считать Каталоги или Файлы?')
# выбор устройства
device = input('Путь:').lower()
dev_c = ['c', 'с']
dev_d = ['d', 'в']
dev_e = ['e', 'у']
dev_f = ['f', 'а']
if len(device) == 1:
    if device in dev_c:
        path = 'C:\\'
    elif device in dev_d:
        path = 'D:\\'
    elif device in dev_e:
        path = 'E:\\'
    elif device in dev_f:
        path = 'F:\\'
else:
    path = device
# выбор расширения
expansion = input('Введите расширение Файла если считаем Файлы или "-" если считаем Каталоги: ')
os.system('cls')

def file_searcher(path, name):
    '''функция поиска файлов по имени, возвращает список найденых файлов с полным путём и именем.'''
    file_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            f_name = filename.split('.')
            if name in f_name:
                some_file = str(os.path.join(dirpath, filename))
                if 'RECYCLE' not in some_file:
                    file_list.append(some_file)
    return file_list

def file_counter(path, exp):
    '''функция подсчёта файлов заданного расширения. возвращает список файлов с указанием пути'''
    file_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            f_name = filename.split('.')
            if len(f_name) < 2:
                continue
            if exp == '*':
                some_file = str(os.path.join(dirpath, filename))
                if 'RECYCLE' not in some_file:
                    file_list.append(some_file)
            elif exp in f_name[1]:
                some_file = str(os.path.join(dirpath, filename))
                if 'RECYCLE' not in some_file:
                    file_list.append(some_file)
    return file_list
    
def folder_counter(path):
    '''функция обнаружения каталогов возвращает список каталогов'''
    folder_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            some_folder = str(os.path.join(dirpath, dirname))
            if 'RECYCLE' not in some_folder:
                folder_list.append(some_folder)
    return folder_list

def test(path, expansion):
    # списки вариантов ответов
    varyes = ['1', 'y', 'yes', 'д', 'да', '1,да,yes']
    varno = ['0', 'n', 'no', 'н', 'нет', '0,no,нет']
    # пуск функции обнаружения каталогов
    if expansion == '-':
        print('Отображать? 1,да,yes/0,no,нет')
        select = input('Выбирайте: ').lower()
        if select in varyes:
            folder_list = folder_counter(path)
            for dirname in folder_list:
                print(dirname)
            folder_count = len(folder_list)
            info = f'По указанному пути: {path}\nобнаружено {folder_count} Каталогов.'
            msg = f'{info}'
            print(msg)
        elif select in varno:
            folder_list = folder_counter(path)
            folder_count = len(folder_list)
            info = f'По указанному пути: {path}\nобнаружено {folder_count} Каталогов.'
            msg = f'{info}'
            print(msg)
    # пуск функции обнаружения файлов
    else:
        print('Отображать? 1,да,yes/0,no,нет')
        select = input('Выбирайте: ')
        if select in varyes:
            file_list = file_counter(path, expansion)
            for file in file_list:
                print(file)
            count_fises = len(file_list)
            info = f'По указанному пути: {path}\nобнаружено  {count_fises} : {expansion} Файлов'
            msg = f'{info}'
            print(msg)
        elif select in varno:
            file_list = file_counter(path, expansion)
            count_fises = len(file_list)
            info = f'По указанному пути: {path}\nобнаружено {count_fises} : {expansion} Файлов'
            msg = f'{info}'
            print(msg)

if __name__ == '__main__':
    test(path, expansion)
    input('ok')
    