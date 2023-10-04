import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import sys

pause_flag = False
bet = 0
freq = 0
waittimer = 0
original_stdout = sys.stdout
def getFreq():
    global freq
    freq = e.get()

def setWaitTimer():
    global waittimer
    waittimer = e_wait_timer.get()

def getBet1():
    global bet
    bet = 1


def getBet2():
    global bet
    bet = 2


def getBet3():
    global bet
    bet = 3


def getBet4():
    global bet
    bet = 4


def getBet5():
    global bet
    bet = 5


def getBet6():
    global bet
    bet = 6


def getBet7():
    global bet
    bet = 7


def getBet8():
    global bet
    bet = 8


def getBet9():
    global bet
    bet = 9

conv1 = 960
conv0 = 0

# Specify the path to the text file where you want to save the console output
output_file_path = 'ref/console_output.txt'
output_file = None  # Global variable to store the file object

class DualOutput:
    def __init__(self, *outputs):
        self.outputs = outputs

    def write(self, text):
        for output in self.outputs:
            output.write(text)

    def flush(self):
        pass  # You can implement flush if needed


def redirect_output_to_file():
    global output_file
    # Open the file in append mode
    output_file = open(output_file_path, 'a')

    # Redirect standard output to both the console and the file
    sys.stdout = DualOutput(sys.stdout, output_file)

    # Optionally, you can redirect standard error as well
    sys.stderr = DualOutput(sys.stderr, output_file)

def restore_original_output():
    global output_file
    # Close the file explicitly before restoring the original standard output
    if output_file:
        output_file.close()
    sys.stdout = original_stdout
    sys.stderr = sys.__stderr__


    
def Green_Arrow_Right(n):
    for i in range(0,n):
        time.sleep(0.2)
        pyautogui.click(840 + conv1,355)
        time.sleep(0.2)
        pyautogui.click(840 + conv0,355)

def Green_Arrow_Left(n):
    for i in range(0,n):
        time.sleep(0.5)
        pyautogui.doubleClick(320 +  conv1,350)
        time.sleep(0.2)
        pyautogui.doubleClick(320 + conv0, 350)
        

def Amount_Selection(bet):
    if bet == 1:
        pyautogui.click(461 + conv1, 287)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(461 + conv0, 287)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 2:
        pyautogui.click(576 + conv1, 284)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(576 + conv0, 284)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 3:
        pyautogui.click(693 + conv1, 286)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(693 + conv0, 286)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 4:
        pyautogui.click(453 + conv1, 338)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(453 + conv0, 338)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 5:
        pyautogui.click(576 + conv1, 340)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(576 + conv0, 340)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 6:
        pyautogui.click(699 + conv1, 336)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(699 + conv0, 336)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 7:
        pyautogui.click(447 + conv1, 393)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(447 + conv0, 393)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 8:
        pyautogui.click(576 + conv1, 392)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(576 + conv0, 392)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)
    elif bet == 9:
        pyautogui.click(701 + conv1, 387)  # 457 + conv0, 290 for the 100 bet
        time.sleep(0.2)
        pyautogui.click(701 + conv0, 387)  # 701+conv0, 385 for the 10m bet
        time.sleep(0.5)


def check_for_cross():
    if pyautogui.locateOnScreen('ref/ext1.png', region=(814 + conv1, 188, 30, 30), grayscale=True,
                                    confidence=0.45) != None:
        pyautogui.click(823 + conv1, 202)
        time.sleep(0.2)
    
    if pyautogui.locateOnScreen('ref/ext1.png', region=(814 + conv0, 188, 30, 30), grayscale=True,
                                confidence=0.45) != None:
        pyautogui.click(823 + conv0, 202)
        time.sleep(0.2)
    
    #Starter Pack Offer
    # if pyautogui.locateOnScreen('ref/ext1.png', region=(814 + conv1, 180, 30, 35), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(823 + conv1, 202)
    #     time.sleep(0.2)
    
    # if pyautogui.locateOnScreen('ref/ext1.png', region=(814 + conv0, 180, 30, 35), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(823 + conv0, 202)
    #     time.sleep(0.2)

    #find out
    # if pyautogui.locateOnScreen('ref/xnoubutton.png', region=(775 + conv0, 200, 30, 30), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(783 + conv0, 210)
    #     time.sleep(0.2)
    
    # if pyautogui.locateOnScreen('ref/xnoubutton.png', region=(775 + conv1, 200, 30, 30), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(783 + conv1, 210)
    #     time.sleep(0.2)
    
    # if pyautogui.locateOnScreen('ref/xbutton.png', region=(830 + conv0, 195, 25, 25), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(840 + conv0, 200)
    #     time.sleep(0.2)
    
    # if pyautogui.locateOnScreen('ref/xbutton.png', region=(830 + conv1, 195, 25, 25), grayscale=True,
    #                             confidence=0.45) != None:
    #     pyautogui.click(840 + conv1, 200)
    #     time.sleep(0.2)

    #Club            
    if pyautogui.locateOnScreen('ref/ext1.png', region=(829 + conv0, 195, 30, 30), grayscale=True,
                                confidence=0.45) != None:
        pyautogui.click(842 + conv0, 207)
        time.sleep(0.2)
    
    if pyautogui.locateOnScreen('ref/ext1.png', region=(829 + conv1, 195, 30, 30), grayscale=True,
                                confidence=0.45) != None:
        pyautogui.click(842 + conv1, 207)
        time.sleep(0.2)

    #Crosses Ring Aquired
    if pyautogui.locateOnScreen('ref/ext1.png', region=(752 + conv0, 198, 25, 25), grayscale=True,
                                confidence=0.45) != None:
        pyautogui.click(763 + conv0, 210)
        time.sleep(0.2)
    
    if pyautogui.locateOnScreen('ref/ext1.png', region=(752 + conv1, 198, 25, 25), grayscale=True,
                                confidence=0.45) != None:
        pyautogui.click(763 + conv1, 210)
        time.sleep(0.2)
    #Winner/Back
    if pyautogui.locateOnScreen('ref/tweet.png', region=(432 + conv1, 456, 35, 35), grayscale=True,
                                 confidence=0.5) != None:
            pyautogui.click(305 + conv1, 535)
            time.sleep(0.2)
            pyautogui.click(305 + conv1, 535)
            time.sleep(0.5)
        
    if pyautogui.locateOnScreen('ref/tweet.png', region=(432 + conv0, 456, 35, 35), grayscale=True,
                                 confidence=0.5) != None:
        pyautogui.click(305 + conv0, 535)
        time.sleep(0.2)
        pyautogui.click(305 + conv0, 535)
        time.sleep(0.5)
    #Play mode and another initial mode
    if (pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                         confidence=0.5) == None and
                pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) == None and
                pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv0, 530)
            time.sleep(0.2)
    #Almost there!
    if pyautogui.locateOnScreen('ref/ext1.png', region= (791 + conv0, 215, 25, 25), grayscale=True, confidence=0.45):
        pyautogui.click(806 + conv0, 226)
        time.sleep(0.5)
    
    if pyautogui.locateOnScreen('ref/ext1.png', region= (791 + conv1, 215, 25, 25), grayscale=True, confidence=0.45):
        pyautogui.click(806 + conv1, 226)
        time.sleep(0.5)

    #Backs if Shop Opens
    if pyautogui.locateOnScreen('ref/shop.png', region=(555 + conv0, 165, 60, 25), grayscale=True,
                                         confidence=0.45) != None:
        pyautogui.click(306 + conv0, 180)
        time.sleep(0.5)

    if pyautogui.locateOnScreen('ref/shop.png', region=(555 + conv1, 165, 60, 25), grayscale=True,
                                         confidence=0.45) != None:
        pyautogui.click(306 + conv1, 180)
        time.sleep(0.5)
    #Backs Berlin
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/berlin.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/berlin.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv0, 530)
        time.sleep(0.2)
    
    #Backs Mumbai
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/mumbai.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/mumbai.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv0, 530)
        time.sleep(0.2)
            
    #Backs Seoul
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/seoul.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/seoul.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv0, 530)
        time.sleep(0.2)        
        
    #Backs Bangkok
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/bang.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/bang.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv0, 530)
        time.sleep(0.2)
    
    #Backs All In
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/allin.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv1, 530)
            time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                     confidence=0.9) != None and
                pyautogui.locateOnScreen('ref/allin.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                         confidence=0.5) != None):
            time.sleep(0.2)
            pyautogui.click(315 + conv0, 530)
            time.sleep(0.2)

    #closes Level Up message
    if(pyautogui.locateOnScreen('ref/levelup.png', region=(535 + conv0, 393, 100, 40), grayscale=True, 
                                confidence=0.7)) != None:
        time.sleep(0.2)
        pyautogui.click(586 + conv0, 413)
        time.sleep(0.5)

    if(pyautogui.locateOnScreen('ref/levelup.png', region=(535 + conv1, 393, 100, 40), grayscale=True, 
                                confidence=0.7)) != None:
        time.sleep(0.2)
        pyautogui.click(586 + conv1, 413)
        time.sleep(0.5)
    
    

def back_on_mismatch():

    if (pyautogui.locateOnScreen('ref/vs.png', region=(562 + conv0, 352, 43, 28), grayscale=True,
                                    confidence=0.5)!= None and pyautogui.locateOnScreen('ref/vs.png',
                                                                                 region=(562 + conv1, 352, 43, 28),
                                                                                 grayscale=True,
                                                                                 confidence=0.5) != None):
        if (pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv0,522,35,35), grayscale=True,
                                     confidence=0.5) == None and
                pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv1,522,35,35), grayscale=True,
                                         confidence=0.5) != None):
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Mis-Match Backed - Screen 2")
            pyautogui.click(305 + conv1, 535)
            time.sleep(0.2)
            pyautogui.click(305 + conv1, 535)
            time.sleep(0.2)

        if (pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv0,522,35,35), grayscale=True,
                                     confidence=0.5) != None and
                pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv1,522,35,35), grayscale=True,
                                         confidence=0.5) == None):
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Mis-Match Backed - Screen 1")
            pyautogui.click(305 + conv0, 535)
            time.sleep(0.2)
            pyautogui.click(305 + conv0, 535)
            time.sleep(0.2)
        
            
def Leave_Sequence():    
        
    if pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv1, 176, 40, 40 + 5), grayscale=True,
                                confidence=0.8) != None and pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv0, 176, 40, 40 + 5),
                                                                                        grayscale=True,
                                                                                        confidence=0.8) != None:
        time.sleep(0.5)
        pyautogui.click(306 + conv1, 190)
        time.sleep(0.5)
        pyautogui.click(306 + conv0, 190)
        time.sleep(0.2)
    
        
        
    if pyautogui.locateOnScreen('ref/leave.png', region=(291 + conv1, 296, 80, 40), grayscale=True,
                                confidence=0.5) != None and pyautogui.locateOnScreen('ref/leave.png', region=(291 + conv0, 296, 80, 40),
                                                                                        grayscale=True, confidence=0.5) != None:
        pyautogui.click(335 + conv1, 307)
        time.sleep(0.2)
        pyautogui.click(335 + conv0, 307)
        time.sleep(0.5)
    if pyautogui.locateOnScreen('ref/leave2.png', region=(477 + conv1, 413, 130, 40), grayscale=True,
                                confidence=0.5) != None and pyautogui.locateOnScreen('ref/leave2.png', region=(477 + conv0, 413, 130, 40),
                                                                                        grayscale=True,
                                                                                        confidence=0.5) != None:
        pyautogui.click(520 + conv1, 420)
        time.sleep(0.2)
        pyautogui.click(520 + conv0, 420)
        time.sleep(0.5)

def Individual_Leave_Sequence(convx):
    if pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + convx, 176, 40, 40 + 5), grayscale=True,
                                confidence=0.8) != None:
        time.sleep(0.5)
        pyautogui.click(306 + convx, 190)
        time.sleep(0.2)
    
    if pyautogui.locateOnScreen('ref/leave.png', region=(291 + convx, 296, 80, 40), grayscale=True,
                                confidence=0.5) != None:
        pyautogui.click(335 + convx, 307)
        time.sleep(0.7)
    if pyautogui.locateOnScreen('ref/leave2.png', region=(477 + convx, 413, 130, 40), grayscale=True,
                                confidence=0.5) != None:
        pyautogui.doubleClick(520 + convx, 420)
        time.sleep(0.5)
         
def Greenbox_Disappear(convx,timeout=40):
    start_time = datetime.now()
    while datetime.now() - start_time < timedelta(seconds=timeout):
        if pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + convx, 176, 40, 40 + 5), confidence=0.8) is None:
            return True
        time.sleep(1)
    
    return False
            
def Greenbox_Check():
    if(pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv1, 176, 40, 40 + 5), grayscale=True,
                                confidence=0.8) == None and pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv0, 176, 40, 40 + 5),
                                                                                        grayscale=True,
                                                                                        confidence=0.8) != None):
        if Greenbox_Disappear(conv0,int(waittimer)):
            pass
        else:
            Individual_Leave_Sequence(conv0)

    if(pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv1, 176, 40, 40 + 5), grayscale=True,
                            confidence=0.8) != None and pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + conv0, 176, 40, 40 + 5),
                                                                                    grayscale=True,
                                                                                    confidence=0.8) == None):
        if Greenbox_Disappear(conv1,int(waittimer)):
            pass
        else:
            Individual_Leave_Sequence(conv1)
                 
def start():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()
            check_for_cross()
                
            if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                        confidence=0.9) != None and
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                            confidence=0.5) != None):
                time.sleep(0.2)
                pyautogui.click(315 + conv1, 530)
                time.sleep(0.2)
            
                
                
            if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                        confidence=0.9) != None and
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                            confidence=0.5) != None):
                time.sleep(0.2)
                pyautogui.click(315 + conv0, 530)
                time.sleep(0.2)
            
                
                
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
                
                
            if pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(580 + conv1, 375)
                time.sleep(0.2)
                pyautogui.doubleClick(580 + conv0, 375)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/noguidelines.png', region=(534 + conv1, 459, 120, 100), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/noguidelines.png', region=(534 + conv0, 459, 120, 100),
                                                                                            grayscale=True,
                                                                                            confidence=0.5) != None:
                pyautogui.click(584 + conv1, 497)
                time.sleep(0.2)
                pyautogui.click(584 + conv0, 497)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/100.png', region=(428 + conv1, 273, 100, 40), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/100.png', region=(428 + conv0, 273, 100, 40),
                                                                                            grayscale=True, confidence=0.5) != None:

                Amount_Selection(bet)
            
                
                
            if pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv1, 461, 100, 50), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv0, 461, 100, 50),
                                                                                            grayscale=True,
                                                                                            confidence=0.5) != None:
                pyautogui.click(576 + conv1, 475)
                time.sleep(0.2)
                pyautogui.click(576 + conv0, 475)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")                                       

            Leave_Sequence()

            Greenbox_Check()

            if pyautogui.position() == (0, 0):
                raise pyautogui.FailSafeException("Fail-safe error")
             
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()



def miami():
    global conv1
    global conv0
    counter = 0
    redirect_output_to_file()
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()   
            check_for_cross()               
            
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
                
                
            if pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv1, 325, 130, 100), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv0, 325, 130, 100),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(710 + conv1, 374)
                time.sleep(0.2)
                pyautogui.doubleClick(710 + conv0, 374)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/100.png', region=(428 + conv1, 273, 100, 40), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/100.png', region=(428 + conv0, 273, 100, 40),
                                                                                            grayscale=True, confidence=0.5) != None:

                Amount_Selection(bet)
            
                
                
            if pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv1, 461, 100, 50), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv0, 461, 100, 50),
                                                                                            grayscale=True,
                                                                                            confidence=0.5) != None:
                pyautogui.click(576 + conv1, 475)
                time.sleep(0.2)
                pyautogui.click(576 + conv0, 475)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}") 
    
            Leave_Sequence()

            Greenbox_Check()  
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()    
    
def dallasl():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()  
            check_for_cross()     
                
            if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                        confidence=0.9) != None and
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True,
                                            confidence=0.5) != None):
                time.sleep(0.2)
                pyautogui.click(315 + conv1, 530)
                time.sleep(0.2)
            
                
                
            if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                        confidence=0.9) != None and
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True,
                                            confidence=0.5) != None):
                time.sleep(0.2)
                pyautogui.click(315 + conv0, 530)
                time.sleep(0.2)
            
                
                
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
                
                
            if pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv1, 325, 130, 100), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv0, 325, 130, 100),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(710 + conv1, 374)
                time.sleep(0.2)
                pyautogui.doubleClick(710 + conv0, 374)
                time.sleep(0.5)
                Green_Arrow_Right(1)
                time.sleep(0.5)
                
            if pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/100.png', region=(428 + conv1, 273, 100, 40), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/100.png', region=(428 + conv0, 273, 100, 40),
                                                                                            grayscale=True, confidence=0.5) != None:

                Amount_Selection(bet)
            
                
                
            if pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv1, 461, 100, 50), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv0, 461, 100, 50),
                                                                                            grayscale=True,
                                                                                            confidence=0.5) != None:
                pyautogui.click(576 + conv1, 475)
                time.sleep(0.2)
                pyautogui.click(576 + conv0, 475) 
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")  
            
            Leave_Sequence()
            
            Greenbox_Check()     
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()       
            

def instanbul():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()
            check_for_cross()    
                
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
                
                
            if pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv1, 325, 130, 100), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv0, 325, 130, 100),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(710 + conv1, 374)
                time.sleep(0.2)
                pyautogui.doubleClick(710 + conv0, 374)
                time.sleep(0.5)
                Green_Arrow_Right(2)
                time.sleep(0.5)
            
            if pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                time.sleep(0.5)
            
                
                
            if pyautogui.locateOnScreen('ref/100.png', region=(428 + conv1, 273, 100, 40), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/100.png', region=(428 + conv0, 273, 100, 40),
                                                                                            grayscale=True, confidence=0.5) != None:

                Amount_Selection(bet)
            
                
                
            if pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv1, 461, 100, 50), grayscale=True,
                                        confidence=0.5) != None and pyautogui.locateOnScreen('ref/confirm.png', region=(540 + conv0, 461, 100, 50),
                                                                                            grayscale=True,
                                                                                            confidence=0.5) != None:
                pyautogui.click(576 + conv1, 475)
                time.sleep(0.2)
                pyautogui.click(576 + conv0, 475)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")     

            Leave_Sequence()        
            Greenbox_Check()           
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()                


def mumbai():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()
            
            check_for_cross()        
                
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                        region=(345 + conv1, 511, 40, 40),
                                                                                        grayscale=False,
                                                                                        confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
                
                
            if pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv0 ,325, 130, 90), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playone.png',region=(370 + conv1 ,325, 130, 90),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(430+ conv1 ,370)
                time.sleep(0.2)
                pyautogui.doubleClick(430 + conv0, 370)
                time.sleep(0.5)
                Green_Arrow_Left(1)
                time.sleep(0.5)
            
            if pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/dbet.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)  
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}") 

            Leave_Sequence()
            Greenbox_Check()
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()


def seoull():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()
            check_for_cross()    
                
            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
            if pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv0 ,325, 130, 90), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playone.png',region=(370 + conv1 ,325, 130, 90),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(430+ conv1 ,370)
                time.sleep(0.2)
                pyautogui.doubleClick(430 + conv0, 370)
                time.sleep(0.5)
                Green_Arrow_Left(2)
                time.sleep(0.5)
            
            if pyautogui.locateOnScreen('ref/seoul.png', region=(455 + conv1, 353, 265, 65), grayscale=True, confidence=0.5) != None and \
                        pyautogui.locateOnScreen('ref/seoul.png', region=(455 + conv0, 353, 265, 65), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")      
            
            Leave_Sequence()
            Greenbox_Check()
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()
        
def bang():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet-1])}")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()

            check_for_cross()

            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
            if pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv0 ,325, 130, 90), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playone.png',region=(370 + conv1 ,325, 130, 90),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(430+ conv1 ,370)
                time.sleep(0.2)
                pyautogui.doubleClick(430 + conv0, 370)
                time.sleep(0.5)
                Green_Arrow_Left(3)
                time.sleep(0.5)
                
            if pyautogui.locateOnScreen('ref/bang.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/bang.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")    
                    
            Leave_Sequence()
            Greenbox_Check()
    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()
            
def all_in():
    global conv1
    global conv0
    redirect_output_to_file()
    counter = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {combo_table.get()}     |")
    time.sleep(0.5)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency :{freq} matches,   Wait Timer: {waittimer} seconds,   Bet: {str(bet_amounts[bet-1])} coins    |")
    time.sleep(1)
    try:
        while True:
            back_on_mismatch()

            check_for_cross()

            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40), grayscale=False,
                                        confidence=0.5) and pyautogui.locateOnScreen('ref/friends2.png',
                                                                                    region=(345 + conv1, 511, 40, 40),
                                                                                    grayscale=False,
                                                                                    confidence=0.5) and counter % (
                    int(freq) + 1) == 0:  # cambia questo modulo
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)  # clicks challenge
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)  # clicks the scenario
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)  # clicks accept (2s)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1
            
            if pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv0 ,325, 130, 90), grayscale=True,
                                        confidence=0.9) != None and pyautogui.locateOnScreen('ref/playone.png',region=(370 + conv1 ,325, 130, 90),
                                                                                            grayscale=True,
                                                                                            confidence=0.9) != None:
                pyautogui.doubleClick(430+ conv1 ,370)
                time.sleep(0.2)
                pyautogui.doubleClick(430 + conv0, 370)
                time.sleep(0.5)
                Green_Arrow_Left(16)
                time.sleep(0.5)
                
            if pyautogui.locateOnScreen('ref/allin.png', region=(461 + conv0, 355, 250, 60), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen('ref/allin.png', region=(461 + conv1, 355, 250, 60), grayscale=True, confidence=0.5) != None:
                pyautogui.click(561 + conv1, 385)
                time.sleep(0.2)
                pyautogui.click(561 + conv0, 385)
                time.sleep(0.5)   
            if pyautogui.locateOnScreen('ref/allin_yes.png', region=(535 + conv0, 453, 100, 40), grayscale=True,
                                        confidence=0.8) != None and pyautogui.locateOnScreen('ref/allin_yes.png', region=(535 + conv1, 453, 100, 40),
                                                                                            grayscale=True, confidence=0.8) != None:
                pyautogui.click(585 + conv1, 473)
                time.sleep(0.2)
                pyautogui.click(585 + conv0, 473)
                counter += 1
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")           
            Leave_Sequence()
            Greenbox_Check()

    except pyautogui.FailSafeException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failsafe activated, exiting...")
    finally:      
        restore_original_output()

game_running = False 
def start_game():
    selected_table = combo_table.get()
    if selected_table == "Miami Beach":
        miami()
    elif selected_table == "Dallas":
        dallasl()
    elif selected_table == "Istanbul":
        instanbul()
    elif selected_table == "Mumbai":
        mumbai()
    elif selected_table == "Seoul":
        seoull()
    elif selected_table == "Bangkok":
        bang()
    elif selected_table == "Beijing":
        start()
    elif selected_table == "All-In":
        all_in()
    else:
        print("Please select a table.")


def pause_game():
    global game_running
    if game_running:
        game_running = False
        print("Game paused")
    else:
        print("Game is not running")

def stop_game():
    global game_running
    if game_running:
        game_running = False
        print("Game stopped")
    else:
        print("Game is not running")

root = tk.Tk()
root.title("8Ball Bot")
root.resizable(False, False)

icon_path = r"C:\Users\sahas\Desktop\Bot2\TitleBar.ico"
root.iconbitmap(icon_path)
                
style = ttk.Style()
style.configure("TButton", font=('Arial', 10))

e = tk.Entry(root, font=('Arial', 10))
e.grid(row=0, column=1, padx=10, pady=10)

e_wait_timer = tk.Entry(root, font=('Arial', 10))
e_wait_timer.grid(row=1, column=1, padx=10, pady=10)

mybuttonFreq = ttk.Button(root, text="Frequency", command=getFreq)
mybuttonFreq.grid(row=0, column=2, padx=10, pady=10)

mybuttonWait = ttk.Button(root, text="Wait Timer", command=setWaitTimer)
mybuttonWait.grid(row=1, column=2, padx=10, pady=10)

bet_frame = ttk.Frame(root)
bet_frame.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

bet_amounts = ["100", "500", "2.5k", "10k", "50k", "100k", "500k", "2.5M", "10M"]
bet_buttons = []

for i, amount in enumerate(bet_amounts):
    bet_button = ttk.Button(bet_frame, text=amount, style="TButton", command=locals()[f'getBet{i+1}'])
    bet_button.grid(row=i//3, column=i%3, padx=5, pady=5)
    
    style.map(f"BetButton{i+1}.TButton", foreground=[("active", "purple")], background=[("active", "#007acc")])
    style.configure(f"BetButton{i+1}.TButton", padding=(5, 5), width=10, height=2, relief="raised")
    bet_button.config(style=f"BetButton{i+1}.TButton")
    bet_buttons.append(bet_button)

frame_game = ttk.LabelFrame(root, text="Select a Game")
frame_game.grid(row=4, column=0, columnspan=4, padx=10, pady=10)


combo_table = ttk.Combobox(frame_game, values=["Miami Beach", "Dallas", "Istanbul", "Mumbai", "Seoul","Bangkok","Beijing","All-In"])
combo_table.set("Select Table")
combo_table.grid(row=0, column=0, padx=10, pady=10)


start_button = ttk.Button(frame_game, text="START", command=start_game)
start_button.grid(row=1, column=0, padx=10, pady=10)

button_frame = ttk.Frame(frame_game)
button_frame.grid(row=1, column=0, padx=10, pady=10)

start_button = ttk.Button(button_frame, text="START", command=start_game)
start_button.grid(row=0, column=0, padx=10, pady=10)


pause_button = ttk.Button(button_frame, text="PAUSE", command=pause_game)
pause_button.grid(row=0, column=1, padx=10, pady=10)

stop_button = ttk.Button(button_frame, text="STOP", command=stop_game)
stop_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()