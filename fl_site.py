from flask import Flask, render_template, request, g, flash, abort, make_response, redirect, url_for
import os
import sqlite3
from FDataBase import FDataBase

DATABASE = 'flsite.db'
DEBUG = True
SECRET_KEY = 'dfsajhfaskjhbcah2138eduihknd3u8923uhfwe'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))




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



@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    content = render_template('index2.html', menu=dbase.getMenu(), posts=dbase.getPostAnonce())
    res = make_response(content, 500)
    res.headers['Content-Type'] = 'text/html'
    res.headers['Server'] = 'flasksite'
    return res

@app.route('/flask')
def flask():
    return "<h1>Main page</h1>", 200, {'Content-Type':'text/html'}


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
    db = get_db()
    dbase = FDataBase(db)
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
def showPost(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)



@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()




def before_first_request():
    print('before first request')

def before_request():
    print('before request called')


app.before_first_request(before_request)
app.before_first_request(before_first_request)


@app.after_request
def after_request(response):
    print('after request called')
    return response

@app.teardown_request
def teardown_request(response):
    print('teardown request called')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
