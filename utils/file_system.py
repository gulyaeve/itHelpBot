from json import loads, dumps

def read(filename):
    try:

        with open('json/'+filename+'.json', 'r', encoding='utf-8') as file:
            return loads(file.read())

    except FileNotFoundError:
        log('log', '[error] Файл ' + filename + ' не найден (код 5)')
        return None


def write(filename, value):
    try:

        with open('json/'+filename+'.json', 'w', encoding='utf-8') as file:
            file.write(dumps(value))

    except KeyError:
        log('log', '[error] Ключ не найден (код 4)')
        return None

    else:
        return 0


def add_junk(value):
    try:
        file = list(read('junk'))
        file.append(str(value))
        write('junk', file)

    except FileNotFoundError:
        log('log', '[error] Ошибка, файл не найден')


def new_user(user_id):
    try:
        users = read('users')
        users[user_id] = {
            "register": '0'
            }
        write('users', users)

    except KeyError:
        log('log', '[error] Ключ не найден (код 3)')
        return None

    else:
        return 0

def new_interactivePanel(panel_id):
    try:
        panels = read('interactivePanelsDB')
        panels[panel_id] = {
          "1": "0",
          "2": "0",
          "3": "0",
          "4": "0",
          "5": "0",
          "6": "0",
          "7": "0",
          "8": "0",
          "9": "0",
          "10": "0",
          "11": "0",
          "12": "0",
          "13": "0",
          "14": "0",
          "15": "0",
          "16": "0",
          "17": "0",
          "18": "0",
          "19": "0",
          "20": "0",
          "21": "0",
          "22": "0",
          "23": "0",
          "24": "0",
          "25": "0",
          "26": "0",
          "27": "0",
          "28": "0",
          "29": "0",
          "30": "0",
          "31": "0",
          "32": "0",
          "33": "0",
          "34": "0",
          "35": "0",
          "36": "0",
          "37": "0",
          "38": "0",
          "39": "0",
          "40": "0",
          "41": "0",
          "42": "0",
          "43": "0",
          "44": "0",
          "45": "0",
          "46": "0",
          "47": "0",
          "48": "0",
          "49": "0",
          "50": "0",
          "51": "0",
          "52": "0",
          "53": "0",
          "54": "0",
          "55": "0",
          "56": "0",
          "57": "0",
          "58": "0",
          "59": "0",
          "60": "0",
          "61": "0",
          "62": "0",
          "63": "0",
          "64": "0",
          "65": "0",
          "66": "0",
          "67": "0"
          }

        write('interactivePanelsDB', panels)

    except KeyError:
        log('log', '[error] Ключ не найден (код 3)')
        return None

    else:
        return 0

def update_panel(panel_id, field, value):
    try:
        panels = read('interactivePanelsDB')
        panels[panel_id][field] = value
        write('interactivePanelsDB', panels)

    except KeyError:
        log('log', '[error] Ключ не найден (код 2)'+str(field))
        return None

    else:
        return 0

def update_user(user_id, field, value):
    try:
        users = read('users')
        users[user_id][field] = value
        write('users', users)

    except KeyError:
        log('log', '[error] Ключ не найден (код 2)'+str(field))
        return None

    else:
        return 0


def log(filename, message):
    try:
        with open('logs/' + filename + '.txt', 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    except FileNotFoundError:
        print('Файл не найден (код 1)')
        return None

    else:
        return 0
