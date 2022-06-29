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
print(data_into_list,bymultspaces,sep='\n')
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
# for x in T:
#     print (x)
#     if x==['a','a']:
#         T.remove([x])

window = Tk()
window.title("serbian")
window.geometry('550x250')


lbl = Label(window, text="Hello")


lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


def clicked():
    res = "Welcome to " + txt.get()

    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
choices=[]
def question():
    global choices
    global answer
    global answerindex
    choices = random.choices(T, k=3)

    answer = random.choice(choices)
    #answer = random.choice(answe)
   # print(rad, 'rad')

    answerindex = T.index(answer)
    print(T[answerindex][0], 'choices')
   # pdb.set_trace()
    rad1 = Radiobutton(window, text=choices[0][1], value=1)
    rad2 = Radiobutton(window, text=choices[1][1], value=2)
    rad3 = Radiobutton(window, text=choices[2][1], value=3)
    rad1.bind("<Button-1>", ent)
    rad2.bind("<Button-1>", ent)
    rad3.bind("<Button-1>", ent)

    lbl1 = Label(window, text=T[answerindex][0])

    lbl1.grid(column=0, row=2)
    rad1.grid(column=3, row=1)
    rad2.grid(column=3, row=2)
    rad3.grid(column=3, row=3)

def ent(event):
    print(event.widget.cget("text"),T[answerindex][0])
    if event.widget.cget("text") == T[answerindex][1]:
        print('hey')
        question()
question()
print(choices, 'choices')



def close_window():
    window.quit()


# exit()
window.mainloop()
