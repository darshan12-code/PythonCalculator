from tkinter import *

def click(event):
     global scvalue
     text=event.widget.cget("text")
     print(text)
     if text=="=":
          if scvalue.get().isdigit():
               value=int(scvalue.get())
          else:
               value=eval(screen.get())

          scvalue.set(value)
          screen.update()
     elif text=="c":
          scvalue.set("")
          screen.update()
     else:
          scvalue.set(scvalue.get()+text)
          screen.update()
root=Tk()
root.geometry("500x800")
root.title("MyCaculator ")
root['background']='grey'

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
 
"""for j in range(1,4):
 f=Frame(root,bg="grey")
 for i in range(1,10):
      b=Button(f,text=f"{i}",padx=28,pady=22,font="lucida 35 bold")
      b.pack(side=LEFT,padx=18,pady=12)

 
 f.pack()
"""
f=Frame(root,bg="#856ff8")
b=Button(f,text=f"1",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"2",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=f"3",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="#856ff8")

b=Button(f,text=f"4",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"5",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=f"6",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="#856ff8")

b=Button(f,text=f"7",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"8",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=f"9",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="#856ff8")

b=Button(f,text=f"=",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=f"0",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text=f"c",padx=8,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="#856ff8")

b=Button(f,text=f"+",padx=30,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)
b=Button(f,text=f"-",padx=30,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)

b=Button(f,text=f"*",padx=30,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="#856ff8")

b=Button(f,text=f"/",padx=35,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)
b=Button(f,text=f"",padx=37,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)

b=Button(f,text=f"%",padx=22,pady=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=20,pady=5,fill=X)
b.bind("<Button-1>",click)
f.pack()

"""b=Button(f,text=f"4",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b=Button(f,text=f"5",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b=Button(f,text=f"6",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b=Button(f,text=f"7",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b=Button(f,text=f"8",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b=Button(f,text=f"9",padx=28,pady=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
"""



root.mainloop()