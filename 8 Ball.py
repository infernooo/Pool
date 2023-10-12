import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import sys
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import re
from prettytable import PrettyTable

game_paused = False
bet = 0
freq = 0
waittimer = 0
freq_balance_check = 0
original_stdout = sys.stdout
table_list = ['dbet','allin', 'berlin', 'mumbai', 'seoul', 'bang', 'rome', 'paris', 'shanghai', 'dubai', 'cairo', 'torento', 'jakarta', 'lasvegas', 'tokyo', 'moscow', 'sydney', 'london']
conv1 = 960
conv0 = 0
# Specify the path to the text file where you want to save the console output
output_file_path = 'ref/Logs/console_output.txt'
output_file = None  # Global variable to store the file object
to_check_bal = False
all_tables = []
table_file = None


def getFreq():
    global freq
    freq = e.get()

def setWaitTimer():
    global waittimer
    waittimer = e_wait_timer.get()

def getBalanceReader():
    global freq_balance_check
    freq_balance_check = e_balance_checker.get()


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


class DualOutput:
    def __init__(self, *outputs):
        self.outputs = outputs

    def write(self, text):
        for output in self.outputs:
            output.write(text)

    def flush(self):
        pass  # You can implement flush if needed

def screenshot(R, pic=0):
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot(region=R)
    pic +=1
    # Specify the file path where you want to save the screenshot
    save_path = Rf"C:\Users\sahas\Desktop\Bot2\dist\ref\Failed_extractions\fail{pic}.png"
    # Save the screenshot
    screenshot.save(save_path)

def redirect_output_to_file():
    global output_file
    # Open the file in append mode
    output_file = open(output_file_path, 'a')

    # Redirect standard output to both the console and the file
    sys.stdout = DualOutput(sys.stdout, output_file)

    # Optionally, you can redirect standard error as well
    sys.stderr = DualOutput(sys.stderr, output_file)

def restore_original_output(table):
    global output_file, table_file, all_tables
    if output_file:
        output_file.close()
    if table_file:
        table_file.close()

    sys.stdout = original_stdout
    sys.stderr = sys.__stderr__

    # Append the table to the list of all_tables
    all_tables.append(table)

    # Write tables to the table file
    with open(output_file_path, 'a') as table_file:
        for t in all_tables:
            table_file.write(str(t) + '\n')


    
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
        time.sleep(0.5)
        pyautogui.click(305 + conv1, 535)
        time.sleep(0.5)
        
    if pyautogui.locateOnScreen('ref/tweet.png', region=(432 + conv0, 456, 35, 35), grayscale=True,
                                 confidence=0.5) != None:
        pyautogui.click(305 + conv0, 535)
        time.sleep(0.5)
        pyautogui.click(305 + conv0, 535)
        time.sleep(0.5)
    
    #Almost there!
    if pyautogui.locateOnScreen('ref/ext1.png', region= (791 + conv0, 215, 25, 25), grayscale=True, confidence=0.45):
        pyautogui.click(806 + conv0, 226)
        time.sleep(0.5)
    
    if pyautogui.locateOnScreen('ref/ext1.png', region= (791 + conv1, 215, 25, 25), grayscale=True, confidence=0.45):
        pyautogui.click(806 + conv1, 226)
        time.sleep(0.5)

    #Backs if Shop Opens
    if pyautogui.locateOnScreen('ref/shop.png', region=(555 + conv0, 165, 60, 25), grayscale=True,
                                         confidence=0.7) != None:
        pyautogui.click(306 + conv0, 180)
        time.sleep(0.5)

    if pyautogui.locateOnScreen('ref/shop.png', region=(555 + conv1, 165, 60, 25), grayscale=True,
                                         confidence=0.7) != None:
        pyautogui.click(306 + conv1, 180)
        time.sleep(0.5)

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
    
def Backs_Inactive_screens():

    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/i.png', region=(695 + conv1, 445, 21, 24), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv1, 530)
        time.sleep(0.2)
    if (pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100), grayscale=True,
                                    confidence=0.9) != None and
            pyautogui.locateOnScreen('ref/i.png', region=(695 + conv0, 445, 21, 24), grayscale=True,
                                        confidence=0.5) != None):
        time.sleep(0.2)
        pyautogui.click(315 + conv0, 530)
        time.sleep(0.2)        

def back_on_mismatch():
    while True:
        vs_r1 = pyautogui.locateOnScreen('ref/vs.png', region=(562 + conv0, 309, 43, 70), grayscale=True, confidence=0.5) is not None
        vs_r2 = pyautogui.locateOnScreen('ref/vs.png', region=(562 + conv1, 309, 43, 70), grayscale=True, confidence=0.5) is not None
        fb_r3 = pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv0, 522, 35, 35), grayscale=True, confidence=0.5) is not None
        fb_r4 = pyautogui.locateOnScreen('ref/fb.png', region=(290 + conv1, 522, 35, 35), grayscale=True, confidence=0.5) is not None

        if vs_r1 and vs_r2 and fb_r3 and fb_r4:
            # Either all conditions are met or none are met, continue checking
            continue

        if vs_r1 and vs_r2 and fb_r3 and not fb_r4:
            pyautogui.click(305 + conv0, 535)
        elif vs_r1 and vs_r2 and not fb_r3 and fb_r4:
            pyautogui.click(305 + conv1, 535)


        # Break out of the loop once action is taken
        break
            
def Leave_Sequence(num=0,denom=1):    
        
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
                                confidence=0.6) != None and pyautogui.locateOnScreen('ref/leave.png', region=(291 + conv0, 296, 80, 40),
                                                                                        grayscale=True, confidence=0.6) != None:
        pyautogui.click(335 + conv1, 307)
        time.sleep(0.2)
        pyautogui.click(335 + conv0, 307)
        time.sleep(0.5)
    if pyautogui.locateOnScreen('ref/leave2.png', region=(477 + conv1, 413, 130, 40), grayscale=True,
                                confidence=0.6) != None and pyautogui.locateOnScreen('ref/leave2.png', region=(477 + conv0, 413, 130, 40),
                                                                                        grayscale=True,
                                                                                        confidence=0.6) != None:
        pyautogui.click(520 + conv1, 420)
        time.sleep(0.2)
        pyautogui.click(520 + conv0, 420)
        time.sleep(0.5)
        if int(freq_balance_check) == 0:
            pass
        if num % ((denom + 1) * int(freq_balance_check)) == 1 and num // denom > 0:
            return True
    
def Individual_Leave_Sequence(convx, retries=3):
    for attempt in range(retries):
        if pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + convx, 176, 40, 40 + 5), grayscale=True,
                                    confidence=0.6) is not None:
            time.sleep(0.5)
            pyautogui.click(306 + convx, 190)
            time.sleep(0.2)
        
        if pyautogui.locateOnScreen('ref/leave.png', region=(291 + convx, 296, 80, 40), grayscale=True,
                                    confidence=0.6) is not None:
            pyautogui.click(335 + convx, 307)
            time.sleep(0.7)
        if pyautogui.locateOnScreen('ref/leave2.png', region=(477 + convx, 413, 130, 40), grayscale=True,
                                      confidence=0.6) is not None:
            pyautogui.doubleClick(520 + convx, 420)
            time.sleep(0.5)
        else:
            time.sleep(0.5)  # Delay before the next retry
            continue
        
        break
#Checks In case of Individual Match, opponent quits before the wait buffer time         
def Greenbox_Disappear(convx,timeout=40):
    start_time = datetime.now()
    while datetime.now() - start_time < timedelta(seconds=timeout):
        if pyautogui.locateOnScreen('ref/greenbutton.png', region=(293 + convx, 176, 40, 40 + 5), confidence=0.8) is None:
            return True
        time.sleep(1)
    
    return False

def Greenbox_Check():
    r1 = (293 + conv0, 176, 40, 40 + 5)
    r2 = (293 + conv1, 176, 40, 40 + 5)
    global to_check_bal
    green_button_in_r1 = pyautogui.locateOnScreen('ref/greenbutton.png', region=r1, grayscale=True, confidence=0.7)
    green_button_in_r2 = pyautogui.locateOnScreen('ref/greenbutton.png', region=r2, grayscale=True, confidence=0.7)

    if green_button_in_r1 is not None and green_button_in_r2 is None or green_button_in_r1 is None and green_button_in_r2 is not None:
        time.sleep(0.2) 
        green_button_in_r1 = pyautogui.locateOnScreen('ref/greenbutton.png', region=r1, grayscale=True, confidence=0.7)
        green_button_in_r2 = pyautogui.locateOnScreen('ref/greenbutton.png', region=r2, grayscale=True, confidence=0.7)
        
    if green_button_in_r1 is not None and green_button_in_r2 is None:
        if Greenbox_Disappear(conv0, int(waittimer)):
            pass
        else:
            Individual_Leave_Sequence(conv0)

    elif green_button_in_r1 is None and green_button_in_r2 is not None:
        if Greenbox_Disappear(conv1, int(waittimer)):
            pass
        else:
            Individual_Leave_Sequence(conv1)

class OCRProcessor:
    def __init__(self, max_retries=3, delay_between_retries=0.5):
        self.readings = []
        self.max_retries = max_retries
        self.delay_between_retries = delay_between_retries

    def preprocess_image(self, img):
        preprocessed_img = img.resize((650, 100)).convert('L')
        enhancer = ImageEnhance.Contrast(preprocessed_img)
        preprocessed_img = enhancer.enhance(1.5)
        preprocessed_img = preprocessed_img.filter(ImageFilter.GaussianBlur(radius=1.5))
        return preprocessed_img

    def extract_numbers_from_text(self, text):
        numbers = re.findall(r'\d+', text)
        result = ''.join(numbers)
        return int(result) if result else 0

    def image_to_text_from_screenshot(self, region, repeat_ocr=False):
        self.readings = []

        for attempt in range(self.max_retries):
            try:
                ss = pyautogui.screenshot(region=region)
                preprocessed_img = self.preprocess_image(ss)
                custom_config = r'--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789'
                extracted_text = pytesseract.image_to_string(preprocessed_img, config=custom_config)

                result = self.extract_numbers_from_text(extracted_text)
                self.readings.append(result)

                if repeat_ocr and len(self.readings) >= 2 and self.readings[-1] != self.readings[-2]:
                    repeat_ocr = False
                    continue
                elif repeat_ocr and len(self.readings) == 3 and self.readings[-1] in (self.readings[0], self.readings[1]):
                    return self.readings[-1]

                if not repeat_ocr:
                    return self.readings[-1]

            except pytesseract.TesseractError as e:
                print(f"Tesseract Error: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay_between_retries)
                else:
                    print("Max retries reached. Unable to extract text.")
                    return 0
            finally:
                if 'preprocessed_img' in locals():
                    del preprocessed_img
                 
def play_game(game_type, no_of_clicks, table_name, Initial_Balance_r1, Initial_Balance_r2):
    global table, all_tables
    ocr_processor = OCRProcessor()
    current_balance_r1, current_balance_r2 = 0, 0
    previous_balance_r1, previous_balance_r2 = Initial_Balance_r1, Initial_Balance_r2
    transfered_amount, wastage_amount = 0, 0
    total_transfered_amount, total_wastage_amount = 0, 0
    counter = 0
    global to_check_bal
    table = PrettyTable()
    table.field_names = ["Time", "Receiver", "Sender", "Transferred", "Wastage", "Rate of Transfer"]
    table.add_row([time.strftime("%H:%M:%S"), f"{Initial_Balance_r1:,}", f"{Initial_Balance_r2:,}", "", "", ""])
    table.add_row(['Total :', "", "", f"{total_transfered_amount:,}", f"{total_wastage_amount:,}", ""])
    total_row_index = 1
    print(table)
    start_time = datetime.now()
    try:
        while True:
            back_on_mismatch()
            check_for_cross()

            if to_check_bal and pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40),
                                                         grayscale=False, confidence=0.5) and pyautogui.locateOnScreen(
                    'ref/friends2.png', region=(345 + conv1, 511, 40, 40), grayscale=False, confidence=0.5):

                current_balance_r1 = ocr_processor.image_to_text_from_screenshot((811 + conv0, 193, 62, 10),
                                                                                repeat_ocr=True)
                current_balance_r2 = ocr_processor.image_to_text_from_screenshot((811 + conv1, 193, 62, 10),
                                                                                repeat_ocr=True)

                transfered_amount = current_balance_r1 - previous_balance_r1
                wastage_amount = (previous_balance_r2 - current_balance_r2) - transfered_amount

                total_transfered_amount = current_balance_r1 - Initial_Balance_r1
                total_wastage_amount = Initial_Balance_r2 - current_balance_r2 - total_transfered_amount

                end_time = datetime.now()
                elapsed = end_time - start_time
                bph = round((transfered_amount / elapsed.total_seconds()) * 3600 / 1000000000, 4)
                start_time = datetime.now()
                row = [time.strftime("%H:%M:%S"), f"{current_balance_r1:,}", f"{current_balance_r2:,}",
                       f"{transfered_amount:,}", f"{wastage_amount:,}", bph]
                table.del_row(total_row_index)
                table.add_row(row)
                table.add_row(['Total :', "", "", f"{total_transfered_amount:,}", f"{total_wastage_amount:,}", ""])
                total_row_index += 1
                previous_balance_r1 = current_balance_r1
                previous_balance_r2 = current_balance_r2
                to_check_bal = False
                time.sleep(0.5)

                # Print the updated table
                print("\033c")  # ANSI escape code to clear console
                print(table)

            if pyautogui.locateOnScreen('ref/friends2.png', region=(345 + conv0, 511, 40, 40),
                                        grayscale=False, confidence=0.5) and pyautogui.locateOnScreen(
                    'ref/friends2.png', region=(345 + conv1, 511, 40, 40), grayscale=False, confidence=0.5) and counter % (
                    int(freq) + 1) == 0:
                pyautogui.doubleClick(362 + conv1, 530)
                time.sleep(1.3)
                pyautogui.click(368 + conv1, 477)
                time.sleep(1.3)
                pyautogui.click(395 + conv1, 390)
                time.sleep(2)
                pyautogui.click(1673 - conv1, 191)
                time.sleep(2.3)
                pyautogui.click(722 + conv1, 192)
                # print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Started friendly")
                counter += 1

            Greenbox_Check()
            to_check_bal = Leave_Sequence(counter, int(freq))
            Backs_Inactive_screens()
                
            #9 Ball Mode
            if game_type == "9bp":
                if pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv1, 325, 130, 100),
                                                                grayscale=True, confidence=0.9) is not None and \
                    pyautogui.locateOnScreen('ref/playf.png', region=(660 + conv0, 325, 130, 100),
                                            grayscale=True, confidence=0.9) is not None:
                    pyautogui.doubleClick(710 + conv1, 374)
                    time.sleep(0.2)
                    pyautogui.doubleClick(710 + conv0, 374)
                    time.sleep(0.5)
                    Green_Arrow_Right(no_of_clicks)
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
                    # print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}")  

            #PlaySpecial Mode    
            elif game_type == "special": 
                if pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv1, 325, 120, 100),
                                                                    grayscale=True, confidence=0.9) is not None and \
                    pyautogui.locateOnScreen('ref/playspecial.png', region=(526 + conv0, 325, 120, 100),
                                            grayscale=True, confidence=0.9) is not None:
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
                    # print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}") 


            #1 on 1 Mode
            elif game_type == "1o1": 
                if pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv0, 325, 130, 90),
                                                               grayscale=True, confidence=0.9) is not None and \
                    pyautogui.locateOnScreen('ref/playone.png', region=(370 + conv1, 325, 130, 90),
                                            grayscale=True, confidence=0.9) is not None:
                    pyautogui.doubleClick(430 + conv1, 370)
                    time.sleep(0.2)
                    pyautogui.doubleClick(430 + conv0, 370)
                    time.sleep(0.5)
                    Green_Arrow_Left(no_of_clicks)
                    time.sleep(0.5)

                if pyautogui.locateOnScreen(f'ref/{table_name}.png', region=(455 + conv1, 353, 265, 65), grayscale=True, confidence=0.5) != None and \
                    pyautogui.locateOnScreen(f'ref/{table_name}.png', region=(455 + conv0, 353, 265, 65), grayscale=True, confidence=0.5) != None:
                    pyautogui.click(561 + conv1, 385)
                    time.sleep(0.2)
                    pyautogui.click(561 + conv0, 385)  
                    counter += 1
                    # print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Counter: {counter}") 

                if pyautogui.locateOnScreen('ref/allin_yes.png', region=(535 + conv0, 453, 100, 40), grayscale=True,
                                            confidence=0.8) != None and pyautogui.locateOnScreen('ref/allin_yes.png', region=(535 + conv1, 453, 100, 40),
                                                                                                grayscale=True, confidence=0.8) != None:
                    pyautogui.click(585 + conv1, 473)
                    time.sleep(0.2)
                    pyautogui.click(585 + conv0, 473)

                if pyautogui.locateOnScreen('ref/tutorial.png', region=(458 + conv0, 211, 255, 18), grayscale=True,
                                            confidence=0.8) != None and pyautogui.locateOnScreen('ref/tutorial.png', region=(458 + conv1, 211, 255, 18),
                                                                                                grayscale=True, confidence=0.8) != None:
                    pyautogui.click(585 + conv1, 496)
                    time.sleep(0.2)
                    pyautogui.click(585 + conv0, 496)
                
    except pyautogui.FailSafeException:
        print("[ERROR] PyAutoGUI fail-safe exception triggered. Stopping the game.")
        # Add any additional cleanup or logging here
    except KeyboardInterrupt:
        print("[INFO] Game stopped manually.")
    finally:      
        restore_original_output(table)


 
def start_game():
    global game_paused
    redirect_output_to_file()
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...")
    time.sleep(0.2)

    selected_table = combo_table.get()
    ocr_processor = OCRProcessor()
    # Mapping table names to corresponding functions
    table_mapping = {
        "Miami Beach": lambda r1, r2: play_game("9bp", 0, selected_table, r1, r2),
        "Dallas": lambda r1, r2: play_game("9bp", 1, selected_table, r1, r2),
        "Istanbul": lambda r1, r2: play_game("9bp", 2, selected_table, r1, r2),
        "Beijing": lambda r1, r2: play_game("special", r1, r2, r1, r2),
        "All-In": lambda r1, r2: play_game("1o1", 16, 'allin', r1, r2),
        "Berlin - 25M": lambda r1, r2: play_game("1o1", 0, 'berlin', r1, r2),
        "Mumbai - 15M": lambda r1, r2: play_game("1o1", 1, 'mumbai', r1, r2),
        "Seoul - 10M": lambda r1, r2: play_game("1o1", 2, 'seoul', r1, r2),
        "Bangkok - 5M": lambda r1, r2: play_game("1o1", 3, 'bang', r1, r2),
        "Rome - 4M": lambda r1, r2: play_game("1o1", 4, 'rome', r1, r2),
        "Paris - 2.5M": lambda r1, r2: play_game("1o1", 5, 'paris', r1, r2),
        "Shanghai - 1M": lambda r1, r2: play_game("1o1", 6, 'shanghai', r1, r2),
        "Dubai - 500K": lambda r1, r2: play_game("1o1", 7, 'dubai', r1, r2),
        "Cairo - 250K": lambda r1, r2: play_game("1o1", 8, 'cairo', r1, r2),
        "Toronto - 100K": lambda r1, r2: play_game("1o1", 9, 'Torento', r1, r2),
        "Jakarta - 50K": lambda r1, r2: play_game("1o1", 10, 'jakarta', r1, r2),
        "Las Vegas": lambda r1, r2: play_game("1o1", 11, 'lasvegas', r1, r2),
        "Tokyo": lambda r1, r2: play_game("1o1", 12, 'tokyo', r1, r2),
        "Moscow": lambda r1, r2: play_game("1o1", 13, 'moscow', r1, r2),
        "Sydney": lambda r1, r2: play_game("1o1", 14, 'sydney', r1, r2),
        "London": lambda r1, r2: play_game("1o1", 15, 'london', r1, r2),
    }

    
    if selected_table in table_mapping:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Table Selected - {selected_table}")
        time.sleep(0.2)
        print(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Friendly Frequency: {freq}   Wait Timer: {waittimer}   Bet: {str(bet_amounts[bet - 1])}    Balance Checker: {freq_balance_check}")

        # Loop through check_for_cross(), leave_sequence(), and Individual_leave_sequence()
        while Individual_Leave_Sequence(conv0) or Individual_Leave_Sequence(conv1) or check_for_cross() or Leave_Sequence():
            time.sleep(1)
            pass  # You may want to add a delay or other logic here

        # Take Initial_Balance_r1 and r2 readings
        Initial_Balance_r1 = ocr_processor.image_to_text_from_screenshot((811 + conv0, 193, 62, 10), repeat_ocr=True)
        Initial_Balance_r2 = ocr_processor.image_to_text_from_screenshot((811 + conv1, 193, 62, 10), repeat_ocr=True)

        # Start the called functions with Initial_Balance_r1 and r2 as arguments
        table_mapping[selected_table](Initial_Balance_r1, Initial_Balance_r2)
    else:
        print("Please select a valid table.")


def pause_game():
    global game_paused
    game_paused = not game_paused  # Toggle the pause state
    if game_paused:
        print("Game paused")
        # Include any logic needed when the game is paused
    else:
        print("Game resumed")
        # Include any logic needed when the game is resumed

def stop_game():
    global game_paused
    print("Game stopped!")
    # Include any cleanup or finalization code here
    root.destroy()

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

e_balance_checker = tk.Entry(root, font=('Arial', 10))
e_balance_checker.grid(row=2, column=1, padx=10, pady=10)

mybuttonFreq = ttk.Button(root, text="Frequency", command=getFreq)
mybuttonFreq.grid(row=0, column=2, padx=10, pady=10)

mybuttonWait = ttk.Button(root, text="Wait Timer", command=setWaitTimer)
mybuttonWait.grid(row=1, column=2, padx=10, pady=10)

mybuttonNew = ttk.Button(root, text="Balance Checker", command=getBalanceReader)
mybuttonNew.grid(row=2, column=2, padx=10, pady=10)

bet_frame = ttk.Frame(root)
bet_frame.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

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


combo_table = ttk.Combobox(frame_game, values=["Miami Beach", "Dallas", "Istanbul","Beijing", "All-In", 
                                               "Berlin - 25M", "Mumbai - 15M", "Seoul - 10M", "Bangkok - 5M", 
                                               "Rome - 4M", "Paris - 2.5M", "Shanghai - 1M", "Dubai - 500K",
                                                "Cairo - 250K" , "Toronto - 100K", "Jakarta - 50K", 
                                               "Las Vegas", "Tokyo", "Moscow", "Sydney", "London"])
combo_table.set("Select Table")
combo_table.grid(row=0, column=0, padx=10, pady=10)


button_frame = ttk.Frame(frame_game)
button_frame.grid(row=1, column=0, padx=10, pady=10)

start_button = ttk.Button(button_frame, text="START", command=start_game)
start_button.grid(row=0, column=0, padx=10, pady=10)


pause_button = ttk.Button(button_frame, text="PAUSE", command=pause_game)
pause_button.grid(row=0, column=1, padx=10, pady=10)

stop_button = ttk.Button(button_frame, text="STOP", command=stop_game)
stop_button.grid(row=0, column=2, padx=10, pady=10)

keyboard.add_hotkey('ctrl+alt+s', start_game)
keyboard.add_hotkey('ctrl+alt+p', pause_game)
keyboard.add_hotkey('ctrl+alt+q', stop_game)


root.mainloop()
