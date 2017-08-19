import tkinter

root = tkinter.Tk()

# integer value
val = tkinter.IntVar()
val.set(0)

# slider function
def slide(sc1):
  label.config(text = 'value = %d' % int(sc1))

# enter 쳤을 때
def tbox_enter(event):
#  label.config(text = tbox.get())
  try:
    val.set(int(tbox.get()))
    label.config(text = 'value = %d' % val.get())
  except ValueError:
    label.config(text = 'not a number')
  tbox.delete(0,'end')

#label
label = tkinter.Label(root, text = 'Value = %s' % val.get())
label.pack()

# 텍스트 상자 생성
tbox = tkinter.Entry(root, width = 5)
#tbox.pack()
tbox.pack(side='right')

# bind
tbox.bind('<Return>', tbox_enter)

#slider
#scale_slider = tkinter.Scale(root, label = 'Scale', orient = 'h', from_ =0, to = 100, showvalue = True, variable = val, command = slide)
#scale_slider.pack()
scale_slider = tkinter.Scale(root, orient = 'h', from_ =0, to = 100, showvalue = False, variable = val, command = slide)
scale_slider.pack(side='right')

root.mainloop()

