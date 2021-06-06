from tkinter import *
from tkinter import messagebox as mb
question=[
    "what is capital of india?",
    "Who is the Father of our Nation?",
    "Who was the first President of India?",
    "Which is the most sensitive organ in our body?",
    "Which is the longest river on the earth?",
    "Smallest state of India is?",
    "Which plant grows in desert?",
    "National Tree of India is?",
    "We get solar energy from?",
    "How many players are there in a cricket team?",
]
answer=[["1.Delhi","2.rajasthan","3.gujarat","4.maharastra"],
["1. Mahatma Gandhi","2. Dr.Rajendra Prasad","3. Dr. B. R.Ambedkar ","4. Rabindra Nath Tagore"],
["1. Dr.Rajendra Prasad","2. Charles Babbage ","3. Dr. B. R.Ambedkar","4. Rabindra Nath Tagore"],
["1.Skin ","2. Eyes","3. Nose","4. hand"],
["1. Nabda ","2. Nile","3. Ganga ","4. Sarswati"],
["1. Rajasthan","2. Gujarat","3. Goa","4. Bombay"],
["1. Cactus","2. Rose ","3. jamun ","4. Lemon"],
["1. Banyan Tree","2. Neam Tree","3. Babul Tree","4. Ashoka tree"],
["1. Sun","2. Moon","3. Star","4. Earth"],
["1. 10","2. 9","3. 11","4. 8"],]
exacans=['1','1','1','1','2','3','1','1','1','3']
def finalans(anssheet):
    marks=0
    for i in range(0,len(question)):
        if str(anssheet[i])==exacans[i]:
            marks=marks+1                    
    root1=Tk()
    totalmarks=Label(root1,text="total marks=",font="comic 19 bold")  
    total=Label(root1,text=marks,font="comic 19 bold") 
    totalmarks.pack()
    total.pack()
    root1.mainloop()
global i
i=0
user_ans_sheet=[]
def increase():
    if radiovar.get()==-1:
        mb.showinfo("error message","please choose the option")
    else:
        user_ans_sheet.append(radiovar.get())
        print(user_ans_sheet)
        lblquestions.destroy()
        Next.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        global i
        i=i+1
        if i<len(question):
            startquiz()
        else:
            finalans(user_ans_sheet)
            quit()
def startquiz():
    global lblquestions
    lblquestions=Label(
        text=question[i],font="comic 19 bold",
    )
    lblquestions.pack()
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    global r1
    r1=Radiobutton(root,text=answer[i][0],variable=radiovar,value=1)
    r1.pack()
    global r2
    r2=Radiobutton(root,text=answer[i][1],variable=radiovar,value=2)
    r2.pack()
    global r3
    r3=Radiobutton(root,text=answer[i][2],variable=radiovar,value=3)
    r3.pack()
    global r4
    r4=Radiobutton(root,text=answer[i][3],variable=radiovar,value=4)
    r4.pack()
    global Next
    Next=Button(root,text="Next",command=increase)
    Next.pack()

def work():
    labeltext.destroy()
    Start.destroy()
    lblinstruction.destroy()
    lblrules.destroy()
    root.geometry("500x500")
    labeltext1=Label(root,text="WELCOME TO QUIZ ",font="comic 33 bold ",bg="BLUE")
    labeltext1.pack()
    startquiz()

root = Tk()
root.maxsize(500,500)
# img=PhotoImage(file="kinl.png")
# label=Label(
# root,
# image=img,
# )
# label.pack(side=TOP)
labeltext=Label(root,text="QUIZ STAR",font="comic 33 bold ",bg="BLUE")
labeltext.pack(pady=(20,50))
Start=Button(root,text="Start",font="comic 19 bold ",bg="Yellow",command=work)
Start.pack(pady=(0,50))
lblinstruction=Label(
    root,
    text="Read The rules and \nClick on Start quiz when u r ready\nWe hope you enjoy the quiz",
)
lblrules=Label(
    root,
    text="This quiz contain 10 question\nsolve all the questions\n you will get 20 sec to select an option\n you have compulsory to select an option",
    width=100,
    fg="White",
    bg="Black",
)
lblrules.pack(side="bottom")
lblinstruction.pack()
root.mainloop()