from jinja2 import Template


cars = [
    {'model':'Audi', 'price':20000},
    {'model':'BMW', 'price':30000},
    {'model':'Mercedes', 'price':40000},
    {'model':'Tesla', 'price':30000},
]



price = [200,300,100]
def summ2(): #Выводит сумму всех значений из списка
    tpl = "Сумарная цена товара {{ cs | sum}}"
    tm = Template(tpl)
    return tm.render(cs=price)


def maxx(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
    tm = Template(tpl)
    return tm.render(cs=cars)

def rand(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ (cs | random).model }}"
    tm = Template(tpl)
    return tm.render(cs=cars)


def repl(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ cs | replace('e', 'E')}}"
    tm = Template(tpl)
    return tm.render(cs=cars)



persons = [
    {'name':'Bob', 'old':18, 'weight':'90'},
    {'name':'Marc', 'old':50, 'weight':'74'},
    {'name':'Viks', 'old':18, 'weight':'70'},
    {'name':'Jhon', 'old':36, 'weight':'94'}
]

def persons_upper():
    tpl = '''
    {%  for u in users -%}
    {%  filter upper %}{{ u.name }} {% endfilter %}
    {%  endfor -%}
    '''

    tm = Template(tpl)
    tres = tm.render(users=persons)
    return tres


def dry():
    html = '''
    {% macro input(name, value=" ", type="text", size="20") -%}
        <input type="{{ type }}" name="{{ name }}" value="{{ value | e }}" size="{{ size }}">
    {% endmacro %}
    <p>{{ input("username") }}</p>
    <p>{{ input("email") }}</p>
    <p>{{ input("password") }}</p>
    '''

    tm = Template(html)
    msg = tm.render()
    return msg


print(dry())










