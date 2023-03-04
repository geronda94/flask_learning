from flask import Flask, render_template, request
import os
import sqlite3
import psycopg2

DATABASE = 'tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'dfsajhfaskjhbcah2138eduihknd3u8923uhfwe'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
