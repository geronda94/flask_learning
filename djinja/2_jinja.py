from jinja2 import Template



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



per = Person('Google', 22)

data = """{%raw%} Модуль Jinja определяет имя {{name}}{% endraw %}"""
#data = """ Модуль Jinja определяет имя {{name}}"""


tm = Template(data)
msg2 = tm.render(name = per.name)

print(msg2)






