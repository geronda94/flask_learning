from jinja2 import Template, Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name':'Bob', 'old':18, 'weight':'90'},
    {'name':'Marc', 'old':50, 'weight':'74'},
    {'name':'Viks', 'old':18, 'weight':'70'},
    {'name':'Jhon', 'old':36, 'weight':'94'}
]

# Демонстрация работы загрузчика который возвращет html из файла
def file_loader(): #Функция возвращает данные из загрузчика локальных файлов
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('main.html')
    return tm.render(users=persons)


def func_loader(): #Демонстрация работы загрузчика который подгружает html через функцию
    def loadTPL(path): #создаем ссылку для вызова через загрузчик
        if path == "index":
            return '''Имя {{ u.name }}, возраст {{ u.old }}'''
        else:
            return '''Данные: {{ u }}'''



    file_loader = FunctionLoader(loadTPL) #Передаем ссылку на прописанную только что функцию
    env = Environment(loader=file_loader)

    tm = env.get_template('index')
    return tm.render(u=persons[0])


print(func_loader())

















