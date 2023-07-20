import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer
import playsound
import sqlite3
from PIL import ImageTk, Image
import itertools 
import pandas as pd
import numpy as np
import tkinter.messagebox
import random

amount = ['0', '10,000', '20,000', '40,000', '80,000', '1,60,000', '3,20,000', '6,25,000', '12,50,000', '25,00,000',
          '50,00,000', '1,00,00,000']
i1=0
double=0
question_count=0
q='Book1.csv'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
name,name1='',''
a=0
questionset=''
click,life,set1=0,list(),0
life=['lifeline50Button','audiencePoleButton','phoneLifelineButton']
questions,correct_answers,first_option,second_option,fourth_option,third_option=list(),list(),list(),list(),list(),list()
def que(q):
    def extraction(simple, medium, hard):
        global questions,correct_answers,first_option,second_option,fourth_option,third_option
        filename=pd.read_csv(simple)
        nlinesfile = len(filename)
        nlinesrandomsample = 4
        lines2skip = np.random.choice(np.arange(1,nlinesfile+1), (nlinesfile-nlinesrandomsample), replace=False)
        df1 = pd.read_csv(simple, skiprows=lines2skip)
        simple_final_q = df1.iloc[:, 1].to_list()
        option1_simple = df1.iloc[:, 2].to_list()
        option2_simple = df1.iloc[:, 3].to_list()
        option3_simple = df1.iloc[:, 4].to_list()
        option4_simple = df1.iloc[:, 5].to_list()
        ans_of_simples = df1.iloc[:, 6].to_list()
        # df.to_csv("simple_q.csv")


        filename=pd.read_csv(medium)
        nlinesfile = len(filename)
        nlinesrandomsample = 4
        lines2skip = np.random.choice(np.arange(1,nlinesfile+1), (nlinesfile-nlinesrandomsample), replace=False)
        df2 = pd.read_csv(medium, skiprows=lines2skip)
       
        medium_final_q = df2.iloc[:, 1].to_list()
        option1_medium = df2.iloc[:, 2].to_list()
        option2_medium = df2.iloc[:, 3].to_list()
        option3_medium = df2.iloc[:, 4].to_list()
        option4_medium = df2.iloc[:, 5].to_list()
        ans_of_medium = df2.iloc[:, 6].to_list()
        # df.to_csv("medium_q.csv")


        filename=pd.read_csv(hard)
        nlinesfile = len(filename)
        nlinesrandomsample = 4
        lines2skip = np.random.choice(np.arange(1,nlinesfile+1), (nlinesfile-nlinesrandomsample), replace=False)
        df3 = pd.read_csv(hard, skiprows=lines2skip)
        hard_final_q = df3.iloc[:, 1].to_list()
        option1_hard = df3.iloc[:, 2].to_list()
        option2_hard = df3.iloc[:, 3].to_list()
        option3_hard = df3.iloc[:, 4].to_list()
        option4_hard = df3.iloc[:, 5].to_list()
        ans_of_hard = df3.iloc[:, 6].to_list()
        # df.to_csv("hard_q.csv")


        questions = list(itertools.chain(simple_final_q, medium_final_q, hard_final_q)) 
        correct_answers = list(itertools.chain(ans_of_simples, ans_of_medium, ans_of_hard))
        
        
        first_option = list(itertools.chain(option1_simple, option1_medium, option1_hard))
        second_option = list(itertools.chain(option2_simple, option2_medium, option2_hard))
        third_option = list(itertools.chain(option3_simple, option3_medium, option3_hard))
        fourth_option = list(itertools.chain(option4_simple, option4_medium, option4_hard))


    df = pd.read_csv(r"Question_files/"+q,encoding="latin-1") # pass you selected q_set here Book-1 is just a sample 
    df1 = df.iloc[:, 0:7]
    df2 = df.iloc[:, 7:14]
    df3 = df.iloc[:, 14:]
    df1.to_csv("Question_files/sim.csv")
    df2.to_csv("Question_files/med.csv")
    df3.to_csv("Question_files/hrd.csv")

    extraction("Question_files/sim.csv","Question_files/med.csv","Question_files/hrd.csv")

que(q)
'''questions = ["Which of the following is not a framework?",
             "Which graphics rendering engine is used in Flutter?",
             "Which HTTP status codes correspond to Server error?",
             "Which is the best searching algorithm in terms of time complexity?",
             "Which command shows the record of all commits?",
             "What is the fundamental unit of Quantum Computing?",
             "Who created Java?",
             "What does typeof typeof 1 will return?",
             "Which DB engine use Key-Value store?",
             "Number of nodes in Perfect Binary Tree of height h?",
             "Which is a self balancing tree with height difference atmost 1?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["ExpressJs", "Nvidia",
                "4XX", "Linear Search",
                "git commit -a", "Qubit",
                "Guido van Rossum", "number", "MongoDB", "2^h",
                "AVL Tree", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["Django", "Gecko",
                "5XX", "Binary Search",
                "git log", "Cubit",
                "Dennis Ritchie", "string", "MySql", "2^(h-1)",
                "Red Black Tree", "7",
                "500 years",
                "Amazon", "Bill Gates"]

third_option = ["PHP", "Blink",
                "3XX", "Ternary Search",
                "git reflog", "Byte",
                "Bjarne Stroustrup", "object", "Redis", "2^h-1",
                "Segment Tree", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Laravel", "Skia",
                 "2XX", "BFS",
                 "git status", "Bit",
                 "James Gosling", "function", "PostgreSQL", "2*h",
                 "Skew Tree",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["PHP", "Skia", "5XX", "Binary Search", "git reflog", "Qubit",
                   "James Gosling", "string", "Redis", "2^h-1", "AVL Tree", "7", "1000 years", "Apple",
                   "Bill Gates"]'''


def select(event):

    b = event.widget
    value = b['text']
    global question_count
    question_count+=1
    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
    for i in range(11):
        if value == correct_answers[i]:
            global i1
            i1=i+1    
            if value == third_option[11]:
               
                def playagain():
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    doubleDipButton.config(state=NORMAL, image=doubleDip)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    playsound.playsound('music/kbc.mp3')
                    mixer.music.load('music/kbc.mp3')
                    mixer.music.play(1)
                    

                def on_closing():
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image11)
                mixer.music.stop()
                mixer.music.load('music/Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.grab_set()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 1 million Pounds')
                centerimg = PhotoImage(file='image/center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='You Won 1 million Pounds', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                happyimage = PhotoImage(file='image/happy.png')
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                     , activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break
            
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])
            
            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=images[i])
            # time.sleep(1)
            mixer.music.load('music/KbcQuestion.mp3')
            mixer.music.set_volume(0.1)
            mixer.music.play()

        if value not in correct_answers:
            def tryagain():
                global i1,name
                db=sqlite3.connect('database/nitish.db')
                cr=db.cursor()
                global amount
                amount1=amount[i1]
                cr.execute("UPDATE regis SET won ='%s' WHERE UNAME='%s'"%(amount1,name))
                db.commit()
                db.close()
                mixer.music.load('music/kbc.mp3')
                mixer.music.play(1)
                global question_count
                question_count=0
                # playsound.playsound('kbc.mp3')
                if 'phoneLifelineButton' in life:
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                if 'lifeline50Button' in life:    
                  lifeline50Button.config(state=NORMAL, image=image50)
                if 'audiencePoleButton' in life:  
                  audiencePoleButton.config(state=NORMAL, image=audiencePole)
                if 'FlipQuestionButton' in life:  
                  doubleDipButton.config(state=NORMAL, image=doubleDip)
                questionArea.delete(1.0, END)
                global q
                que(q)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()

            def on_closing():
                root1.destroy()
                root.destroy()

            # mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            # root1.geometry('500x400')

            root1.title('You won 0 Rupee')
            img = PhotoImage(file='image/center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()
            sadimage = PhotoImage(file='image/sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break

'''def doubleDipLifeline():
    def double_select(value):
        # for i in range(len(questions) - 1):
        #if questionArea.get(1.0, "end-1c") == questions[question_count]:
            if value == correct_answers[question_count]:
                select(value)
            else:
                if value == optionButton1['text']: optionButton1.config(text="")
                if value == optionButton2['text']: optionButton2.config(text="")
                if value == optionButton3['text']: optionButton3.config(text="")
                if value == optionButton4['text']: optionButton4.config(text="")
            optionButton1.config(command=lambda: select(optionButton1['text']))
            optionButton2.config(command=lambda: select(optionButton2['text']))
            optionButton3.config(command=lambda: select(optionButton3['text']))
            optionButton4.config(command=lambda: select(optionButton4['text']))

    
    optionButton1.config(command=lambda: double_select(optionButton1['text']))
    optionButton2.config(command=lambda: double_select(optionButton2['text']))
    optionButton3.config(command=lambda: double_select(optionButton3['text']))
    optionButton4.config(command=lambda: double_select(optionButton4['text']))'''
def lifeline50():
    count=0
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)
    # for i in range(len(questions) - 1):
    if questionArea.get(1.0, 'end-1c') == questions[question_count]:
        visible_option = [correct_answers[question_count]]
        if optionButton1['text'] not in visible_option and count<2:
            count+=1
            optionButton1.config(text='')
        if optionButton2['text'] not in visible_option and count<2:
            count+=1
            optionButton2.config(text='')
        if optionButton3['text'] not in visible_option and count<2:
            count+=1
            optionButton3.config(text='')
        if optionButton4['text'] not in visible_option and count<2:
            count+=1
            optionButton4.config(text='')
def FlipQuestion():
    global i1
    doubleDipButton.config(image=doubleDip)
    doubleDipButton.config(state=DISABLED)
    doubleDipButton.config(image=doubleDipX, state=DISABLED)
    questionArea.delete(1.0, END)
    questionArea.insert(END, questions[i1+1])
    
    optionButton1.config(text=first_option[i1+1])
    optionButton2.config(text=second_option[i1+1])
    optionButton3.config(text=third_option[i1+1])
    optionButton4.config(text=fourth_option[i1+1])
            # time.sleep(1)
    mixer.music.load('music/KbcQuestion.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play()
    global question_count
    question_count+=1
    
def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)
    x=int(random.uniform(60,90))
    y=int(random.uniform(10,60))
    z=int(random.uniform(10,60))
    p=int(random.uniform(10,60))
    progressbarA.place(x=700, y=190)
    progressbarLabelA.place(x=700, y=300)
    progressbarB.place(x=740, y=190)
    progressbarLabelB.place(x=740, y=300)
    progressbarC.place(x=780, y=190)
    progressbarLabelC.place(x=780, y=300)
    progressbarD.place(x=820, y=190)
    progressbarLabelD.place(x=820, y=300)
    if optionButton1['text']==correct_answers[question_count]:
        progressbarA.config(value=x)
        progressbarB.config(value=y)
        progressbarC.config(value=z)
        progressbarD.config(value=p)
    if optionButton2['text']==correct_answers[question_count]:
        progressbarA.config(value=y)
        progressbarB.config(value=x)
        progressbarC.config(value=z)
        progressbarD.config(value=p)
    if optionButton3['text']==correct_answers[question_count]:
        progressbarA.config(value=z)
        progressbarB.config(value=y)
        progressbarC.config(value=x)
        progressbarD.config(value=p)
    if optionButton4['text']==correct_answers[question_count]:
        progressbarA.config(value=p)
        progressbarB.config(value=y)
        progressbarC.config(value=z)
        progressbarD.config(value=x)    
    

    '''# for i in range(len(questions) - 1):
    if questionArea.get(1.0, 'end-1c') == questions[question_count]:
        progressbarA.config(value=audience_a[question_count])
        progressbarB.config(value=audience_b[question_count])
        progressbarC.config(value=audience_c[question_count])
        progressbarD.config(value=audience_d[question_count])'''

    


def phoneLifeline():
    mixer.music.stop()
    mixer.music.load('music/calling.mp3')
    mixer.music.play()

    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    # mixer.music.load('kbc.mp3')
    # mixer.music.play(-1)
    # mixer.music.set_volume(0)
    for i in range(11):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.setProperty('rate', 125)
            engine.say(f'The Answer is {correct_answers[i]}')
            engine.runAndWait()




def get_name():
           

    name_window = Tk()
    name_window.geometry("600x400")
    img = ImageTk.PhotoImage(Image.open("image/center.png"))
    name_window.title('KBC: Kaun Banega Crorepati')
    name_window.config(bg='black')
    favicon = PhotoImage(file="image/favicon.png")
    name_window.iconphoto(False, favicon)
    #name_window.overrideredirect(True)
    #name_window.config(bg="#091e42",pady=100)
    
    def changeOnHover(button, colorOnHover, colorOnLeave):
            button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
            button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))

	
    def home():
        mixer.init()
        mixer.music.load('music/kbc.mp3')
        mixer.music.set_volume(0.05)
        mixer.music.play()
        f1=Frame(bg="black")
        f1.place(x=0,y=0,width=600,height=400)
       
        label = Label(f1, image = img)
        label.pack()
        f1.place(x=0,y=0,width=600,height=400)
        b1=Button(f1,text="Guestplay",command=guestplayuser,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b1.place(x=30,y=300,width=120,height=40)
        changeOnHover(b1, "#28282B", "black")

        b1=Button(f1,text="Login",command=login,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b1.place(x=170,y=300,width=120,height=40)
        changeOnHover(b1, "#28282B", "black")

        
        b2=Button(f1,text="Register",command=register,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=310,y=300,width=120,height=40)
        changeOnHover(b2, "#28282B", "black")

        b2=Button(f1,text="Admin",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white" ,command=adminelogin)
        b2.place(x=450,y=300,width=120,height=40)
        changeOnHover(b2, "#28282B", "black")

    def admine():
        f3=Frame(bg="black")
        f3.place(x=0,y=0,width=600,height=400)
        un=Label(text="Game Setting",font=("",30,"bold"),bg="black",fg="white")
        un.place(x=10,y=10)
        
        def set_selection(csv_files,b):
                    global set1
                    set1+=1
                    if(set1<=1):
                        que(csv_files)
                        b.configure(bg="green",fg="green")
                    else:
                        messagebox.showinfo('Title','SET already selected')
                        
                       
                             
        def quesset():
            def checkcsv():
                csv_files=[]
                cur_dir=os.getcwd()
                cur_dir=cur_dir+'/Question_files'
                content_list=os.listdir(cur_dir)
                for x in content_list:
                    if x.split('.')[-1]=='csv':
                        csv_files.append(x)
                if len(csv_files)==0:
                    return 'No csv file in the directory'
                else:
                    return csv_files
            '''def display_and_select_csv(csv_files):
                i=0
                for file_name in csv_files:
                    print(i,'...',file_name)
                    i+=1
                return csv_files[int(input("Select file to create ML model"))]'''
            
            csv_files=checkcsv()
            
            f4=Frame(bg="black")
            f4.place(x=0,y=0,width=600,height=400)
            un=Label(text="Please select a question set",font=("",30,"bold"),bg="black",fg="white")
            un.place(x=10,y=30)
            b1=Button(f4,text="SET-1",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:set_selection(csv_files[0],b1))
            b1.place(x=50,y=100,width=100,height=40)
            changeOnHover(b1, "#28282B", "black")
            
            un=Label(text=csv_files[0],font=("",20,"bold"),bg="black",fg="red")
            un.place(x=200,y=100)
            b2=Button(f4,text="SET-2",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:set_selection(csv_files[1],b2))
            b2.place(x=50,y=170,width=100,height=40)
            changeOnHover(b2, "#28282B", "black")
            
            un=Label(text=csv_files[1],font=("",20,"bold"),bg="black",fg="red")
            un.place(x=200,y=170)
            b3=Button(f4,text="SET-3",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:set_selection(csv_files[2],b3))
            b3.place(x=50,y=240,width=100,height=40)
            changeOnHover(b3, "#28282B", "black")
            
            un=Label(text=csv_files[2],font=("",20,"bold"),bg="black",fg="red")
            un.place(x=200,y=240)
            b3=Button(f4,text="<<",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=admine,borderwidth = 0)
            b3.place(x=0,y=0,width=40,height=30)
            changeOnHover(b3, "#28282B", "black")
            
            b3=Button(f4,text="Home",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=home)
            b3.place(x=15,y=340,width=100,height=40)
            changeOnHover(b3, "#28282B", "black")
            
            def finish():
                global name
                name='Admin Nitish'
                name_window.destroy()
                global a
                a=1
            b3=Button(f4,text="Finish",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=finish)
            b3.place(x=485,y=340,width=100,height=40)
            changeOnHover(b3, "Green", "black")
            
        def lifeline():
               f5=Frame(bg="black")
               f5.place(x=0,y=0,width=600,height=400)
            
               un=Label(text="Selece any three LifeLines",font=("",30,"bold"),bg="black",fg="white")
               un.place(x=10,y=30)
               b3=Button(f5,text="<<",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=admine,borderwidth = 0)
               b3.place(x=0,y=0,width=40,height=30)
               changeOnHover(b3, "#28282B", "black")
            
               b3=Button(f5,text="Home",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=home)
               b3.place(x=15,y=340,width=100,height=40)
               changeOnHover(b3, "#28282B", "black")
                   
               def finish():
                 global name
                 name='Admin Nitish'  
                 name_window.destroy()
                 global a
                 a=1
               global life
               life.clear()
               def demoColorChange(b,lifeline):
                      global click,life
                      click+=1
                      if(click<=3):
                        b.configure(bg="green",fg="green")
                        life.append(lifeline)
                        
                      else:
                          messagebox.showinfo('Title','3 LifeLines already selected')
               b3=Button(f5,text="Finish",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=finish)
               b3.place(x=485,y=340,width=100,height=40)
               changeOnHover(b3, "Green", "black")
               b5=Button(f5,text="50-50",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:demoColorChange(b5,'lifeline50Button'))
               b5.place(x=40,y=100,width=200,height=40)
               changeOnHover(b5, "green", "black")
               b6=Button(f5,text="PhoneFrend",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:demoColorChange(b6,'phoneLifelineButton'))
               b6.place(x=40,y=170,width=200,height=40)
               changeOnHover(b6, "green", "black")
               b7=Button(f5,text="AudiancePoll",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:demoColorChange(b7,'audiencePoleButton'))
               b7.place(x=300,y=100,width=200,height=40)
               changeOnHover(b7, "green", "black")
               b8=Button(f5,text="FlipQuestion",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lambda:demoColorChange(b8,'FlipQuestionButton'))
               b8.place(x=300,y=170,width=200,height=40)
               changeOnHover(b8, "green", "black")
               

              
                               
               
        b1=Button(f3,text="quesset",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=quesset)
        b1.place(x=160,y=150,width=150,height=40)
        changeOnHover(b1, "#28282B", "black")
            

        b2=Button(f3,text="Home",command=home,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=15,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
            
        b3=Button(f3,text="LifeLines",cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white",command=lifeline)
        b3.place(x=330,y=150,width=150,height=40)
        changeOnHover(b3, "#28282B", "black")
            
    def adminelogin():
        f2=Frame(bg="black")
        f2.place(x=0,y=0,width=600,height=400)
        g1=StringVar()
        g2=StringVar()
        
        un=Label(text="Enter Name",font=("",11,"bold"),bg="black",fg="white")
        un.place(x=200,y=50)
        e1=Entry(f2,font=("",11),textvariable=g1)
        e1.place(x=300,y=50,width=130)

        up=Label(text="Enter Pass",font=("",11,"bold"),bg="black",fg="white")
        up.place(x=200,y=100)
        e2=Entry(f2,font=("",11),show='*',textvariable=g2)
        e2.place(x=300,y=100,width=130)
        
            
        def login1():
            db=sqlite3.connect('database/nitish.db')
            cr=db.cursor()
            r=cr.execute("select * from admine where name='"+g1.get()+"' AND pass='"+g2.get()+"'")
            for r1 in r:
                messagebox.showinfo('Title','Welcome Admin')
                admine()
                break
            else:
                messagebox.showinfo('Title','Invalid User name Pass')
            db.commit()
            db.close()
            g1.set("")
            g2.set("")
           
        
        b1=Button(f2,text="Login",command=login1,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b1.place(x=260,y=160,width=100,height=40)
        changeOnHover(b1, "Green", "black")
            

        b2=Button(f2,text="Home",command=home,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=15,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
            
               
    def register():
        f3=Frame(bg="black")
        f3.place(x=0,y=0,width=600,height=400)
        r1=StringVar()
        r2=StringVar()
        r3=StringVar()


        def register1():
            db=sqlite3.connect('database/nitish.db')
            cr=db.cursor()
            cr.execute("insert into regis values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"','"+'0'"')")
            db.commit()
            db.close()
            messagebox.showinfo('Title','User Registered')
            r1.set("")
            r2.set("")
            r3.set("")
            login()
            
            
        un=Label(text="Enter Name",font=("",11,"bold"),bg="black",fg="white")
        un.place(x=200,y=50)
        e1=Entry(f3,font=("",11),textvariable=r1)
        e1.place(x=300,y=50,width=130)

        up=Label(text="Enter Pass",font=("",11,"bold"),bg="black",fg="white")
        up.place(x=200,y=100)
        e2=Entry(f3,font=("",11),show='*',textvariable=r2)
        e2.place(x=300,y=100,width=130)

        un=Label(text="Enter C.No.",font=("",11,"bold"),bg="black",fg="white")
        un.place(x=200,y=150)
        e1=Entry(f3,font=("",11),textvariable=r3)
        e1.place(x=300,y=150,width=130)
    
        b1=Button(f3,text="Register",command=register1,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b1.place(x=260,y=200,width=100,height=40)
        changeOnHover(b1, "Green", "black")
            

        b2=Button(f3,text="Home",command=home,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=15,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
            
        
        b2=Button(f3,text="Login",command=login,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=480,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
     
    def login():
        f2=Frame(bg="black")
        f2.place(x=0,y=0,width=600,height=400)
        g1=StringVar()
        g2=StringVar()
        
        un=Label(text="Enter Name",font=("",11,"bold"),bg="black",fg="white")
        un.place(x=200,y=50)
        e1=Entry(f2,font=("",11),textvariable=g1)
        e1.place(x=300,y=50,width=130)

        up=Label(text="Enter Pass",font=("",11,"bold"),bg="black",fg="white")
        up.place(x=200,y=100)
        e2=Entry(f2,font=("",11),show='*',textvariable=g2)
        e2.place(x=300,y=100,width=130)
        
        def login1():
            global name
            name = g1.get()
            db=sqlite3.connect('database/nitish.db')
            cr=db.cursor()
            r=cr.execute("select * from regis where UNAME='"+g1.get()+"' AND UPASS='"+g2.get()+"'")
            for r1 in r:
                messagebox.showinfo('Title','Welcome')
                name_window.destroy()
                global a
                a=1
                break
            else:
                messagebox.showinfo('Title','Invalid User name Pass')
            db.commit()
            db.close()
            g1.set("")
            g2.set("")
           
        
        b1=Button(f2,text="Login",command=login1,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b1.place(x=260,y=160,width=100,height=40)
        changeOnHover(b1, "Green", "black")
        b2=Button(f2,text="Home",command=home,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=15,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
        b2=Button(f2,text="Register",command=register,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=480,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
    def guestplayuser():
        def save_info():
            global name,name1
            name = g1.get()
            name1 = g2.get()
            if name =='' and name1 == '':
               messagebox.showwarning("Name Error", "Enter Your Name")
            else:
               ''' with open("users.txt", 'a') as file:
                    file.write(name + '\n')
                    name_window.destroy()'''
               db=sqlite3.connect('database/kbc_database2.db') 
               cr=db.cursor()
               cr.execute("insert into kbc1 (first_name,last_name,won_price) values('"+g1.get()+"','"+g2.get()+"','"+'0'"')")
               db.commit()
               db.close()
               global a
               a=1
               name_window.destroy()
            
        f2=Frame(bg="black")
        f2.place(x=0,y=0,width=600,height=400)
        
        g1=StringVar()
        g2=StringVar()
        lbl= Label( text="Enter First Name",font=("",11),bg="black",fg="white").place(x=150,y=50)
        first_name = Entry(f2,textvariable=g1).place(x=300,y=50,width=130)
        lb2 = Label( text="Enter Last name",font=("",11),bg="black",fg="white").place(x=150,y=100)
        last_name = Entry(f2,textvariable=g2).place(x=300,y=100,width=130)
        btn = Button( text="Submit", command=save_info,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        btn.place(x=260,y=160,width=100,height=40)
        changeOnHover(btn, "green", "black")
        
        b2=Button(f2,text="Home",command=home,cursor="hand2",font=('Arial Rounded MT Bold',16,'bold'), bg="black",fg="white")
        b2.place(x=15,y=340,width=100,height=40)
        changeOnHover(b2, "#28282B", "black")
        
        #print(input_name.get())
        #lbl.pack()
        #first_name.pack()
        #lb2.pack()
        #last_name.pack()
        #btn.pack()
    home()    
    name_window.mainloop()
    
get_name()

if(a==1):
    mixer.init()
    mixer.music.load('music/kbc.mp3')
    mixer.music.set_volume(0.05)
    mixer.music.play()
    root = Tk()
    root.geometry('1270x652+0+0')
    root.resizable(None, None)
    root.title('KBC: Kaun Banega Crorepati')
    root.config(bg='black')
    favicon = PhotoImage(file="image/favicon.png")
    root.iconphoto(False, favicon)



    leftFrame = Frame(root, bg='black')
    leftFrame.grid(row=0, column=0, padx=0)

    rightFrame = Frame(root, bg='black', pady=25)
    rightFrame.grid(row=0, column=1, padx=(0, 50))

    topFrame = Frame(leftFrame, bg='black', pady=15)
    topFrame.grid(row=0, column=0)
    welcome_name=Label(topFrame,text="welcome "+name+' '+name1,font=("",20),bg="black",fg="white")
    welcome_name.grid(row=0,column=1)
                           
    middleFrame = Frame(leftFrame, bg='black', pady=15)
    middleFrame.grid(row=1, column=0)

    bottomFrame = Frame(leftFrame, bg='black')
    bottomFrame.grid(row=2, column=0)

    centreImage = PhotoImage(file='image/center.png')
    logoLabel = Label(middleFrame, image=centreImage, bd=0, width=400, height=200, bg='black')
    logoLabel.grid(row=0, column=0)

    if('lifeline50Button'in life):
        image50 = PhotoImage(file='image/50-50.png')
        image50x = PhotoImage(file='image/50-50-X.png')

        lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                                  height=80, command=lifeline50)
        lifeline50Button.grid(row=1, column=0)
    if('audiencePoleButton' in life):
        audiencePole = PhotoImage(file='image/audiencePole.png')
        audiencePolex = PhotoImage(file='image/audiencePoleX.png')
        audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                                        width=180, height=80, command=audiencePoleLifeline)
        audiencePoleButton.grid(row=1, column=1)
    if('phoneLifelineButton'in life):
        phoneImage = PhotoImage(file='image/phoneAFriend.png')
        phoneImageX = PhotoImage(file='image/phoneAFriendX.png')
        phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                                 height=80, command=phoneLifeline)
        phoneLifelineButton.grid(row=1, column=2)
    if('FlipQuestionButton' in life):    
        doubleDip = PhotoImage(file='image/doubleDip.png')
        doubleDipX = PhotoImage(file='image/doubleDipX.png')
        doubleDipButton = Button(topFrame, image=doubleDip, bd=0, bg='black', cursor='hand2', activebackground='black',
                                 width=180, height=80, command=FlipQuestion)
        doubleDipButton.grid(row=1, column=3)
    '''if('FlipQuestionButton' in life):    
        FlipQuestion = PhotoImage(file='image/doubleDip.png')
        FlipQuestionX = PhotoImage(file='image/doubleDip.png')
        FlipQuestionButton = Button(topFrame, image=doubleDip, bd=0, bg='black', cursor='hand2', activebackground='black',
                                 width=180, height=80, command=doubleDipLifeline)
        FlipQuestionButton.grid(row=1, column=3)   ''' 
    callimage = PhotoImage(file='image/phone.png')
    callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
    callButton.place(x=70, y=260)

    amountimage = PhotoImage(file='image/Picture0.png')
    image1 = PhotoImage(file='image/Picture1.png')
    image2 = PhotoImage(file='image/Picture2.png')
    image3 = PhotoImage(file='image/Picture3.png')
    image4 = PhotoImage(file='image/Picture4.png')
    image5 = PhotoImage(file='image/Picture5.png')
    image6 = PhotoImage(file='image/Picture6.png')
    image7 = PhotoImage(file='image/Picture7.png')
    image8 = PhotoImage(file='image/Picture8.png')
    image9 = PhotoImage(file='image/Picture9.png')
    image10 = PhotoImage(file='image/Picture10.png')
    image11 = PhotoImage(file='image/Picture11.png')


    images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11]

    amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
    amountlabel.grid(row=0, column=0)

    layoutimage = PhotoImage(file='image/layout1.png')
    layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
    layoutlabel.grid(row=0, column=0)


    questionArea = Text(bottomFrame, font=('arial', 16, 'bold'), bg='black', fg='white', width=60, height=2,
                            wrap='word',bd=0)
    questionArea.place(x=90, y=25)
    questionArea.insert(END, questions[0])


    labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='black', fg='white')
    labelA.place(x=60,y=110)

    optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 16, 'bold'), bg="black", fg='white',
                                      cursor='hand2', bd=0, activebackground='black',activeforeground='white')
    optionButton1.place(x=100, y=103)

    labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
    labelB.place(x=520,y=110)

    optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                                      cursor='hand2', bd=0, activebackground='black', activeforeground='white')
    optionButton2.place(x=570,y=103)

    labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
    labelC.place(x=60,y=175)

    optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                                     cursor='hand2', bd=0, activebackground='black', activeforeground='white')
    optionButton3.place(x=100,y=165)

    labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
    labelD.place(x=520,y=175)

    optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                                     cursor='hand2', bd=0, activebackground='black', activeforeground='white')
    optionButton4.place(x=570, y=165)

    progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)
    root.mainloop()

        
