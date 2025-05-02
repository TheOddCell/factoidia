#!/usr/bin/python3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import requests
import json
import sys
 
genai=True
aiMenu=True
extras=True
if genai:
    del genai
    from google import genai
    aiOn=True
    key=open("api.txt", "r")
    client = genai.Client(api_key=key.read())
    key.close()
else:
    aiOn=False
 
 
def ai(ask):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=ask,
    )
    return response.text
 
uselessFacts="https://uselessfacts.jsph.pl/api/v2/facts/random"
techy="https://techy-api.vercel.app/api/text"
nooois="https://api.chucknorris.io/jokes/random"
excuse="https://excuser-three.vercel.app/v1/excuse"
mewo="https://meowfacts.herokuapp.com/"
kanyo="https://api.kanye.rest/"
 
def extractExcuse(input):
    #return re.search(input,r"[^:\\\"]+").group()
    return json.loads(input)[0]['excuse']
 
buttonTexts=["Create new fact", "Create new techy system", "Create new Chuck Norris Joke", "Create new Excuse", "Create new Cat Info Thing","Create new Kanye West Quote", "Create EVERYTHING"]
titleTexts=["Factoidia","Factoidia","Factoidia","Factoidia","Factoidia","Factoidia","Factoidia"]
#root = tk.Tk()
root = Window(themename="darkly")
frm = ttk.Frame(root, padding=0)
#root.config(font=("Arial", 25))
frm.grid()
root.title(titleTexts[0])
factAreaText = StringVar(frm, "Please create a new fact.")
factArea=Label(frm, textvariable=factAreaText).grid(column=0, row=0)
root.resizable(False, False)
 
 
#default_font = tkFont.nametofont("TkDefaultFont")
#default_font.configure(size=30)
 
idk=0
buttonText=StringVar(frm, buttonTexts[0])
#buttonTexts=["Fact, New\" Create",                  "Message Create's Techy",       "Chuck! create",    "Excuse??",                  "Mewo!",         "Chcuck Tecy Facto Create excuse? with mewo"    , "WARNING: AI LOOP. USE EVERY ONE HOUR."]
 
#titleTexts=["Factoid Normal, Totaly. Generator\"", "Techy, Help Normal Generator", "Norris Generator", "Party, buck I am Genrator", "Mewo Genrator", "Tech, Factoid Chuck Excuse Generator with mewo", "AI. AI, AI AI, AI!"]
if aiOn and aiMenu:
    aibuttonvalue = tk.BooleanVar()
    aibutton=Checkbutton(frm, text='AI mode', bootstyle="danger-square-toggle", variable=aibuttonvalue).grid(column=0, row=2)
    aibuttonvalue.set(True)
    extrabuttonvalue = tk.BooleanVar()
    extrabutton=Checkbutton(frm, text='Extras', bootstyle="warning-square-toggle", variable=extrabuttonvalue).grid(column=1, row=2)
    extrabuttonvalue.set(True)
    baibuttonvalue = tk.BooleanVar()
    baibutton=Checkbutton(frm, text='Good AI mode', bootstyle="info-square-toggle", variable=baibuttonvalue).grid(column=0, row=3)
    baibuttonvalue.set(False)
 
 
def newfact(set=True):
    extras=aibuttonvalue.get()
    hi=""
    msg=""
    if set:
        factAreaText.set("Building...")
    j=0
    for i in range(100):
        j=j+1
        if j==6:                                
            j=0
        try:
            if idk==0:
                ddd=json.loads(requests.get(uselessFacts).text)["text"]
            elif idk==1:
                ddd=requests.get(techy).text
            elif idk==2:
                ddd=json.loads(requests.get(nooois).text)["value"]
            elif idk==3:
                ddd=extractExcuse(requests.get(excuse).text)
            elif idk==4:
                ddd=json.loads(requests.get(mewo).text)["data"][0]
            elif idk==5:
                ddd=json.loads(requests.get(kanyo).text)["quote"]
            elif idk==6:
                if j==0:
                    ddd=json.loads(requests.get(uselessFacts).text)["text"]
                elif j==1:
                    ddd=requests.get(techy).text
                elif j==2:
                    ddd=json.loads(requests.get(nooois).text)["value"]
                elif j==3:
                    ddd=extractExcuse(requests.get(excuse).text)
                elif j==4:
                    ddd=json.loads(requests.get(mewo).text)["data"][0]
                elif j==5:
                    ddd=json.loads(requests.get(kanyo).text)["quote"]
            if i+1<10:
                coollookingi=" "+str(i+1)
            else:
                coollookingi=str(i+1)
            if idk==6:
                print(coollookingi, ddd, j)
                msg=msg+f"{coollookingi} {ddd} {j}\n"
            else:
                print(coollookingi, ddd)
                msg=msg+f"{coollookingi} {ddd}\n"
            hi=hi+ddd.split(" ")[i]+" "
            if set:
                factAreaText.set("Building... "+hi)
        except:
            break
    print()
    if aiMenu:
        if aiOn and aibuttonvalue.get():
            if baibuttonvalue.get():
                msg=msg+f"\nPreAI:  {hi}\n"
                print(f"PreAI:  {hi}")
                hi=ai(f"Rearrange the following jumble of words to make sense. You may add or remove words, but only do so if else the sentance would not be grammaticly correct, something that the output should be. Please do not respond anything more then the modified jumble. The words are the following:    {hi}")
                print(f"PostGoodAI: {hi}")
                msg=msg+f"PostGoodAI: {hi}\n"
            else:
                msg=msg+f"\nPreAI:  {hi}\n"
                print(f"PreAI:  {hi}")
                hi=ai(f"Rearrange the following jumble of words to make sense. Do not add any new words or change anything other than punctuation. Please do not respond anything more then the modified jumble. The words are the following:    {hi}")
                print(f"PostAI: {hi}")
                msg=msg+f"PostAI: {hi}\n"
        else:
            print(f"Output: {hi}")
            msg=msg+f"Output: {hi}"
    else:
        if aiOn:
            msg=msg+f"\nPreAI:  {hi}\n"
            print(f"PreAI:  {hi}")
            hi=ai(f"Rearrange the following jumble of words to make sense. Do not add any new words or change anything other than punctuation. Please do not respond anything more then the modified jumble. The words are the following:    {hi}")
            print(f"PostAI: {hi}")
            msg=msg+f"PostAI: {hi}\n"
        else:
            print(f"Output: {hi}")
            msg=msg+f"\nOutput: {hi}\n"
    print()
    if set:
        factAreaText.set(hi)
    else:
        return hi[:-1]
    if extrabuttonvalue.get():
        try:
            if sys.argv[1]=="--bro":
                Messagebox.ok(msg[:-3], "Factoidia Extra Info")
            else:
                Messagebox.ok(msg[:-3], "Factoidia Extra Info")
        except:
            Messagebox.ok(msg[:-3], "Factoidia Extra Info")
        print(msg)
    frm.pack()
 
def switch():
    global idk
    idk=idk+1
    if idk==6:
        idk=0
    buttonText.set(buttonTexts[idk])
    root.title(titleTexts[idk])
 
try:
    if sys.argv[1]=="--bro":
        root.wm_attributes('-transparentcolor', '#222222')
except:
    pass
Button(frm, textvariable=buttonText, command=newfact, bootstyle=SUCCESS).grid(column=0, row=1)
if aiOn and aiMenu:
    Button(frm, text="Switch Modes", command=switch, bootstyle=(INFO, OUTLINE)).grid(column=1, row=1)
    #ttk.Button(frm, textvariable=AibuttonText, command=aiswitch).grid(column=0, row=2)
    #Button(frm, text="Quit", command=root.destroy, bootstyle=DANGER).grid(column=1, row=1)
    #root.overrideredirect(True)
else:
    Button(frm, text="Swtich Modes", command=switch).grid(column=1, row=1)
    #Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
#newfact()
frm.pack(fill="both", expand=True, side="left")
 
root.mainloop()
