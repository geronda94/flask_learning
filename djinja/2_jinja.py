from jinja2 import Template



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



name = 'Goga'
per = Person('Google', 22)



tm = Template("Привет {{ p.name.upper() }}, Твой возраст {{ p.age }}")
msg =  tm.render(p=per)

print(msg)






