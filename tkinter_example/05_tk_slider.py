import tkinter

root = tkinter.Tk()

# integer value
val = tkinter.IntVar()
val.set(0)

# slider function
def slide(sc1):
  label.config(text = 'value = %d' % int(sc1))

#label
label = tkinter.Label(root, text = 'Value = %s' % val.get())
label.pack()

#slider
scale_slider = tkinter.Scale(root, label = 'Scale', orient = 'h', from_ =0, to = 100, showvalue = True, variable = val, command = slide)
scale_slider.pack()

root.mainloop()

