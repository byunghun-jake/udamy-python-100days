import tkinter


# 텍스트 변환
def convert():
    # 입력한 마일 텍스트 받아오기
    try:
        mile_num = float(miles_input.get())
        km_num = mile_num * 1.609
    except ValueError:
        km_num = "숫자를 입력하세요."


    # result 값으로 출력
    km_result_label.config(text=km_num)


# window
window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=10, pady=20)
# window.minsize(width=500, height=200)

# Entry
miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1)

# Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

km_result_label = tkinter.Label(text="")
km_result_label.grid(row=1, column=1)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)


# Button
calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(row=2, column=1)
calculate_button.config()

























window.mainloop()