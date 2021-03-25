from tkinter import *
import math

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
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global checks
    global reps
    global timer
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    checks = ""
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checks
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            checks += "✓ "
            check_label["text"] = checks
        start()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Timer label
timer_label = Label(text="Timer")
timer_label.config(font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

#Buttons
#Start button 
button = Button(text="Start", command=start)
button.grid(column=0, row=2)
#Reset button 
button = Button(text="Reset", command=reset)
button.grid(column=2, row=2)

#Check mark label
check_label = Label()
check_label.config(font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)



window.mainloop()


