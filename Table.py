
from tkinter import *
def showTable():
    table=entry.get()
    num1=int(table)*1
    num2=int(table)*2
    num3=int(table)*3
    num4=int(table)*4
    num5=int(table)*5
    num6=int(table)*6
    num7=int(table)*7
    num8=int(table)*8
    num9=int(table)*9
    num10=int(table)*10
    
    labelText1.set(table +'*'+'1='+str(num1))
    labelText2.set(table +'*'+'2='+str(num2))
    labelText3.set(table +'*'+'3='+str(num3))
    labelText4.set(table +'*'+'4='+str(num4))
    labelText5.set(table +'*'+'5='+str(num5))
    labelText6.set(table +'*'+'6='+str(num6))
    labelText7.set(table +'*'+'7='+str(num7))
    labelText8.set(table +'*'+'8='+str(num8))
    labelText9.set(table +'*'+'9='+str(num9))
    labelText10.set(table +'*'+'10='+str(num10))

root=Tk()

entry=Entry(root) 
entry.pack()
Button(root,text='Show Table',command = showTable).pack()

labelText1=StringVar()
labelText1.set('----------')
Label(root,textvariable=labelText1,bg='green').pack()


labelText2=StringVar()
labelText2.set('----------')
Label(root,textvariable=labelText2,bg='red').pack()

labelText3=StringVar()
labelText3.set('----------')
Label(root,textvariable=labelText3,bg='brown').pack()

labelText4=StringVar()
labelText4.set('----------')
Label(root,textvariable=labelText4,bg='blue').pack()

labelText5=StringVar()
labelText5.set('----------')
Label(root,textvariable=labelText5,bg='orange').pack()

labelText6=StringVar()
labelText6.set('----------')
Label(root,textvariable=labelText1,bg='pink').pack()

labelText7=StringVar()
labelText7.set('----------')
Label(root,textvariable=labelText7,bg='white').pack()

labelText8=StringVar()
labelText8.set('----------')
Label(root,textvariable=labelText8,bg='yellow').pack()

labelText9=StringVar()
labelText9.set('----------')
Label(root,textvariable=labelText9,bg='violet').pack()

labelText10=StringVar()
labelText10.set('----------')
Label(root,textvariable=labelText10,bg='orange').pack()


root.mainloop() 