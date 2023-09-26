import tkinter as tk


def eat_text():
    player_input.delete("1.0", 'end')


def countdown(t):
    if t > 0:
        window.after(1000, countdown, t-1)
    else:
        eat_text()


def start_timer(e):
    if e:
        countdown(5)


window = tk.Tk()
window.title('Typing speed test')
window.config(padx=100, pady=100, bg='#252B48')

title = tk.Label(text='BE WARY OF THE TEXT MONSTER', font=("Courier", 36, 'bold'), fg='#F7E987', bg='#252B48', pady=50)
sentence = tk.Label(text='he is really hungry', font=("Courier", 32), fg='#F7E987', bg='#252B48', pady=50)
player_input = tk.Text(window, width=100, height=6, padx=15, pady=15, bg='#252B48', font=("Courier", 15), fg='#F7E987')
player_input.bind('<KeyRelease>', start_timer)


title.grid(row=0, column=1)
sentence.grid(row=1, column=1)
player_input.grid(row=2, column=1)


window.mainloop()

