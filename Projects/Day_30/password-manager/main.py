from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

default_user = "cedric.lutonda@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list.extend([random.choice(symbols) for char in range(nr_symbols)])

    password_list.extend([random.choice(numbers) for char in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global default_user
    #Gets entries
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oooops", message="Please don't leave any empty field.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            #Clear entries
            website_entry.delete(0, END)
            website_entry.focus()
            user_entry.delete(0, END)
            user_entry.insert(0, default_user)
            password_entry.delete(0, END)
            messagebox.showinfo(title=website, message="Password saved.")
# ---------------------------- FIND PASSWORD ------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
        try:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        except KeyError:
            messagebox.showwarning(title="Error", message=f"No Details for {website} exist.")      
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
#User label
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
#Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Website entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
#User entry
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, default_user)
#Password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Generate Password button 
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
#Add button 
add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)
#Search button
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

window.mainloop()