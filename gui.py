from tkinter import *

import random
import pdb

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# opening the file in read mode
my_file = open("serbian phrases", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.replace('\n', '  ').split('  ')
bymultspaces=data.split(r"\\s{2,}");
#print(data_into_list,bymultspaces,sep='\n')
my_file.close()

T=[['a','a']]
y=0
z=0
g=0
for x in data_into_list:
    if x=='':
        continue
    if g%2==1 and g !=0:
        z+=1
        T.append(['a', 'a'])
    if g % 2 == 0 and g != 0:
        y+=1
        z=0

    T[y][z%2]=x

    g+=1

T.remove(['a','a'])


window = Tk()
window.title("serbian")
window.configure(bg='blue')
window.geometry('550x250')
CorrectAnswers=[]


def clicked():
    #res = "Welcome to " + txt.get()
    question()
    #lbl.configure(text=res)


btn = Button(window, text=">", command=clicked)
btn.grid(column=7, row=5)
choices=[]
lbl2 = Label(window, text="TRUE", fg="green", padx=10, pady=5)
#lbl2.grid(column=2, row=13,rowspan=2,sticky="W",pady=5)
#lbl2.grid_forget()
#B = Button(window, text ="NEXT", command = next)
#B.grid(column=4, row=5,sticky="W",pady=5)

def next():
    lbl2.grid_forget()
    question()

def question():
    global choices
    global answer
    global answerindex
    choices = random.choices(T, k=3)

    answer = random.choice(choices)


    answerindex = T.index(answer)
    print(T[answerindex][0], 'choices')
   # pdb.set_trace()
    rad1 = Radiobutton(window, text=choices[0][1], value=1, padx=5, pady=5)
    rad2 = Radiobutton(window, text=choices[1][1], value=2)
    rad3 = Radiobutton(window, text=choices[2][1],value=3)
    rad1.bind("<Button-1>", ent)
    rad2.bind("<Button-1>", ent)
    rad3.bind("<Button-1>", ent)

    lbl1 = Label(window, text=T[answerindex][0],fg="white",bg="black", padx = 10, pady=5)

    lbl1.grid(column=2, row=0,rowspan=2,sticky="W",pady=5)
    rad1.grid(column=1, row=3,sticky="W",padx=5)
    rad2.grid(column=1, row=5,sticky="W",rowspan=2,padx=5)
    rad3.grid(column=1, row=7,sticky="W",rowspan=2,padx=5)

def ent(event):
    #print(event.widget.cget("text"),T[answerindex][0])
    lbl2.grid(column=2, row=13, rowspan=2, sticky="W", pady=5)
    if event.widget.cget("text") == T[answerindex][1]:
        CorrectAnswers.append(event.widget.cget("text"))
        lbl2.grid(column=2, row=6,rowspan=2,sticky="W",pady=5)
        #question()
    else:
        lbl2.grid(column=2, row=6, rowspan=2, sticky="W", pady=5)
        lbl2.config(text = "wrong",fg="red")
question()
print(choices, 'choices')



def close_window():
    window.quit()


# exit()
window.mainloop()
