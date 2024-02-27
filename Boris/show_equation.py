import os
import random

def generate_equation():
    # Generate random coefficients
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    # Generate LaTeX code for the equation
    equation = f"y = {a}x^2 + {b}x + {c}"

    # Write LaTeX code to a file
    with open("equation.tex", "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{amsmath}\n")
        f.write("\\begin{document}\n")
        f.write("\\section*{Random Mathematical Equation}\n")
        f.write(f"Here is a randomly generated mathematical equation:\n")
        f.write(f"\\[ {equation} \\]\n")
        f.write("\\end{document}\n")

    # Compile LaTeX to PDF
    os.system("pdflatex equation.tex")

    # Open the PDF file
    os.system("start equation.pdf")

if __name__ == "__main__":
    generate_equation()
