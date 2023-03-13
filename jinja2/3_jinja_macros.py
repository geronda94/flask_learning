from jinja2 import Template


cars = [
    {'model':'Audi', 'price':20000},
    {'model':'BMW', 'price':30000},
    {'model':'Mercedes', 'price':40000},
    {'model':'Tesla', 'price':30000},
]

persons = [
    {'name':'Bob', 'old':18, 'weight':'90'},
    {'name':'Marc', 'old':50, 'weight':'74'},
    {'name':'Viks', 'old':18, 'weight':'70'},
    {'name':'Jhon', 'old':36, 'weight':'94'}
]



price = [200,300,100]
def summ2(): #Выводит сумму всех значений из списка
    tpl = "Сумарная цена товара {{ css | sum}}"
    tm = Template(tpl)
    return tm.render(cs=price)


def maxx(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ (css | max(attribute='price')).model }}"
    tm = Template(tpl)
    return tm.render(cs=cars)

def rand(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ (css | random).model }}"
    tm = Template(tpl)
    return tm.render(cs=cars)


def repl(): #Выводит сумму всех значений с ключем price
    tpl = "Сумарная цена автомобилей {{ css | replace('e', 'E')}}"
    tm = Template(tpl)
    return tm.render(cs=cars)


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

    html = '''{% macro input(name, value=" ", type="text", size="40") -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value | e }}" size="{{ size }}">
    {% endmacro %}
    <p>{{ input("username") }}</p>
    <p>{{ input("email") }}</p>
    <p>{{ input("password") }}</p>
    '''

    tm = Template(html)
    msg = tm.render()
    return msg


def macro_users():
    html = '''{% macro list_users(list_of_user) -%}
        <ul>
        {% for u in list_of_user -%}
            <li> {{ u.name }}</li>
        {% endfor -%}
        </ul>
        {%- endmacro %}     
        {{ list_users(users) }}'''


    html2 = '''{% macro list_users(list_of_user) -%}
            <ul>
            {% for u in list_of_user -%}
                <li> {{ u.name }} {{ caller(u) }}</li>
            {% endfor -%}
            </ul>
            {%- endmacro %}     
            
            {% call(user) list_users(users) -%}
                <ul>
                    <li>age: {{ user.old }} </li>
                    <li>weight: {{ user.weight }} </li>
                </ul>
            {% endcall -%}'''



    tm = Template(html2)
    return tm.render(users=persons)



print(macro_users())










