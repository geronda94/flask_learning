import datetime

from flask import Flask,request, session, url_for, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e6af7e7bf42518fbf4f89426af642da357b33dcf'
app.permanent_session_lifetime = datetime.timedelta(days=10)



@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1 #обновление данных сессии
    else:
        session['visits'] = 1 #Запись данныйх сессии

    return f"<h1>Main Page</h1><p>Число просмотров: {session['visits']}"


data = [1,2,3,4]
@app.route("/session")
def session_data():
    session.permanent = True #Устанавливаем срок жизни сессии(по умолчанию 31 день)
    # app.permanent_session_lifetime этим параметром выше устанавливаем нужное время жизни сессии

    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True #Без этой строчки состояние сессии будет всегда неизменным
    return f"<p>session['data'] = {session['data']}"










if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



