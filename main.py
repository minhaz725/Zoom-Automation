# Made By Prashanth Umapathy
# Specialises is Laziness

# Libraries imported
import pyautogui 
import schedule 
import time 

# User Inputs





print('\n\n        Routine:\n')
print('      09:00  10:00  11:00  12:00')
print('Sat:         eun           mah\n')
print('Sun:         eun           alm\n')
print('mon:  kms    adn              \n')
print('tue:  sho                  mah\n')
print('wed:  kms    adn              \n\n')

teacher_name = input('Enter Teacher Name(e.g. kms / adn) according to correct day (e.g. kms for mon/wed , alm for sun): ')

meet_time = ""
meet_id = ""
password = ""
if teacher_name == 'adn':
	meet_id = '66958617778'
	password = 'cse301'
	meet_time='10:00'
	print("id %s"%meet_id)
	print("pass %s"%password)
	print("time %s"%meet_time)
elif teacher_name == 'kms': 
	 meet_id = '4766692101'
	 password = '635467'
	 meet_time='09:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)
elif teacher_name == 'mah': 
	 meet_id = '7998110539'
	 password = '121121'
	 meet_time='12:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)	
elif teacher_name == 'eun': 
	 meet_id = '9232649477'
	 meet_time='10:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)
elif teacher_name == 'sho': 
	 meet_id = '66259669588'
	 password = '321000'
	 meet_time='09:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)
elif teacher_name == 'alm': 
	 meet_id = '6236249969'
	 password = '547161'
	 meet_time='12:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)	 
else: print('invalid course')	 
	 	 

total_meet = '50'


#just for confirmation
total_meet = int(total_meet)
meet_time = str(meet_time)

# Where the Magic happens function
def zoomClass():
    time.sleep(0.2)

    pyautogui.press('esc',interval=0.1)
    
    time.sleep(0.3)

    pyautogui.press('win',interval=0.5)
    pyautogui.write('zoom')
    pyautogui.press('enter',interval=0.5)

    time.sleep(10)

    x,y = pyautogui.locateCenterOnScreen('joinIMG.png')
    """
    # x,y = pyautogui.locateCenterOnScreen('joinIMG.png', confidence = 0.9)
    # Uncomment ln 49 and comment ln 47 
    # if you get an 'TypeError: cannot unpack non-iterable NoneType object' error
    """
    pyautogui.click(x,y)


    pyautogui.press('enter',interval=5)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=5)

    pyautogui.write(password)
    pyautogui.press('enter',interval = 10)

    print("Session has started and will continue for %s minutes"%total_meet)

    print('Hold (Ctrl+c) to exit the program ')

    #Total time of zoom session
    time.sleep(total_meet) 

    # closing Zoom
    os.system("TASKKILL /F /IM Zoom.exe")
    time.sleep(0.5)


# Every day at whatever time the user has entered.
schedule.every().day.at("%s"%meet_time).do(zoomClass)
print("Scheduling class at ",meet_time)

# Infinite Loop so that the scheduled task keeps running
while True: 

	# Check whether a scheduled task is pending to run or not
	schedule.run_pending() 
	time.sleep(1) 

# Main Func
# if __name__ == "__main__":
    # zoomClass()
