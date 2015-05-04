--------------------
* ROADBOT SOFTWARE *
--------------------


INTRODUCTION
------------

When run, this code will load images of road signs from Campics folder and use template matching 
with frames captured through a webcam video stream. If a sign is found in the video feed frame a 
serial command is sent to the arduino instructing the robot to move in a certain direction.


REQUIREMENTS
------------

* Python 2.7 (https://www.python.org/downloads/)
	
  Required Python libraries:

  - serial					
  - numpy                        
  - matplotlib          
  - time
  

* Arduino IDE (http://www.arduino.cc/en/main/Software)

* Campics library:

  - This library is included in the repository. The RoadbotCompleter.py should be run in the same
    folder as the stock road sign pictures.


RECOMMENDED MODULES
-------------------

* PyCharm Code Editor (https://www.jetbrains.com/pycharm/download/):
  User friendly Python IDE that allows for search and direct download of necessary libraries 

  - Go to File >> Settings >> Project Interpreter 
  - Look for necessary libraries by typing in the search bar or clicking the green '+' symbol


OPERATING INSTRUCTIONS
----------------------

* Connect USB to Arduino serial port 
 
* Open the MtrCtrComplete.ino file in the Arduino IDE

* Verify and run the MtrCtrComplete.ino file in the Arduino IDE by using the checkmark and arrow icons

* Run the RoadbotCompleter.py file in the Python IDE

* Verify there are no errors and that the webcam display has appeared on the monitor

* Robot is ready to recieve visual cues


TROUBLESHOOTING
---------------

* The turn delay will probably have to be adjusted when switching computers, as this is processor dependent.
  Not doing so may result in turns that are slightly above or below 90 degrees.

* In Python IDE, run RoadbotCompleter.py 

* In line 57 of ("while (i<=9015000):") change the number up or down smaller increments initially, then larger 
  increments until a satisfactory turn radius is achieved. This may require several test runs.

* If the software is not detecting signs correctly, new reference images may need to be taken specific to
  the robot's current environment.

AUTHORS
-------

Group12 -Nathaniel Jackson, Jerrod Rout, Blake Taylor, Akash Patel
