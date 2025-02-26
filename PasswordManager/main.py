from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_passw():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_passw():
    print(webs_entr.get())
    print(passw_entr.get())
    print(user_entr.get())
    if webs_entr.get() and passw_entr.get() and user_entr.get():
        is_ok = messagebox.askokcancel(title=webs_entr.get(), message=f"Are these details correct: \n"
                                                                      f" {webs_entr.get()} | {user_entr.get()} | {passw_entr.get()}\n")
        if is_ok:
            with open("data.txt", mode="a") as save_file:
                save_file.write(f"{webs_entr.get()} | {user_entr.get()} | {passw_entr.get()}\n")
                webs_entr.delete(0, END)
                passw_entr.delete(0, END)
    else:
        messagebox.showwarning(title= "error",message="Not all required fields were filled\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
window.title("PassWord Manager")
canvas = Canvas(width=200, height=200, highlightthickness= 0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100 ,image = lock_img)
webs_text = Label(text= "Website")
webs_entr = Entry( width= 52)
webs_entr.focus()
user_text = Label(text= "Email/Username")
user_entr = Entry( width= 52)
passw_text = Label(text= "Password")
passw_entr = Entry( width= 33)
gen_pw_but = Button(text="Generate Password", command= gen_passw)
add_pw_but = Button(text="Add", command= save_passw ,  width= 44)
canvas.grid(column =1, row = 0)
webs_text.grid(column =0, row = 1)
webs_entr.grid(column =1, row = 1, columnspan = 2)
user_text.grid(column =0, row = 2)
user_entr.grid(column =1, row = 2, columnspan = 2)
user_entr.insert(0,"joostheicop@hotmail.com")
passw_text.grid(column =0, row = 3)
passw_entr.grid(column =1, row = 3, columnspan = 1)
gen_pw_but.grid(column =2, row = 3)
add_pw_but.grid(column =1, row = 4, columnspan = 2)








window.mainloop()