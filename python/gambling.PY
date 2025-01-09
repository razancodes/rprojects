#slot machine program in python

import random
totalbalance=int(input("Enter the Total Balance to begin with: "))
betamount=0
winningamt=0
graphlist=[]

def displayer(list1):
    print("*"*14)
    j=0
    for i in list1:
        print(i, end='')
        if j<2:
            print("|", end='')
        j+=1
    print()
    print("*"*14)

def bet(num1, list1):
    if list1.count(' 🍒 ')==3:
        return num1*3
    elif list1.count(' 7️ ')==3:
        return num1*7
    elif list1.count(' 📌 ')==3:
        return num1*4
    elif list1.count(' 🔔 ')==3:
        return num1*2
    else:
        return 0
    

def spinner():
    choices=[' 7️ ',' 🍒 ',' 📌 ', ' 🔔 ',' 🔔 ',' 7️ ',' 7️ ',' 7️ ']
    slotlist=[]
    for i in range(3):
        slotlist.append(random.choice(choices))
    return slotlist


def intro():
    global totalbalance
    global winningamt
    graphlist.append(totalbalance)
    print("-"*10)
    print("WELCOME TO RAZAN'S SLOT MACHINE: ")
    print("-"*10)
    print(f"The Balance Left is: {totalbalance}")
    num1=int(input("Enter the total bet: $"))
    totalbalance-=num1
    
    print(f"The balance left: {totalbalance}")

    return num1


while totalbalance>0:
    betamount=intro()
    spinner1=spinner()
    displayer(spinner1)
    winningamt=bet(betamount,spinner1)
    print(f"Winning amount: {winningamt}")
    totalbalance+=winningamt


print(graphlist)




