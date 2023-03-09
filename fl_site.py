from flask import Flask, render_template, request, g, flash, abort, make_response, redirect, url_for
import os
import sqlite3
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from forms import LoginForm


MAX_CONTENT_LENGTH = 1024*1024
DATABASE = 'flsite.db'
DEBUG = True
SECRET_KEY = 'dfsajhfaskjhbcah2138eduihknd3u8923uhfwe'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Вы еще не вошли в свой аккаунт. <p> пожалуйста авторизируйтесь или зарегистрируйтесь <p>' \
                              'если у вас еще нет аккаунта'
login_manager.login_message_category = 'success'

@login_manager.user_loader
def loader_user(user_id):
    print('load_user')
    return UserLogin().fromDB(user_id, dbase)



def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None

@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route('/')
def index():
    content = render_template('index2.html', menu=dbase.getMenu(), posts=dbase.getPostAnonce())
    res = make_response(content, 220)
    res.headers['Content-Type'] = 'text/html'
    res.headers['Server'] = 'flasksite'
    return res
#

# @app.route('/register', methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         if len(request.form['name']) > 4 and len(request.form['email']) >4\
#             and len(request.form['psw']) >4 and request.form['psw'] == request.form['psw2']:
#             hash = generate_password_hash(request.form['psw'])
#             res = dbase.addUser(request.form['name'],request.form['email'], hash)
#             if res:
#                 flash("Вы успешно зарегестрированны", "success")
#             else:
#                 flash("Ошибка регистрации", "error")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()
    return render_template('login.html', menu=dbase.getMenu(), title='Авторизация', form=form)
    # if request.method == 'POST':
    #     user=dbase.getUserByEmail(request.form['email'])
    #     if user and check_password_hash(user['password'], request.form['psw']):
    #         userlogin = UserLogin().create(user)
    #         rm = False if request.form.get('remainme') else True
    #         login_user(userlogin, remember=rm)
    #         return redirect(request.args.get("next") or url_for('profile'))
    #
    #     flash('Неверная пара ЛОГИН - ПАРОЛЬ', 'error')
    #
    # return render_template('login.html', menu=dbase.getMenu(), title='Авторизация')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', menu=dbase.getMenu(), title='Профиль')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
                and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash('Вы успешно зарегистрированны', 'success')
                return redirect(url_for('login'))
            else:
                flash('Ошибка при регистрации', 'error')
    return render_template('register.html', menu=dbase.getMenu(), title='Регистрация')


@app.route('/userava')
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'

    return h


@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verifyExt(file.filename):
            try:
                img = file.read()
                res = dbase.updateUserAvatar(img, current_user.get_id())
                if not res:
                    flash('Ошибка обновления аватара', 'error')
                    return redirect(url_for('profile'))
                flash('Аватар успешно обновлен', 'success')

            except FileNotFoundError as ex:
                flash('Ошибка чтения файла', 'error')

    return redirect(url_for('profile'))


@app.route('/flask')
def flask():
    return "<h1>Main page</h1>", 200, {'Content-Type': 'text/html'}


@app.route('/transfer')
def transfer():
    return redirect(url_for('flask'), 302)


@app.errorhandler(404)
def error(error):
    return ("Страница не найдена", 404)


# @app.route('/')
# def index():
#     img = None
#     with app.open_resource(app.root_path+"/static/images_html/img.jpg", mode='rb') as f:
#         img = f.read()
#
#     if img is None:
#         return "None Image"
#
#     res = make_response(img)
#     res.headers['Content-Type'] = 'image/jpg'
#     return res


@app.route('/add_post', methods=['POST', 'GET'])
def addPost():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья успешно добавлена', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Добавление статьи')


@app.route('/post/<alias>')
@login_required
def showPost(alias):
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


# def before_first_request():
#     print('before first request')
#
# def before_request():
#     print('before request called')
#
#
# app.before_first_request(before_request)
# app.before_first_request(before_first_request)
#
#
# @app.after_request
# def after_request(response):
#     print('after request called')
#     return response
#
# @app.teardown_request
# def teardown_request(response):
#     print('teardown request called')
#     return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
