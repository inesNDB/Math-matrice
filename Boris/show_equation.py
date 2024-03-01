from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_integral_question():
    # Generate random coefficients
    a = random.randint(-5, 5)
    b = random.randint(-5, 5)

    # Generate LaTeX code for the question
    question = f"$\int ({a}x^2 + {b}x) \,dx$"

    # Generate LaTeX code for virtual keyboard
    keyboard = """
    \\begin{array}{cccccc}
    \\int & \\frac{d}{dx} & \\sum & \\prod & \\lim & \\infty \\\\
    \\end{array}
    """

    return question, keyboard

@app.route('/')
def display_integral_question():
    # Generate integral question and virtual keyboard
    question, keyboard = generate_integral_question()

    return render_template('index.html', question=question, keyboard=keyboard)

if __name__ == '__main__':
    app.run(debug=True)
