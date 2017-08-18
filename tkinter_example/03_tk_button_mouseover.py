import tkinter

# object instance creation
# 객체 인스턴스 생성
root = tkinter.Tk()

# button 처리함수
def button():
#  print("버튼눌림")
  label.config(text="버튼눌림")

# button 마우스오버 함수
def button_mouseover(event):
  label.config(text='어디가!')

# 라벨 생성
label = tkinter.Label(root, text='라벨')

# 라벨 배치
label.pack()

# button 생성
button = tkinter.Button(root, text='버튼', command=button)

# 버튼배치
button.pack()  

# 마우스오버 이벤트 추가
button.bind('<Leave>', button_mouseover)

# root 표시
root.mainloop()
