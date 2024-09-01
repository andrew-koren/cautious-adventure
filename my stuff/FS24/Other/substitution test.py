import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def render_latex(equation):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, r"$%s$" % equation, fontsize=20, ha='center', va='center')
    ax.axis('off')
    return fig

def update_canvas():
    equation = entry.get()
    fig = render_latex(equation)
    canvas.figure = fig
    canvas.draw()

# Initialize the main window
root = tk.Tk()
root.title("LaTeX Renderer")

# Create an input box
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to render the equation
button = ttk.Button(root, text="Render", command=update_canvas)
button.grid(row=0, column=1, padx=10, pady=10)

# Create a canvas to display the rendered LaTeX
fig = render_latex(r"\frac{d}{dt} \hat \phi = - r \dot \phi \hat r")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

# Run the application
root.mainloop()
