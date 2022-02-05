# Resolution of display = 1366 X 768
# Browser : Firefox (90% Zoom)

#----------------------importing relevent modules----------------------------
import pyautogui as pg
import time as t

#---------------Taking insta id and number of posts from users---------------
insta_id = input("Enter insta id : ")
post_queue = int(input("How many post do you want to Like ? : "))

#---------------------Searching for the insta id-----------------------------
t.sleep(3)
pg.moveTo(461,63)
pg.leftClick()
pg.write("https://www.instagram.com/"+insta_id)
pg.press("enter")

#-----------------------Selecting first post---------------------------------
t.sleep(8)
pg.moveTo(910,333)
pg.scroll(-700)
pg.moveTo(350,480)
pg.leftClick()

#-------------------Auto loop for scrolling posts----------------------------
t.sleep(2)
for i in range(post_queue):
    pg.moveTo(429,419)
    pg.doubleClick()
    pg.moveTo(1335,409)
    pg.leftClick()
    t.sleep(2)

#-------------------------End of the program---------------------------------