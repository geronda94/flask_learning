from jinja2 import Template, Environment, FileSystemLoader

persons = [
    {'name':'Bob', 'old':18, 'weight':'90'},
    {'name':'Marc', 'old':50, 'weight':'74'},
    {'name':'Viks', 'old':18, 'weight':'70'},
    {'name':'Jhon', 'old':36, 'weight':'94'}
]


def html_loader():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    tm = env.get_template('main.html')
    return tm.render(users=persons)




print(html_loader())

















