from flask import Flask, request, make_response

app = Flask(__name__)


menu = [{'title':'Index', 'url':"/"},
        {'title':'Добавить статью', 'url':"/add_post"}]


@app.route('/')
def index():
    return '<h1> Main Page</h1>'



@app.route('/login')
def login():
    log =""
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Форма автоматизациии</h1><p>logged: {log}")
    res.set_cookie('logged', 'yes', 30*24*3600)
    return res


#Удаление куков
@app.route('/logout')
def logout():
    res = make_response('<p>Вы вышли из аккаунта</p>')
    res.set_cookie("logged", "", 0)
    return res




if __name__ =="__main__":
    app.run(debug=True)


