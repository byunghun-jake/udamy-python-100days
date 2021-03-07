import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = "✅"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    check_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2:
        count_down(work_sec)
    else:
        count_down(short_break_sec)

    # change timer_label
    if reps % 2:
        timer_label.config(text="Work", fg=GREEN)
    else:
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer

    min = count // 60
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    count_text = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=count_text)

    if count == 0:
        start_timer()
        # update check_label
        check_text = check * (((reps - 1) // 2))
        check_label.config(text=check_text)
        return

    timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

# # Call count_down
# count_down(5)

# Timer Label
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Button
start_button = tk.Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tk.Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check Label

check_label = tk.Label(text="", fg=GREEN, bg=YELLOW, pady=20)
check_label.grid(row=3, column=1)


















window.mainloop()


