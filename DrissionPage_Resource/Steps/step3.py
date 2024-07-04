#上一步
'''
from DrissionPage import WebPage

wpage = WebPage()
wpage.get("http://140.118.186.70:3000/pandaCave")

#點擊所有wake_up按鈕
for btn in wpage.eles('@@tag()=button@@name=wake_up'):
    btn.click()

#尋找所有inner text含有Panda的元素，並計算有多少*Panda*
'''
#下一步
from DrissionPage import WebPage

wpage = WebPage()
wpage.get("http://140.118.186.70:3000/pandaCave")

#點擊所有wake_up按鈕
for btn in wpage.eles('@@tag()=button@@name=wake_up'):
    btn.click()

#尋找所有inner text含有Panda的元素，並計算有多少*Panda*
count = len(wpage.eles('@text():*Panda*'))

#把所有attr有Panda的div檢查過一遍，找到所有attr中的*Panda*