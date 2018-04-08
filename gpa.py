import Tkinter as tk
from functools import partial

def resultCalc(label_result,n1,n2,n3,n4,n5,n6,n7,n8,):
	sub1 = n1.get()
	sub2 = n2.get()
	sub3 = n3.get()
	sub4 = n4.get()
	sub5 = n5.get()
	sub6 = n6.get()
	sub7 = n7.get()
	sub8 = n8.get()
	dict = { 'O' :10.0 , 'A+':9 ,'A' :8.5,'B+':8,'B':7,'C':6,'P':5,'F' :4}
	result =  dict[sub1] *4 +dict[sub2] *4 +dict[sub3] *4 + dict[sub4]*3 +dict[sub5]*3 +dict[sub6]*3 +dict[sub7]*1 +dict[sub8]*1
	result = result/23
	label_result.config(text="SGPA is %f" %result)
	return  result

root =tk.Tk()
root.geometry('300x300')
root.title('GPA Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.StringVar()
number6 = tk.StringVar()
number7 = tk.StringVar()
number8 = tk.StringVar()
number9 = tk.StringVar()

labelSub1=tk.Label(root,text='Subject 1')
labelSub1.grid(row=1,column = 1)
labelSub2=tk.Label(root,text='Subject 2')
labelSub2.grid(row=2,column = 1)
labelSub3=tk.Label(root,text='Subject 3')
labelSub3.grid(row=3,column = 1)
labelSub4=tk.Label(root,text='Subject 4')
labelSub4.grid(row=4,column = 1)
labelSub5=tk.Label(root,text='Subject 5')
labelSub5.grid(row=5,column = 1)
labelSub6=tk.Label(root,text='Subject 6')
labelSub6.grid(row=6,column = 1)
labelSub7=tk.Label(root,text='Subject 7')
labelSub7.grid(row=7,column = 1)
labelSub8=tk.Label(root,text='Subject 8')
labelSub8.grid(row=8,column = 1)


entrySub1= tk.Entry(root,textvariable = number1)
entrySub1.grid(row=1,column =2)
entrySub2= tk.Entry(root,textvariable = number2)
entrySub2.grid(row=2,column =2)
entrySub3= tk.Entry(root,textvariable = number3)
entrySub3.grid(row=3,column =2)
entrySub4= tk.Entry(root,textvariable = number4)
entrySub4.grid(row=4,column =2)
entrySub5= tk.Entry(root,textvariable = number5)
entrySub5.grid(row=5,column =2)
entrySub6= tk.Entry(root,textvariable = number6)
entrySub6.grid(row=6,column =2)
entrySub7= tk.Entry(root,textvariable = number7)
entrySub7.grid(row=7,column =2)
entrySub8= tk.Entry(root,textvariable = number8)
entrySub8.grid(row=8,column =2)


labelResult= tk.Label(root)
labelResult.grid(row =10,column =2)

O=10.0
Ap = 9
A =8.5
Bp = 8
B=7.5
C=7
D= 6.5
F=P=0

resultCalc = partial (resultCalc,labelResult,number1,number2,number3,number4,number5,number6,number7,number8)
calcButton =tk.Button(root,text='Calculate SGPA',command = resultCalc)
calcButton.grid(row=9,column = 1)

root.mainloop()
