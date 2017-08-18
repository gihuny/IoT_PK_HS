import tkinter
root = tkinter.Tk()

def radio_b1():
  label.config(text = '버튼1')

def radio_b2():
  label.config(text = '버튼2')

sel = tkinter.IntVar()
sel.set(1)

#label
label = tkinter.Label(root, text='버튼 선택')
label.pack()

#라디오 버튼 1 생성
rb1 = tkinter.Radiobutton(root, text = '선택버튼1', variable = sel, value = 1, command = radio_b1)

#라디오 버튼 1 배치
rb1.pack()

#라디오 버튼 2 생성
rb2 = tkinter.Radiobutton(root, text = '선택버튼2', variable = sel, value = 2, command = radio_b2)

#라디오 버튼 2 배치
rb2.pack()

#root 표시
root.mainloop()

