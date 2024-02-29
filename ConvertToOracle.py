import tkinter.messagebox as msgbox
from tkinter import *
import clipboard

def btnPaste():
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
    strCompText = '(' + strCompText[2:] + ')'
    clipboard.copy(strCompText)
    msgbox.showinfo('알림', '복사되었습니다.')


# 루트화면 (root window) 생성
root = Tk()
root.geometry("100x100")
root.resizable(False, False)
root.title("오라클 IN절")

frame = Frame(root)
frame.pack()

objScrollBar = Scrollbar(frame)
objTextArea = Text(frame, width=280, height=4)
objScrollBar.pack(side=RIGHT, fill=Y)
objTextArea.pack(side=LEFT, fill=Y)
objScrollBar.config(command=objTextArea.yview)
objTextArea.config(yscrollcommand=objScrollBar.set)

objPasteButton = Button(root, text="붙여넣기", command=btnPaste)
objPasteButton.pack()

objConvertButton = Button(root, text="변환", command=btnConvert)
objConvertButton.pack()



# 4. 메인루프 실행
root.mainloop()