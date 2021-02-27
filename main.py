# Made By Prashanth Umapathy
# Specialises is Laziness

# Libraries imported
import pyautogui 
import schedule 
import time 

# User Inputs





print('\n\n        Routine(HCI+ HPDS):\n')
print('         09:00        10:00         11:00         12:00')
print('Sat:  409/Graphics      -          425/HCI       475/Econ\n')
print('Sun:  453/HPDS      405/Security   425/HCI       475/Econ\n')
print('mon:  453/HPDS      405/Security   425/HCI       409/Graphics\n')
print('tue:  453/HPDS          -              -             -   \n')
print('wed:  405/Security      -          409/Graphics  475/Econ\n\n')

course_no = input('Enter Course No. (e.g. 405 / 475)')
day_var = input('Enter day (e.g. mon/wed): ')
meet_time = ""
meet_id = ""
password = ""
if course_no == '453':
	meet_id = '  '
	password = '  '
	meet_time='09:00'
	print("id %s"%meet_id)
	print("pass %s"%password)
	print("time %s"%meet_time)
elif course_no == '405':
	if day_var == 'wed' :
	 	meet_id = '64689450739'
	 	password = '405000'
	 	meet_time='09:00'
	 	print("id %s"%meet_id)
	 	print("pass %s"%password)
	 	print("time %s"%meet_time)
	else : 
	 	meet_id = '64689450739'
	 	password = '405000'
	 	meet_time='10:00'
	 	print("id %s"%meet_id)
	 	print("pass %s"%password)
	 	print("time %s"%meet_time)
elif course_no == '409':
	if day_var == 'sat' :
	 	meet_id = '62457340769'
	 	password = '380007'
	 	meet_time='09:00'
	 	print("id %s"%meet_id)
	 	print("pass %s"%password)
	 	print("time %s"%meet_time)
	elif day_var == 'mon' : 
	 	meet_id = '62457340769'
	 	password = '380007'
	 	meet_time='12:00'
	 	print("id %s"%meet_id)
	 	print("pass %s"%password)
	 	print("time %s"%meet_time)
	elif day_var == 'wed' :
	 	meet_id = '62457340769'
	 	password = '380007'
	 	meet_time='11:00'
	 	print("id %s"%meet_id)
	 	print("pass %s"%password)
	 	print("time %s"%meet_time)	 		
elif course_no == '425': 
	 meet_id = '67578331133'
	 password = '979274'
	 meet_time='11:00'
	 print("id %s"%meet_id)
	 print("pass %s"%password)
	 print("time %s"%meet_time)	
elif course_no == '475': 
	 meet_id = ' '
	 password = ' '
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
