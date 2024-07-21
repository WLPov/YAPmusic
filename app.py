import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/people')
def people():
    f = open('sql/people_list.json', 'r', encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    return render_template('people.html', list=data['list'])


@app.route('/people/<name>')
def people_name(name):
    f = open('sql/people.json', 'r', encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    img = data[name][0]
    age = data[name][1]
    text = data[name][2]
    return render_template('temp/people.html', name=name, img=img, age=age, text=text)
@app.route('/our-do')
def our_do():
    return render_template('我们的业务.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
