import tkinter

# Tk 인스턴스 만들기
window = tkinter.Tk()

# 인스턴스 세팅
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def onClick():
    new_label_text = input_box.get()
    my_label.config(text=new_label_text)


button = tkinter.Button(text="Click Me", command=onClick)
button.pack()


# Entry
input_box = tkinter.Entry(width=10)
input_box.pack()


# 













window.mainloop()
































