import pyautogui as pg  
import time
Text = input("What do you want to spam? ")

try:
  times= int(input("How many times? (input a number) ")) 
except ValueError:
    print("Input a valid number")
    exit()

check = input("Press Enter/Return to execute...")
print("\n You have 5 seconds to focus the field you want to spam in")
time.sleep(5)

for i in range(times):
    pg.write(Text)
    pg.press("Enter")
print(f"Done! Sent {Text} ",f"{times} times")