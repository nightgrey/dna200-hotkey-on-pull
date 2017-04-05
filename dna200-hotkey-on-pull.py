"""
  "dna200-hotkey-on-pull"
  
  Documentation: https://github.com/nightgrey/dna200-hotkey-on-pull
  
  Credits:
   - Idea and original script: /u/sirus20x6's
     https://www.reddit.com/r/electronic_cigarette/comments/4pw6kq/python_script_to_mute_your_skype_mice_when_you/
    
  Links
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms646273(v=vs.85).aspx
    https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py
    http://docs.activestate.com/activepython/2.7/pywin32/PyWin32.HTML
    https://social.technet.microsoft.com/wiki/contents/articles/5169.vbscript-sendkeys-method.aspx
"""

import serial
from time import sleep
import sys
import win32com.client


"""
User-specific configuration
"""
# Connect your DNA200 via USB. Get the port name from "Windows device manager"
portName = "COM4" 

# Hotkey(s) to trigger
# Doc(s):
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
# http://social.technet.microsoft.com/wiki/contents/articles/5169.vbscript-sendkeys-method.aspx
hotkey = "^m" # ^m = STRG+M

# Sleep time between checks
timeBetweenChecks = 0.1

# Activate/deactivate development logs
development = False


"""
Globals
"""
# win32com client
win32 = win32com.client.Dispatch("WScript.Shell")

# Serial connection
serialConnection = serial.Serial()
serialConnection.baudrate = 9600
serialConnection.port = portName
serialConnection.timeout = 10


"""
Check if DNA200 is connected
"""
def isConnected():
    try:
        return self.ser.isOpen()
    except:
        return False


"""
Defines main loop to monitor the serial connection and execute the keypress
"""
def monitorConnection():
    # Define last action
    lastActionWasADraw = False
    
    while 1:
        # Read input
        serialInput = serialConnection.readline()
            
        if serialInput.find("?") == -1:
            if lastActionWasADraw is False:
              win32.SendKeys(hotkey, 0)
              lastActionWasADraw = True
              
              # Development log
              if development is True:
              	print "Trigger keypress: 'drawing'"
              else:
                print "Muted."
            
            # Development log
            if development is True:
            	print "Signal: drawing!"
        else:
            if lastActionWasADraw is True:
                win32.SendKeys(hotkey, 0)
                lastActionWasADraw = False
                
                # Development log
                if development is True:
                    print "Trigger keypress: 'not drawing'"
                else:
                    print "Unmuted."
        	
            # Development log
            if development is True:
                print "Signal: Not drawing!"
        
        #  Sleep
        sleep(timeBetweenChecks)
        
        # Write I=GET (???)
        # TODO: Look up what this does.
        serialConnection.write('I=GET\r\n')
        
        # Development log
        if development is True:
        	print serialInput


"""
Initialize!
"""
serialConnection.open()

# Start monitoring if serial connection was established.
if serialConnection.isOpen():
    #if isConnected is True
        print 'Serial connection established. Port: ' + serialConnection.portstr
        
        # Write I=GET
        # TODO: Understand what this does and if it's required. I just copied it
        # from the original script.
        serialConnection.write('I=GET\r\n')
        
        # Start monitoring.
        monitorConnection()
    #else
    #    print 'Serial connection closed.'
else:
    print 'An error occured. The serial connection could not be established.'
    #serialConnection.close()
