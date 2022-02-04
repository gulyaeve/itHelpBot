from json import loads, dumps
from logging import log, INFO


def read(filename):
    try:

        with open('json/' + filename + '.json', 'r', encoding='utf-8') as file:
            return loads(file.read())

    except FileNotFoundError:
        log(msg='[error] Файл ' + filename + ' не найден (код 5)', level=INFO)
        return None


def write(filename, value):
    try:

        with open('json/' + filename + '.json', 'w', encoding='utf-8') as file:
            file.write(dumps(value))

    except KeyError:
        log(msg='[error] Ключ не найден (код 4)', level=INFO)
        return None

    else:
        return 0


def add_junk(value):
    try:
        file = list(read('junk'))
        file.append(str(value))
        write('junk', file)

    except FileNotFoundError:
        log(msg='[error] Ошибка, файл не найден', level=INFO)


def new_user(user_id):
    try:
        users = read('users')
        users[user_id] = {
            "email": '0',
            "id4me": '0'
        }
        write('users', users)

    except KeyError:
        log(msg='[error] Ключ не найден (код 3)', level=INFO)
        return None

    else:
        return 0


def update_user(user_id, field, value):
    try:
        users = read('users')
        users[user_id][field] = value
        write('users', users)

    except KeyError:
        log(msg=f'[error] Ключ не найден (код 2) {str(field)}', level=INFO)
        return None

    else:
        return 0
