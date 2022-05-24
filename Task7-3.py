import os

def write_sorted_file():
    BASE_PATH = os.getcwd()
    DIR = 'files'

    if DIR not in os.listdir(os.path.join(BASE_PATH)):
        print(f'В каталоге {BASE_PATH} отсутствует каталог {DIR} с файлами для сотрировки')
        return

    files = {}
    for file_name in os.listdir(os.path.join(BASE_PATH, DIR)):
        with open(os.path.join(BASE_PATH, DIR, file_name),'r', encoding='UTF-8') as file_obj:
            lines_list = ()
            for line in file_obj:
                lines_list += (line.strip(), )
            files[lines_list] = file_name

    key_list = list(files.keys())
    for i in range(len(key_list) - 1):
        for j in range(len(key_list) - i - 1):
            if key_list[j] < key_list[j + 1]:
                key_list[j], key_list[j + 1] = key_list[j + 1], key_list[j]

    with open(os.path.join(BASE_PATH, DIR, 'result.txt'), 'w', encoding='UTF-8') as file_obj:
        for key in key_list:
            file_obj.write(files[key] + '\n')
            file_obj.write(str(len(key)) + '\n')
            for line in key:
                file_obj.write(line + '\n')

write_sorted_file()