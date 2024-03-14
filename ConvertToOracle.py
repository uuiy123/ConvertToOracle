from tkinter import *
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import clipboard
import os
#from tkinter import Frame, Button, Text, Label, Checkbutton, Scrollbar

def alert(strMsg):
    msgbox.showinfo('알림', strMsg)
## 붙여넣기
def btnPaste():
    ## 초기화
    objTextArea.delete(0.0, 'end')
    ## 붙여넣기
    result = clipboard.paste()
    result = result.replace("\r", "")
    result = result.replace("\t", "")
    objTextArea.insert(INSERT, result)

## 변환부분
def btnConvert():
    strText = objTextArea.get(1.0, "end")
    arText = strText.split()

    strCompText = ""
    for x in arText:
        strCompText += ", '" + x + "'"
        
        if (CheckVal2.get() == 1) :
            strCompText += "\n"
    strCompText = '(' + strCompText[2:] + ')'
    clipboard.copy(strCompText)
    alert('복사되었습니다.')

## alpha는 창의 투명도를 설정함, 1은 투명도0, 0은 완전 투명
def slide(_):
    root.attributes('-alpha', objSlideBar.get())
    #slide_label.config(text=str(round(objSlideBar.get(), 2)))

def changewindowstop():

    if CheckVal1.get() == 1:
        root.wm_attributes("-topmost", 1)
    else:
        root.wm_attributes("-topmost", 0)

# 루트화면 (root window) 생성
root = tk.Tk()

## 화면구성

## aplication을 프레임 설정하여 각 obj를 배치할수 있게 틀을 잡아준다.
frame1 = Frame(root)
frame1.pack(side="top")
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack(pady=3)

## SCROLLBAR와, TEXTAREA 객체 배치
objScrollBar = Scrollbar(frame1)
objTextArea = Text(frame1, width=280, height=10)
objScrollBar.pack(side="right", fill=Y)
objTextArea.pack(side="left", fill=Y)
objScrollBar.config(command=objTextArea.yview)
objTextArea.config(yscrollcommand=objScrollBar.set)

## 복사, 변환, 항상위에 객체 배치
objPasteButton = Button(frame2, text="붙여넣기", command=btnPaste)
objPasteButton.pack(side="left")

objConvertButton = Button(frame2, text="변환", command=btnConvert)
objConvertButton.pack(side="left")

CheckVal1 = tk.IntVar()
objTopChkButton = Checkbutton(frame2, text="항상위에", variable=CheckVal1, command=changewindowstop)
objTopChkButton.pack(side="left")

CheckVal2 = tk.IntVar()
obVertical = Radiobutton(frame3, text="세로", variable = CheckVal2, value="1")
obVertical.pack(side="right")
obHorizontal = Radiobutton(frame3, text="가로", variable = CheckVal2, value="0")
obHorizontal.pack(side="right")

## 투명도 조절 객체 배치
objSlideLabel = Label(frame4, text='투명도 레벨')
objSlideLabel.pack(side="left")
objSlideBar = ttk.Scale(frame4, from_=0.1, to=1.0, value=1, orient=HORIZONTAL, command=slide)
objSlideBar.pack(side="left")

root.geometry("200x230")
root.resizable(False, False)
root.title("오라클 IN 키워드")
root.attributes('-alpha', 1)
# 4. 메인루프 실행
root.mainloop()