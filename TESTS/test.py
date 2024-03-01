from flask import Flask


app = Flask (__name__)

@app.route("/")
def home ():
    return "hello ! this our project <h1>maths<h1>"

if __name__ == "__main__":
    app.run()

    