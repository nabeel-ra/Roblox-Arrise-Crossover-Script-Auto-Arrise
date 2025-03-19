import pyautogui as pyg
import time

attack_button_imgpath = r"C:\Users\Nabell\Desktop\FUN\attack_pic.png"


while(True):
  attack_button = pyg.locateCenterOnScreen(attack_button_imgpath, confidence=0.5)
  if attack_button is not None:
    pyg.click(attack_button)
    time.sleep(2)