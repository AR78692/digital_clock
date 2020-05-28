from tkinter import*
import time
root=Tk()
root.title('Digital Clock')
root.geometry('1350x700+0+0')
root.config(bg='#081923')
#Function for clock
def clock():
    h=str(time.strftime('%H'))
    m=str(time.strftime('%M'))
    s=str(time.strftime('%S'))
    #print(h,m,s)
    #this if statement for when AM and when PM
    if int(h)>12 and int(m)>0:
        lbl_noon.config(text='PM')

    #this if statement for 24 to 12 convert 
    if int(h)>12:
        h=str(int(h)-12)

    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)

#For Label Hours
lbl_hr=Label(root,text='12',font=('times new roman',50,'bold'),bg='#0875B7',fg='white')
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr1=Label(root,text='Hour',font=('times new roman',20,'bold'),bg='#0875B7',fg='white')
lbl_hr1.place(x=350,y=360,width=150,height=50)
#For Label Minutes
lbl_min=Label(root,text='12',font=('times new roman',50,'bold'),bg='#0875B7',fg='white')
lbl_min.place(x=520,y=200,width=150,height=150)

lbl_min1=Label(root,text='Minute',font=('times new roman',20,'bold'),bg='#0875B7',fg='white')
lbl_min1.place(x=520,y=360,width=150,height=50)
#For Label Seconds
lbl_sec=Label(root,text='12',font=('times new roman',50,'bold'),bg='#0875B7',fg='white')
lbl_sec.place(x=690,y=200,width=150,height=150)

lbl_sec1=Label(root,text='Second',font=('times new roman',20,'bold'),bg='#0875B7',fg='white')
lbl_sec1.place(x=690,y=360,width=150,height=50)
#For Label Noon
lbl_noon=Label(root,text='AM',font=('times new roman',50,'bold'),bg='#0875B7',fg='white')
lbl_noon.place(x=860,y=200,width=150,height=150)

lbl_noon1=Label(root,text='Noon',font=('times new roman',20,'bold'),bg='#0875B7',fg='white')
lbl_noon1.place(x=860,y=360,width=150,height=50)
clock()


root.mainloop()