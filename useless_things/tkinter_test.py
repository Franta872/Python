import tkinter as tk

window = tk.Tk()
window.geometry("600x300")
window.title("tkinter test (:")
window.config(background="blue")

label = tk.Label(window,
                text="Hello World!",
                font=("arial", 50,
                "underline"),
                fg="blue",
                bg="black",
                relief="raised",
                bd=15,
                padx=30,
                pady=50)
label.place(x=50, y=50)

window.mainloop()