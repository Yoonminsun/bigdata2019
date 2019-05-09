from tkinter import *
from tkinter import ttk

temp=[]
operation={'r':['-','+','*','/'],'b':['AC',0,'=']}

def button_pressed(value):
    global temp
    print(value, temp)
    # 숫자
    if not value in operation['r'] and not value in operation['b'] or value==0:
        if temp and type(temp[len(temp)-1])==int:
            temp[len(temp)-1] = int(str(temp[len(temp)-1])+str(value))
        else:
            temp.append(value if type(value) == int else str(value))
        number_entry.insert("end",value)

    # 연산
    elif value in operation['r'] and number_entry.get()!='':
        temp.append(value if type(value) == int else str(value))
        number_entry.delete(0,'end')

    # = , AC
    else:
        if value=='AC':
            number_entry.delete(0,'end')
            temp=[]
        elif value=='=' and temp:
            number_entry.delete(0, 'end')
            result = operation_calc(temp)
            number_entry.insert(0,result)

# 연산 함수
def operation_calc(clist):
    result=clist[0]
    opt=''
    for i in range(1,len(clist)):
        i=clist[i]
        if type(i)==int:
            if opt=='-':
                result = result-i
            elif opt=='+':
                result = result + i
            elif opt=='/':
                result = result / i
            else:
                result = result * i
        else:
            opt=i
    return result

root = Tk()
root.title("Calculator_Yoon")
root.geometry("350x200")
# root.bind('<Key>',key_input)

entry_value = StringVar(root,value='')

number_entry = ttk.Entry(root,textvariable=entry_value,width=20)
number_entry.grid(row=0,columnspan=3)

# GUI 구성
for i in range(4):
    for j in range(4):
        index = j + (3 * (i - 1))
        if j==3:
            btxt=operation['r'][i]
        elif i==0:
            btxt=operation['b'][j]
        else:
            btxt = index + 1
        globals()['num{}'.format(index)] = ttk.Button(root, text="%s"%btxt
                                                      ,command=lambda btxt=btxt: button_pressed(btxt))
        globals()['num{}'.format(index)].grid(row=4-i, column=j)

root.mainloop()

