from jinja2 import Template



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def pers():
    per = Person('Google', 22)
    # Экранируем все что помещается между {% raw %} {% endraw %}
    data = """{%raw%} Модуль Jinja определяет имя {{name}}{% endraw %}"""
    #data = """ Модуль Jinja определяет имя {{name}}"""


    tm = Template(data)
    return tm.render(name = per.name) #в качестве параметра name указываем значение для переменной {{ name }} в разметке




def lnk():
    link = '''Ссылка в HTML  <a href="#">Link</a>'''
    tm = Template("{{ link | e}}") #Механизм экранирования содержимого ссылки
    return tm.render(link=link)


cities = [
        {'id':1, 'city':'Moscow'},
        {'id':2, 'city':'Chisinau'},
        {'id':3, 'city':'Washington'},
        {'id':4, 'city':'Dubai'}
    ]

def block_for():
    link = '''
    <select name="cities"> 
    {% for c in cities -%}
    {% if c.id > 2 -%}
        <option value={{ c.id }}> {{ c.city }} </option>
    {% else -%}
        <option value=0> None </option>
    {% endif -%}
    {% endfor -%}
    </select>'''

    tm = Template(link)
    res = tm.render(cities=cities)
    return res


print(block_for())

