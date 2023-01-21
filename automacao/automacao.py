import pyautogui
import pyperclip
import time 
import pandas as pd
pyautogui.PAUSE = 1
#abri o navegador
pyautogui.alert("A automação ira começar\nprecione ok")
pyautogui.press("winleft")
pyautogui.write("Chrome")
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(700, 430, clicks=1)
time.sleep(5)

#entra no drive
pyautogui.click(364, 50, clicks=1)
time.sleep(5)
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)
#download do arquivo 
pyautogui.click(384, 324, clicks=2)
pyautogui.click(384, 324, clicks=1)
time.sleep(2)
pyautogui.click(1137, 200, clicks=1)
pyautogui.click(924, 642, clicks=1)
time.sleep(10)
pyautogui.click(680, 506, clicks=1)
#mexendo no arquivo 
df = pd.read_excel(r"C:\Users\Cliente\Downloads\Vendas - Dez.xlsx")




pyautogui.alert("A automação acabou\nprecione ok")



