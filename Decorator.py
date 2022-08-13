import datetime
import os


def decorator(path_file):
    def _decorator(old_func):
        def new_func(*args, **kwargs):
            if not os.path.isdir(os.path.dirname(path_file)):
                print(f'Путь {path_file} не существует. Файл log.txt будет создан в текущей директории')
                file_path = 'log.txt'
            else:
                file_path = path_file
            with open(file_path, 'a', encoding="UTF-8") as file_obj:
                file_obj.write('*' * 50 + '\n')
                file_obj.write(f'Время вызова функции: {datetime.datetime.now()}\n')
                file_obj.write(f'Имя функции {old_func.__name__}\n')
                file_obj.write(f'Аргументы {args} - {kwargs}\n')
                result = old_func(*args, **kwargs)
                file_obj.write(f'Результат: {result}\n')
            return result

        return new_func

    return _decorator
