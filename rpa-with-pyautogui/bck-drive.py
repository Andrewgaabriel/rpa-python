import pyautogui
import time

# LISTA TODAS AS TECLAS QUE EU POSSO PRESSIONAR
# pyautogui.KEYBOARD_KEYS
# MOSTRA A POSIÇÃO DO MOUSE
# pyautogui.position()


pyautogui.alert('Automação em andamento, pressione "OK" e aguarde!') # alerta o uso da automação
pyautogui.PAUSE = 0.5   # cria um intervalo entre cada procedimento



# Abrir o google drive no meu computador

pyautogui.press('winleft')  # pressiona a tecla do windows
pyautogui.write('chrome')   # digita chrome
pyautogui.press('enter')    # pressiona enter
time.sleep(1)   # espera 1 segundo
pyautogui.write('https://drive.google.com/drive/u/0/my-drive') # digita o endereço do google drive
pyautogui.press('enter')    # pressiona enter



# Entrar na área de trabalho

pyautogui.hotkey('winleft', 'd')    # abre a área de trabalho com WINDOWS + D
pyautogui.moveTo(x=1863, y=36)      # move o mouse para a posição
pyautogui.mouseDown()               # pressiona o botão esquerdo do mouse
pyautogui.moveTo(x=979, y=611)      # move o mouse para a posição 
pyautogui.hotkey('alt','tab')       # pressiona a tecla ALT + TAB
time.sleep(1)                       # espera 1 segundo
pyautogui.mouseUp()                 # solta o botão esquerdo do mouse


time.sleep(5)
pyautogui.alert('Automação concluida!') # alerta o fim do uso da automação