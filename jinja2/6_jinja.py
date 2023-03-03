from jinja2 import Environment,FileSystemLoader

subs = ['Matematica', 'Fisica', 'Himia', 'Informatica']


def run_template():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    template = env.get_template('about.htm')
    return template.render(list_table=subs)


print(run_template())



