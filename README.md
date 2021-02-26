Original repo was from https://github.com/prashanth-up/Zoom-Automation and it's modified for Buet CSE-16 only


## Requirements 
- [x] Installed python version above 3.5
- [x] Installed pyautogui package
- [x] Installed schedule package
- [X] Install or upgrade pillow pckg
- [x] Updated Zoom Software (Signed in)


#### To install the above packages :
+ To [Download Python](https://www.python.org/downloads/)
+ pip install pyautogui
+ pip install schedule
+ pip install Pillow --upgrade
+ To [Download Zoom Software](https://zoom.us/download#client_4meeting)


# How to run the program :
##### Clone this repository and unzip it

* Right click to edit the run.bat and set the paths
  * First Path - "Path to where python is located"
  * Second Path - "Path to where the main.py is located" 

* Open zoom , take ss and crop the 'join' button . Then rename it with "JoinIMG.png" & replace in this folder (see the existing joinIMG file in this folder)

* Make sure the `joinING.png` is located in the same folder as `main.py` and `run.bat`

* Run the `run.bat` to run the batch file (Alternatively you can also run the `main.py` for the same result but `run.bat` is preferred)

* Finally see the routine then enter course no.(format. 405/475) & day( format. sat/wed/sun)

* Your zoom should run in bg, logged in.Plug in your pc and change the power option to "Never sleep".



#Trouble shoot :

* If error occurs check if pyatogui and pillow pck is updated

* check if zoom is updated





