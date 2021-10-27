import pyautogui
import keyboard
import time
import random
import win32api , win32con

ag=va=bt=tps=se1=se2=se3=sub=tp=cha=0
vara=str(input("posicione seu mouse e digite v para marcar posicao da vara: "))
if vara == "v":
    va=pyautogui.position()
agua=str(input("posicione seu mouse e digite l para marcar posicao na agua: "))
if agua == "l":
    ag  = pyautogui.position()  
battle=str(input("posicione seu mouse e digite b para marcar posicao do target: "))
if battle == "b":
    bt=pyautogui.position()
tpe=str(input("posicione seu mouse e digite t para marcar posicao do poke de tp:"))
if tpe == "t":
    tps= pyautogui.position()

querpoke=str(input("Quer usar o modo de substituir pokemon quando o seu morrer?  S/N"))
if querpoke.upper() == "S":
    seg1=str(input("posicione seu mouse e digite s1 para marcar outro poke caso o seu morra 1: "))
    if seg1 == "s1":
        se1=pyautogui.position()
    seg2=str(input("posicione seu mouse e digite s2 para marcar outro poke caso o seu morra 2: "))
    if seg2 == "s2":
        se2=pyautogui.position()
    seg3=str(input("posicione seu mouse e digite s3 para marcar outro poke caso o seu morra 3: "))
    if seg3 == "s3":
        se3=pyautogui.position()
    sub=1


chat=[]

for ce in range(3):
    chat.append(input("Digite coisas para falar no chat: "))
viuda=0
while keyboard.is_pressed("c") == False:
    win32api.SetCursorPos((va))
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.5)
    win32api.SetCursorPos((ag))
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.5)
    c=0
    
    while c == 0:
        c=0
        if pyautogui.locateOnScreen("peixeverde.PNG"):
            pyautogui.moveTo("peixeverde.PNG")
            pyautogui.click("peixeverde.PNG")
            pyautogui.moveTo(bt,duration=0.1)
            pyautogui.click(bt)
            pyautogui.press("f1")
            pyautogui.press("f2")
            pyautogui.press("f3")
            pyautogui.press("f4")
            pyautogui.press("f5")
            pyautogui.press("f6")
            pyautogui.press("f7")
            pyautogui.press("f8")
            pyautogui.press("f9")
            pyautogui.press("f10") 
            c=1
            break
            
        if pyautogui.locateOnScreen("chat.PNG"):
            pyautogui.press("tab")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(0.5)
            if cha == 0:
                pyautogui.write(chat[0])
            if cha == 1:
                pyautogui.write(chat[1])
            if cha == 2:
                pyautogui.write(chat[2])
            time.sleep(1)
            pyautogui.press("enter")
            pyautogui.press("tab")
            tp+=1
            time.sleep(0.5)
            pyautogui.press("f1")
            pyautogui.press("f2")
            pyautogui.press("f3")
            pyautogui.press("f4")
            pyautogui.press("f5")
            pyautogui.press("f6")
            pyautogui.press("f7")
            pyautogui.press("f8")
            pyautogui.press("f9")
            pyautogui.press("f10")
            win32api.SetCursorPos((va))
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(0.5)
            win32api.SetCursorPos((ag))
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(0.5)
            c=1
            cha+=1
            break
        if tp == 2:
            pyautogui.moveTo(tps)
            pyautogui.click(tps)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.write("!teleport singer")
            time.sleep(1)
            pyautogui.press("enter")
            cha=0
            
            quer=str(input("quer continua?"))
            tp=0
        if sub == 1:
            if pyautogui.locateOnScreen("vida.PNG"):
                if viuda==0:
                    pyautogui.moveTo(se1)
                    time.sleep(0.3)
                    pyautogui.click(se1)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    win32api.SetCursorPos((va))
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    time.sleep(0.5)
                    win32api.SetCursorPos((ag))
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    time.sleep(0.5)
                    break

                elif viuda==1:
                    pyautogui.moveTo(se2)
                    time.sleep(0.3)
                    pyautogui.click(se2)
                    viuda+=1
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")
                    win32api.SetCursorPos((va))
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    time.sleep(0.5)
                    win32api.SetCursorPos((ag))
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    time.sleep(0.5)
                    break
                elif viuda==2:
                    pyautogui.moveTo(tps)
                    time.sleep(0.5)
                    pyautogui.click(tps)
                    pyautogui.press("enter")
                    time.sleep(0.5)
                    pyautogui.write("!teleport singer")
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    time.sleep(0.5)
                    pyautogui.press("f1")
                    pyautogui.press("f2")
                    pyautogui.press("f3")
                    pyautogui.press("f4")
                    pyautogui.press("f5")
                    pyautogui.press("f6")
                    pyautogui.press("f7")
                    pyautogui.press("f8")
                    pyautogui.press("f9")
                    pyautogui.press("f10")  
                    viuda=0
                    cha=0
                    quer=str(input("quer continua?"))
                    





    
        
        
        
   
