import tkinter

# object instance creation
# 객체 인스턴스 생성
root = tkinter.Tk()

# button 처리함수
def button():
  print("버튼눌림")

# button 생성
button = tkinter.Button(root, text='버튼', command=button)

# 버튼배치
button.pack()  

# root 표시
root.mainloop()
