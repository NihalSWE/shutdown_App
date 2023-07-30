# Shutdown App 

from tkinter import *
import os


def restart():
    os.system("shutdown -r -t 1")

def shutdown():
    os.system("shutdown -s -t 1")

def restart_time():
    os.system("shutdown -r -t 15")


st=Tk()

st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")
#restart
r_button=Button(st,text="Restart",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart)
r_button.place(x=150,y=60,width=200,height=50)
#shutdown
st_button=Button(st,text="Shutdown",font=("arial",20,"bold"),bg="red",cursor="plus",command=shutdown)
st_button.place(x=150,y=170,width=200,height=50)
#restart with time
t_button=Button(st,text="Restart Time",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart_time)
t_button.place(x=150,y=270,width=200,height=50)
#close
c_button=Button(st,text="Close",font=("arial",20,"bold"),bg="red",cursor="plus",command=st.destroy)
c_button.place(x=150,y=370,width=200,height=50)


st.mainloop()