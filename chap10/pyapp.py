import tkinter as tk
from api import Api
api = Api()
window = tk.Tk()
window.title('Hello')
window.geometry("600x400") #윈도우 사이즈
message = tk.StringVar(value=api.get_message())
label = tk.Label(
    window,
    textvariable = message,
    font = ("Arial", 40)
)
label.pack(pady=10, expand=True)
window.mainloop()