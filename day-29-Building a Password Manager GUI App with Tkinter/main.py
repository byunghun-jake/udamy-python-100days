import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    # 입력창 초기화
    password_entry.delete(0, tk.END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    # 입력값 확인
    is_valid = website and email and password
    
    if not is_valid:
        messagebox.showwarning(title="이런...", message="필요한 정보를 모두 입력하세요.")
    else:
        ask_message = f"입력한 정보를 확인합니다: \n이메일: {email} \n비밀번호: {password} \n비밀번호를 저장할까요?"
        is_ok = messagebox.askokcancel(title=website, message=ask_message)

        if is_ok:
            data = f"{website} | {email} | {password}\n"
            with open("./data.txt", mode="a", encoding="utf-8") as f:
                f.write(data)
        else:
            messagebox.showinfo(title="저장 실패", message="입력한 내용을 초기화합니다")

        # entry 초기화
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(bg="white", width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)
# canvas.pack()

# Website
website_label = tk.Label(text="서비스 이름: ", bg="white")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=35, bg="lightyellow")
website_entry.grid(row=1, column=1, columnspan=2)

website_entry.focus()
website_entry.insert(0, "Tingle")

# Email/Username
email_label = tk.Label(text="이메일/아이디: ", bg="white")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35, bg="lightyellow")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "figma@kakao.com")

# Password
password_label = tk.Label(text="비밀번호: ", bg="white")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=22, bg="lightyellow")
password_entry.grid(row=3, column=1)
password_entry.insert(0, "")

password_button = tk.Button(text="비밀번호 생성", bg="white", command=generate_password)
password_button.grid(row=3, column=2)


# Add
add_button = tk.Button(text="추가", width=34, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)
















window.mainloop()