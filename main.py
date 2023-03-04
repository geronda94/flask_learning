from flask import Flask, render_template, request, url_for, flash



menu = [
    {'name':'Установка', 'url':'install-flask'},
    {'name':'Первое приложение', 'url':'first-app'},
    {'name':'Обратная связь', 'url':'contact'}
]

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'




@app.route('/index')
@app.route("/")
def index():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(ip_address)
    print(url_for('index')) #Выводит url если он соотвествует именно этому значнию
    return render_template('index.html', title="Главная страница", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)


#@app.route("/profile/<int:username>/<path>")
#@app.route("/profile/<path: username>")#а эта конструкция будет все одной ссылкой /profile/username/next
@app.route("/profile/<username>")#Такая конструкция будет считать другой сслыкой все что будет выглядеть так /profile/username/next
def profile(username):
    return f'Пользователь {username}'



@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) < 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')

    return render_template('contact.html', title='Обратная связь', menu=menu)




with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username='selfedu'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

