from flask import Blueprint, request, redirect, url_for, flash, render_template, session

admin = Blueprint('admnin', __name__, template_folder='templates', static_folder='static')

menu=[
    {'url':'index', 'title':'Панель'},
    {'url':'logout', 'title':'Выход'}
]



@admin.route('/')
def index():
    if not isLogged():
        return redirect(url_for('login_admin'))

    return render_template('admin/index.html', menu=menu, title='Админ панель')

def login_admin():
    session['admin_logged'] = 1

def isLogged():
    return True if session.get('admin_logged') else False

def logout_admin():
    session.pop('admin_logged', None)



@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin' and request.form['psw'] == '12345':
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash( 'Неверный логин-пароль', 'error')

    return render_template('admin/login.html', title='Admin-panel')

@admin.route('/logout', methods=["GET", "POST"])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))

    logout_admin()

    return redirect(url_for('.login'))





















