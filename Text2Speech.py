from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3

print('''
FileName  : Text2Speech
Lang      : Python3
Modules   : tkinter,pyttsx3
Programmer: Pavan Kumar
Github ID : pavkcode
youtube   : Pavk Code
''')
def Speak():
    #Input from the TextArea
    txt = txtArea.get(1.0,END)
    
    #if the combox value is > Male
    if(voiceCombo.get() == "Male"):
        voiceEngine = pyttsx3.init()
        voices = voiceEngine.getProperty('voices')
        voiceEngine.setProperty('voice', voices[0].id)
        
        #if voicecombo is slow , fast , or normal
        if(voiceMode.get() == "Slow"):
            voiceEngine.setProperty('rate', 50)
        elif(voiceMode.get() == "Fast"):
            voiceEngine.setProperty('rate', 350)
        elif(voiceMode.get() == "Normal"):
            voiceEngine.setProperty('rate', 150)

        voiceEngine.say(txt)
        voiceEngine.runAndWait()
    
    #if the combox value is > Female
    elif(voiceCombo.get() == "Female"):
        voiceEngine = pyttsx3.init()
        voices = voiceEngine.getProperty('voices')
        voiceEngine.setProperty('voice', voices[1].id)
        
        #if voicecombo is slow , fast , or normal
        if(voiceMode.get() == "Slow"):
            voiceEngine.setProperty('rate', 50)
        elif(voiceMode.get() == "Fast"):
            voiceEngine.setProperty('rate', 350)
        elif(voiceMode.get() == "Normal"):
            voiceEngine.setProperty('rate', 150)

        voiceEngine.say(txt)
        voiceEngine.runAndWait()    


txt2speech = Tk()
txt2speech.title('Text To Speech')
txt2speech.geometry('600x420')

Label(txt2speech,text="Text - To - Speech",font="Arial 14",foreground="blue").place(x = 210, y=30)

txtArea = Text(txt2speech,width=50,height=15,bg="#505060",fg="red",font="monospace 10")
txtArea.place(x=10,y=100)

Label(txt2speech,text="Filter",font="Arial 15").place(x=485,y = 120)

voiceMode = Combobox(txt2speech,width=10,values=("Fast","Normal","Slow"))
voiceMode.place(x=470, y =  160)
voiceMode.set("Normal")

voiceCombo = Combobox(txt2speech,values=("Male","Female"),width=10)
voiceCombo.place(x = 470,y = 200)
voiceCombo.set("Male")

speakBtn = Button(txt2speech,command=Speak,width= 10,text="Speak")
speakBtn.place(x=470,y=240)

txt2speech.mainloop()
