import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyclip


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
        email = data[website]["email"]
        password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(
            title="WOOOOO!", message="Hey man you havnt made any passwords yet.")
    except KeyError:
        messagebox.showinfo(
            title="WOOOOO!", message="Hey man you dont have any login info for that website yet.")
    else:
        messagebox.showinfo(
            title="Amazon Login Info", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(
            title="WOOOOO!", message="Hey man you need to enter some info")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white",
                      fg="black", font=("Arial", 15))
website_label.grid(column=0, row=1)

website_entry = Entry(width=21, bg="white", fg="black")
website_entry.grid(column=1, row=1)
website_entry.focus

search_button = Button(
    width=10, text="Search Password", highlightbackground="white", command=search_password)
search_button.grid(column=2, row=1)


email_label = Label(text="Email/Username:", bg="white",
                    fg="black", font=("Arial", 15))
email_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg="white", fg="black")
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "YourEmailHere@gmail.com")


password_label = Label(text="Password:", bg="white",
                       fg="black", font=("Arial", 15))
password_label.grid(column=0, row=3)

password_entry = Entry(width=21, bg="white", fg="black")
password_entry.grid(column=1, row=3)

gen_pass_button = Button(
    width=10, text="Generate Password", highlightbackground="white", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(
    width=30, text="Add", highlightbackground="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
