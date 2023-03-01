from flask import Flask, render_template



menu = ['Главная', 'О нас', 'Еще один пункк']




app = Flask(__name__)

@app.route('/index')
@app.route("/")
def index():
    return render_template('index.html', title="Главная страница", menu=menu)



@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)




if __name__ == '__main__':
    app.run(debug=True)

