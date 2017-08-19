import tkinter
root = tkinter.Tk()

r = tkinter.IntVar()
r.set(0)

def add():
  r.set(int(abox.get()) + int(bbox.get()))
  label.config(text = '결과값 = %d' % int(r.get()))

def add_event(event):
  add()

#top label
label = tkinter.Label(root, text = '결과값 = %d' % r.get())
label.config(text = '결과값 = %d' % int(r.get()))
label.pack()

#boxes
abox = tkinter.Entry(root, width = 10)
label_plus = tkinter.Label(root, text = ' + ')
bbox = tkinter.Entry(root, width = 10)
abox.pack(side='left')
label_plus.pack(side='left')
bbox.pack(side='left')

#bind boxes
abox.bind('<Return>', add_event)
bbox.bind('<Return>', add_event)

#add button
button = tkinter.Button(root, text='Add!', command=add)
button.pack()

root.mainloop()
