import pyautogui
import time
import pyperclip
import datetime

def add_rows(row_num, day_inc, amount_inc):
    sleep_time = 0.01
    print('add_rows hello world')
    # get time
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleep_time)
    date_str = pyperclip.paste()
    cur_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    inc_date = cur_date
    # get starting increment
    pyautogui.press('tab')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleep_time)
    start_slope = pyperclip.paste()
    inc_slope = int(start_slope)
    # add rows
    for x in range(0, int(row_num)):
        inc_date = inc_date + datetime.timedelta(days=int(day_inc))
        inc_slope = inc_slope + int(amount_inc)
        pyautogui.press('tab')
        time.sleep(sleep_time)
        pyautogui.press('enter')
        time.sleep(sleep_time)
        pyautogui.press('tab')
        time.sleep(sleep_time)
        pyautogui.press('tab')
        time.sleep(sleep_time)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(sleep_time)
        pyautogui.press('backspace')
        time.sleep(sleep_time)
        pyautogui.typewrite(str(inc_date.date()), interval=0.01)
        time.sleep(sleep_time)
        pyautogui.press('tab')
        time.sleep(sleep_time)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(sleep_time)
        pyautogui.press('backspace')
        time.sleep(sleep_time)
        pyautogui.typewrite(str(inc_slope), interval=0.01)
        time.sleep(sleep_time)

user_input = 'null'
while user_input != 'q':
    print('Beeminder Rode Editor Increment Program.')
    print('This program is for the Beeminder Client-Side Graphs and Road Editor (Editor radio button).')
    print('a - used to add rows after the row that has cursor focus on the end date.') 
    print('q - used to quit this program.') 
    user_input = input('type one of the previous commands: ')
    if user_input == 'a':
        row_num = input('How many rows would you like to add?\n')
        day_inc = input('How often (in days) would you like to increment? For one weak, put 7.\n')
        amount_inc = input('By how much would you like to increment? 2 will add 2 each time (10, 12, 14, 16).\n')
        print('After clicking enter, there will be a 6 second countdown before new rows start getting added.')
        print('Move the application focus to the browser with the browser with the Beeminder Road Editor.')
        input('Move the cursor focus to the Road Editor date just before where you want to add the rows.')
        print('6')
        time.sleep(1)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('BLAST OFF!!!')
        add_rows(row_num, day_inc, amount_inc)

print('Have a nice day.')
