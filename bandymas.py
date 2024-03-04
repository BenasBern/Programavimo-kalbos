from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def login():
    return render_template('index.html', title='Home', username='Studentas_1', user_is_logged_in=True, shopping_list=['preke1', 'preke2', 'preke3'])

if __name__ == '__main__':
    app.run(debug=True)
