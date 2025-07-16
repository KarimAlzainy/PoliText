from tkinter import *
import clipboard

importingOfclipboardcopy = "AIzaSyAhE1VWG_Kp7FvsEH6t7bWngyV5CqVWQ8A"

# def langChoice():#-----------------------Language Window
#     langwindow = Tk()
#     langwindow.geometry("400x150")
#     langwindow.title("Choose Your Language")
#     langwindow.resizable(False,False)
    
#     title = Label(langwindow, text="""Choose your language
# اختر لغتك""",
#                   font=("Arial",23), fg="black")
#     title.pack(pady=10)
#     def engFun():#------------------If english Button function
#         with open("lang.txt",'w') as savedlang:
#             savedlang.write("english") #Will write if english language
#             langwindow.destroy()
#             EnEmailWindow()
#print("line3")

# def langChoice():#-----------------------Language Window
#     langwindow = Tk()
#     langwindow.geometry("400x150")
#     langwindow.title("Choose Your Language")
#     langwindow.resizable(False,False)
    
#     title = Label(langwindow, text="""Choose your language
# اختر لغتك""",
#                   font=("Arial",23), fg="black")
#     title.pack(pady=10)
#     def engFun():#------------------If english Button function
#         with open("lang.txt",'w') as savedlang:
#             savedlang.write("english") #Will write if english language
#             langwindow.destroy()
#             EnEmailWindow()
            
#     EngBtn = Button(langwindow,
#                        text="English",
#                        bg="gray",
#                        font=("Roboto Light", 15),
#                        command=lambda: engFun())
#     def arbFun():
#         with open("lang.txt",'w') as savedlang:
#             savedlang.write("arabic")
#             langwindow.destroy()
#             ArbEmailWindow()
                
#     ArbBtn = Button(langwindow,
#                            text="عربي",
#                            bg="gray",
#                            font=("Roboto Light", 15),
#                          command=lambda: arbFun())
#     EngBtn.pack()
#     ArbBtn.pack()
#     langwindow.mainloop()

# lang = open("lang.txt","r").read()
# if lang != "english" and lang != "arabic":
#     langChoice()
lang = "english"

if lang == "english":
    window = Tk()
    window.geometry("500x300")
    window.resizable(False,False)
    window.title("Politing Tool")
    window.iconbitmap("resources/search.ico")
    #Credits to Riswan Ratta for the icon
    canvas = Canvas(window, width=500, height=300)
    canvas.place(x=-1,y=-1)
    bgFile = PhotoImage(file="resources\engBg.png")
    bg = canvas.create_image((0,0), image=bgFile, anchor="nw")
    
    entry = Entry(window, font=("Calibri","18"), background="#707EFF",
                  borderwidth=0, border=0, width=31)
    entry.place(x=58,y=87)
    
    resultLabel = canvas.create_text((19,206),
#                                     text=response.text,
                                     font=("Calibri", "22"), anchor="nw",
                                     width=500)
    
    def happytoneFun():
        try:
            import google.generativeai as genai
            genai.configure(api_key=importingOfclipboardcopy)
            model = genai.GenerativeModel("gemini-1.5-flash")
            global response
            sentence = entry.get()
            response = model.generate_content(f"""
'{sentence}', try to make this sound as polite as possible, direct answer only, only one answer, just give me the same sentence with a polite tone.""")
            
            canvas.itemconfig(resultLabel, text=response.text)
        except:
            canvas.itemconfig(resultLabel, text="No Internet!")

    def copyText():
        try:
            text = response.text
            clipboard.copy(text)
        except:
            canvas.itemconfig(resultLabel, text="You haven't typed anything yet.")
    #---------------------
    happytonePhoto = PhotoImage(file="resources\engHappyBtn.png")
    happytoneBtn = Button(window, text="Change tone", font=("Calibrii",18),
                          image=happytonePhoto, border=-1, borderwidth=-1,
                          background="#7A8CFF", activebackground="#7A8CFF",
                          command=lambda: happytoneFun())
    happytoneBtn.place(x=162,y=159)
    
    copyBtnPhoto = PhotoImage(file="resources\copybtn.png")
    copybtn = Button(window, image=copyBtnPhoto, command=lambda:copyText())
    copybtn.place(x=458,y=137)
    
    window.mainloop()