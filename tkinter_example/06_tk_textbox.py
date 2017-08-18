import tkinter

root = tkinter.Tk()

# enter 쳤을 때
def tbox_enter(event):
  label.config(text = tbox.get())

#label
label = tkinter.Label(root, text = '텍스트를 입력하세요')
label.pack()

# 텍스트 상자 생성
tbox = tkinter.Entry(root)
tbox.pack()

# bind
tbox.bind('<Return>', tbox_enter)

root.mainloop()
