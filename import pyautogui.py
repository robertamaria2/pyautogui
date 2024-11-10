import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=995, y=406)
pyautogui.hotkey("ctrl+a")
pyautogui.write("robertamariasilva258@gmail.com")
pyautogui.press("tab")
pyautogui.write("robertamaria")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
import pandas
tabela = pandas.read_csv("C:/Users/Roberta Maria/Downloads/Nova pasta/produtos.csv")

for linha in tabela.index:   
    


    pyautogui.click(x=1013, y=289)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

if not pandas.isna(tabela.loc[linha, "obs"]):
    pyautogui.write(str(tabela.loc[linha, "obs"]))
pyautogui.scroll(5000)
pyautogui.press("tab")  
pyautogui.press("enter") 
