# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# opening the file in read mode
my_file = open("serbian phrases", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
words = re.split(r'\s{2,}', data)
print(words,'words')
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

print (T)
