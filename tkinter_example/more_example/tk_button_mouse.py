import tkinter
import time

# object instance creation
# 객체 인스턴스 생성
root = tkinter.Tk()

# button 처리함수
def button():
#  print("버튼눌림")
#  label.config(text="버튼눌림")
  label.config(text='좌클릭 끝!')

# button 마우스오버 함수
def button_mouseover(event):
  label.config(text='어디가!')

def button_leftmouseclick(event):
  label.config(text='좌클릭!')
def button_middlemouseclick(event):
  label.config(text='가운데클릭!')
def button_rightmouseclick(event):
  label.config(text='우클릭!')

def button_leftrelease(event):
  label.config(text='좌클릭 끝!')
def button_middlerelease(event):
  label.config(text='가운데클릭 끝!')
def button_rightrelease(event):
  label.config(text='우클릭 끝!')

def button_leftmousedbclick(event):
  label.config(text='더블클릭_좌!')
def button_middlemousedbclick(event):
  label.config(text='더블클릭_중!')
def button_rightmousedbclick(event):
  label.config(text='더블클릭_우!')

def button_leftmotion(event):
  label.config(text='좌클릭 이동!')
def button_middlemotion(event):
  label.config(text='가운데클릭 이동!')
def button_rightmotion(event):
  label.config(text='우클릭 이동!')

# 라벨 생성
label = tkinter.Label(root, text='라벨')

# 라벨 배치
label.pack()

# button 생성
button = tkinter.Button(root, text='버튼', command=button)

# 버튼배치
button.pack()  

# 마우스 이벤트 추가
button.bind('<Leave>', button_mouseover)
button.bind('<Button-1>', button_leftmouseclick)
button.bind('<Button-2>', button_middlemouseclick)
button.bind('<Button-3>', button_rightmouseclick)
button.bind('<ButtonRelease-1>', button_leftrelease)
button.bind('<ButtonRelease-2>', button_middlerelease)
button.bind('<ButtonRelease-3>', button_rightrelease)
button.bind('<Double-Button-1>', button_leftmousedbclick)
button.bind('<Double-Button-2>', button_middlemousedbclick)
button.bind('<Double-Button-3>', button_rightmousedbclick)
button.bind('<B1-Motion>', button_leftmotion)
button.bind('<B2-Motion>', button_middlemotion)
button.bind('<B3-Motion>', button_rightmotion)


# root 표시
root.mainloop()
