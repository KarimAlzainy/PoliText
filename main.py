from tkinter import *
import clipboard
import os

geminiAPI = "Please insert your gemini API"

window = Tk()
window.geometry("500x300")
window.resizable(False, False)
window.title("PoliText")
window.iconbitmap("resources/search.ico")

btnPhoto = PhotoImage(file="resources/btn.png")
bgFile = PhotoImage(file="resources/bg.png")
copyBtnPhoto = PhotoImage(file="resources/copybtn.png")

canvas = Canvas(window, width=500, height=300, highlightthickness=0)
canvas.place(x=-1, y=-1)

bg = canvas.create_image((0, 0), image=bgFile, anchor="nw")

# --------------------------- Entry Box ---------------------------
entry = Entry(window,
              font=("Calibri", 18),
              bg="#707EFF",
              fg="white",
              border=0,
              width=31,
              insertbackground="white")
entry.place(x=58, y=87)

# --------------------------- Result Label ---------------------------
resultLabel = canvas.create_text(
    19, 206,
    text="",
    font=("Calibri", 18),
    anchor="nw",
    fill="black",
    width=460
)
import google.generativeai as genai
genai.configure(api_key=geminiAPI)
model = genai.GenerativeModel("gemini-1.5-flash")
# --------------------------- Tone Function ---------------------------
def happytoneFun():
    sentence = entry.get().strip()
    if not sentence:
        canvas.itemconfig(resultLabel, text="Please type a sentence first.")
        return

    try:
        response = model.generate_content(
            f"'{sentence}', try to make this sound as polite as possible, direct answer only, only one answer, just give me the same sentence with a polite tone."
        )

        canvas.itemconfig(resultLabel, text=response.text)
        # Store for copying
        window.generated_response = response.text

    except Exception as e:
        canvas.itemconfig(resultLabel, text="No Internet Connection!")

# --------------------------- Copy Function ---------------------------
def copyText():
    text = getattr(window, 'generated_response', None)
    if not text:
        canvas.itemconfig(resultLabel, text="Nothing to copy yet.")
    else:
        clipboard.copy(text)
        canvas.itemconfig(resultLabel, text="Copied to clipboard ✅")

# --------------------------- Buttons ---------------------------
toneButton = Button(window,
                    image=btnPhoto,
                    command=happytoneFun,
                    border=0,
                    bg="#7A8CFF",
                    activebackground="#7A8CFF")
toneButton.place(x=162, y=159)

copyBtnPhoto = PhotoImage(file="resources/copybtn.png")
copybtn = Button(window,
                 image=copyBtnPhoto,
                 command=copyText,
                 border=0,
                 bg="#7A8CFF",
                 activebackground="#7A8CFF")
copybtn.place(x=458, y=137)

window.mainloop()
