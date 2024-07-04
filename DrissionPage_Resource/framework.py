from DrissionPage import WebPage

wpage = WebPage()
wpage.get("http://140.118.186.70:3000/pandaCave")

#點擊所有wake_up按鈕
for btn in wpage.eles('(填空)'):
    btn.click()

#尋找所有inner text含有*Panda*的元素
p_list = wpage.eles('(填空)')
count = len(p_list)

#把所有attr有*Panda*的div元素加入p_list並確保不重複
for e in wpage.eles('(填空)'):
    for attr in e.(填空).values():
        if '*Panda*' in attr and not e in p_list:
            p_list.append(e)
            break

#計算所有取得的元素中有多少*Panda*藏在attr中
for e in p_list:
    for attr in e.(填空).values():
        if '*Panda*' in attr:
            count += 1

print(count)
