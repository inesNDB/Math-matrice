#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return "Hello, World!"

#if __name__ == '__main__':
#    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return f"You entered: {user_input}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)