import random
import time
import os

print("=".center(50,'='))
time.sleep(0)

print()
print("\t\t   Welcome to")
print("\t\tOnline Quix Game")

print("=".center(50,'='))
time.sleep(0)
print()

a=input("\tEnter Your Name - ")

print("=".center(50,'='))
time.sleep(0)
print()

print("\n\tOK ",a," Let's Start The Game")
time.sleep(1)
questions=["Who is The Prime Minister of India",
           "In Which Country Area 51 is Located",
           "Which one is the largest Continent in the world",
           "What is the Latest Version of Windows Since 2019",
           "Which One of These Is not a Software Company",
           "How Many MB Makes 1 GB",
           "Facebook Was Firstly Developed By",
           "Founder of Apple is",
           "_________ is one of The Founder of Google",
           "BIGG BOSS season 13 Starts in ____ & ends in _____",
           "Apple's Laptop is Also Known as",
           "First Apple Computer is Known as",
           "Joystick is used For",
           "____________ is used to Encrypt Drives in Computer"]
answer=["Narendra Modi","United States","Asia","Windows 10","Honda","1024","Mark Zuckenberg",
        "Steve Jobs","Larry Page","2019 - 2020","Macbook","Mactonish","Playing Games","Bitlocker"]
wronganswers=[["Amit Shah","Aditya Nath Yogi","Azhar Ansari"],
              ["India","Africa","Iraq"],
              ["South Africa","North America","Europe"],
              ["Windows 7","Windows 8","Windows 11"],
              ["Oracle","Microsoft","Google"],
              ["10024","1004","2024"],
              ["Bill Gates","Larry Page","Azhar Ansari"],
              ["Azhar Ansari","Charles Babbage","Sundar Pichai"],
              ["Larry Hensberg","Sunder Pichai","Bill Gates"],
              ["2020 - 2021","Not Starts Now","2018 - 2019"],
              ["ThinBook","Notebook","ChromeBook"],
              ["Apple v.1","Apple Computer","Appbook"],
              ["Giving output command","Shutting down Computer","Log off Computer"],
              ["KeyGuard","Windows Secure","No Software like this"]]

attempquestion=[]
count=1
Point=0

while True:
    while True:
        selectquestion=random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex=questions.index(selectquestion)
            correctanswer=answer[questionindex]
            break
    optionslist=[]
    inoptionlist=[]
    optioncount=1
    while optioncount<4:
        optionselection=random.choice(wronganswers[questionindex])
        if optionselection in inoptionlist:
            pass
        elif optionselection not in inoptionlist:
            optionslist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount+=1
    optionslist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    
    a1=True
    while a1:
        a=random.choice(optionslist)
        if a in alreadydisplay:
            pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b=random.choice(optionslist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1=not True
    a1=True
    while a1:
        c=random.choice(optionslist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1=not True
    a1=True
    while a1:
        d=random.choice(optionslist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1=not True
    
    right_answer=""
    if correctanswer==a:
        right_answer="a"
    elif correctanswer==b:
        right_answer="b"
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"

    print("=".center(50,'='))
    print("\t\t You Win - ",Point,'Points')
    print("=".center(50,'='))
    time.sleep(1)
    print("\n\tQuestion ",count," on your Screen")
    print("=".center(70,'='))
    time.sleep(1)
    print("  |  Question - ",selectquestion)
    print("=".center(70,'='))
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  A. ",a)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  B. ",b)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  C. ",c)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  D. ",d)
    print("\t-----------------------------------------------------------------------------")
    
    useranswer=input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...").lower()
    if useranswer==right_answer:
        if count==1:
            Point=10
        elif count==2:
            Point=20
        elif count==3:
            Point=30
        elif count==4:
            Point=40
        elif count==5:
            Point=50
        elif count==6:
            Point=60
        elif count==7:
            Point=70
        elif count==8:
            Point=80
        elif count==9:
            Point=90
        elif count==10:
            Point=100
    
            os.system('cls')
            print("=".center(70,'='))
            print(" Congratulations! ".center(70,'='))
            print(" You Won The Game ".center(70,'='))
            print("=".center(70,'='))
            print(f"\n\n\t\t You Won {Point} Points. ",)
            print()
            print("=".center(70,'='))
            break

        print("=".center(70,'='))
        print(" Congratulations! ".center(70,'='))
        print(" You Won The Game ".center(70,'='))
        print("=".center(70,'='))
        
        count+=1
    elif useranswer=="q":
            print("\n\n\t\t You Won Point. ",Point)
            break
    else:
        print("=".center(70,'='))
        print("\t\t\tWrong Answer")
        print("=".center(70,'='))
        print("\n\n\t\t \tYou Won Point. ",Point)
        print('')
        print("=".center(70,'='))
        print(" Wrong Answer ".center(70,'='))
        print(f" You Won {Point} Point.  ".center(70,'='))
        print("=".center(70,'='))
        break