from tkinter import*
import time
root=Tk()
root.title('Digital Clock')
root.geometry('1380x1080')
root.config(bg='orange')
#Function for clock
def clock():
    h=str(time.strftime('%H'))
    m=str(time.strftime('%M'))
    s=str(time.strftime('%S'))
    #print(h,m,s)
    #this if statement for when AM and when PM
    if int(h)>12 and int(m)>0:
        Label_for_noon.config(text='PM')

    #this if statement for convert 24 to 15
    if int(h)>12:
        h=str(int(h)-12)

    Label_for_hrs.config(text=h)
    Label_for_min.config(text=m)
    Label_for_sec.config(text=s)

    Label_for_hrs.after(200,clock)
#Label For Clock Heading
Label_for_heading=Label(root,text='Digital Clock',font=('times new roman',50,'bold'),bg='white',fg='red')
Label_for_heading.place(x=330,y=100,width=700,height=70)
#Label For Hours
Label_for_hrs=Label(root,text='15',font=('times new roman',50,'bold'),bg='blue',fg='white')
Label_for_hrs.place(x=350,y=200,width=150,height=150)

Label_for_hrs1=Label(root,text='Hour',font=('times new roman',20,'bold'),bg='blue',fg='white')
Label_for_hrs1.place(x=350,y=360,width=150,height=50)
#Label For Minutes
Label_for_min=Label(root,text='15',font=('times new roman',50,'bold'),bg='blue',fg='white')
Label_for_min.place(x=520,y=200,width=150,height=150)

Label_for_min1=Label(root,text='Minute',font=('times new roman',20,'bold'),bg='blue',fg='white')
Label_for_min1.place(x=520,y=360,width=150,height=50)
#Label For Seconds
Label_for_sec=Label(root,text='15',font=('times new roman',50,'bold'),bg='red',fg='white')
Label_for_sec.place(x=690,y=200,width=150,height=150)

Label_for_sec1=Label(root,text='Second',font=('times new roman',20,'bold'),bg='red',fg='white')
Label_for_sec1.place(x=690,y=360,width=150,height=50)
#Label For Noon
Label_for_noon=Label(root,text='AM',font=('times new roman',50,'bold'),bg='green',fg='white')
Label_for_noon.place(x=860,y=200,width=150,height=150)

Label_for_noon1=Label(root,text='Noon',font=('times new roman',20,'bold'),bg='green',fg='white')
Label_for_noon1.place(x=860,y=360,width=150,height=50)
#Function call
clock()

root.mainloop()