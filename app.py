from tkinter import *
from random import randint


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

window = Tk()


def generateNumber(min, max):
    return str(randint(min, max + 1))


textL = Label(window, text="Click to the button to generate a random number", font=(
    'Monospace', 20))
textL.place(x=WINDOW_WIDTH / 2 - 260, y=100)


def createLabel(txt):
    global textL
    if textL:
        textL.destroy()
    textL = Label(window, text=f'Number: {txt}', font=('Monospace', 20))
    textL.place(x=WINDOW_WIDTH / 2 - 70, y=100)


window.title('Random number generator!')
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+100+100")
generatingButton = Button(
    window, text="Generate number!", bg='#39a3aa', fg='white', font=('Helvetica', 20), command=lambda: createLabel(generateNumber(0, 100000)))
generatingButton.place(x=WINDOW_WIDTH / 2 - 110, y=250)
window.mainloop()
