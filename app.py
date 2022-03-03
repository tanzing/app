import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask('SDLAB')

class Data:
    def __init__(self, id, name, data_type):
        self.id = id
        self.name = name
        self.data_type = data_type

    id: int
    name: str
    data_type: str


def get_connection_for_db():
    connection = sqlite3.connect('posts.db')
    connection.row_factory = sqlite3.Row
    return connection

def fetch_data():
    connection = get_connection_for_db()
    temp = []
    for v in connection.execute('SELECT * FROM posts').fetchall(): 
        temp.append(Data(v['id'], v['user_name'], v['user_type']))
    connection.close()
    return temp 

def add_data(user_name: str, user_type: str):
    connection = get_connection_for_db()
    connection.execute('INSERT INTO posts (user_name, user_type) VALUES (?, ?)', (user_name, user_type))
    connection.commit()
    connection.close()

@app.route('/')
def data_view():
    temp = fetch_data()
    return render_template('view.html', data=temp)

@app.route('/edit', methods = ['GET', 'POST'])
def form_view():
    if request.method == 'GET':
        return render_template('edit.html')
    else:
        temp_data = request.form
        print(temp_data)
        add_data(temp_data['user_name'], temp_data['user_type'])
        return redirect(url_for('data_view'))