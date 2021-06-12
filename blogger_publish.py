import pyautogui
import time
import csv
# time.sleep(5)
import check_link

pyautogui.press('winleft')
time.sleep(2)
pyautogui.click(19,328)
pyautogui.moveTo(200,400)
time.sleep(3)
pyautogui.keyDown('ctrl')
pyautogui.press('t')
pyautogui.keyUp('ctrl')
time.sleep(0.5)
def publish(file):
    with open(file,'r+') as f:
        csvreader = csv.reader(f)
        pyautogui.typewrite("https://blogger.com")
        pyautogui.press('enter')
        time.sleep(10)
        for i in range(10):
            pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.press('tab')
        for row in csvreader:
            link = row[0]
            heading = row[1]
            body = row[2]
            img_link = row[3]
            chk = check_link.check('uploaded_data.csv',link)
            if chk == False:
                # pyautogui.click(195, 275)
                pyautogui.write(heading, interval=0.05)
                # pyautogui.click(724,560)
                # pyautogui.write(body, interval=0.05)
                # pyautogui.click(164,585)
                for i in range(15):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.press('up')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.write(img_link,interval=0.01)
                time.sleep(2)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write(img_link[-4:],interval=0.1)
                time.sleep(1)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write(img_link[-2:],interval=0.1)
                time.sleep(1)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write(img_link[-2:], interval=0.1)
                time.sleep(1)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write(img_link[-2:], interval=0.1)
                time.sleep(5)
                pyautogui.press('enter')

                pyautogui.press('down')
                pyautogui.press('enter')
                pyautogui.press('enter')
                pyautogui.write(body, interval=0.01)
                pyautogui.moveTo(1723,419,2)
                pyautogui.click(1723,419)
                if file == 'Tech_data.csv':
                    pyautogui.write("Technology,")
                elif file == 'World_data.csv':
                    pyautogui.write("World,")
                elif file == 'India_data.csv':
                    pyautogui.write("India,")
                for i in range(5):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.write(body[:140],interval=0.05)
                for i in range(13):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.press('enter')
                write_csv(link,heading,body,img_link)
                time.sleep(10)
                pyautogui.press('f5')
                time.sleep(7)
                for i in range(10):
                    pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.press('tab')

def write_csv(link,heading,body,img_link):
    with open('blogger_uploaded_data.csv', 'a') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([link, heading, body, img_link, '1'])

publish('India_data.csv')
publish('World_data.csv')