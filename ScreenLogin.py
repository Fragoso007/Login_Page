
import customtkinter
def click():
    show ='logged sucessuful'
    text_down ['text'] = show

from customtkinter import *
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

window = CTk()
window.geometry('450x400')
window.title('Login')

text = CTkLabel(window, text='Make your login and follow me in my programming journey')
text.pack(padx=10, pady=10)
git = CTkLabel(window, text='Antonio Fragoso/GitHub')
git.pack(padx=10, pady=10)
email = CTkEntry(window, placeholder_text='Your email')
email.pack(padx=2, pady=1)
password = CTkEntry(window, placeholder_text='Your password', show= '*')
password.pack(padx=10, pady=10)
checkbox = CTkCheckBox(window, text='remember password')
checkbox.pack(padx=10, pady=10)

button = CTkButton(window, text='Login', command=click)
button.pack(padx = 10, pady = 10)
text_down = CTkLabel(window, text='')
text_down.pack(padx=10, pady=10)

window.mainloop()