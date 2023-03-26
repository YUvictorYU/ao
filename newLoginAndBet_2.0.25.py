from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from selenium.webdriver.common.keys import Keys
import time


# 创建GUI界面
root = tk.Tk()
root.title("网站登陆器")

# 创建标签和输入框
url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0)
url_entry = tk.Entry(root, width=100)
url_entry.grid(row=0, column=1, columnspan=3)

amount_label = tk.Label(root, text="投注金额:")
amount_label.grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

periods_label = tk.Label(root, text="投注期数:")
periods_label.grid(row=1, column=2)
periods_entry = tk.Entry(root)
periods_entry.grid(row=1, column=3)

# 定义登录和投注函数
def login_and_bet():
    # 获取输入框中的值
    url = url_entry.get()
    amount = int(amount_entry.get())
    periods = int(periods_entry.get())
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge('D:\driver\msedgedriver',options=option)
    driver.maximize_window
    global count
    while (periods > 0):
        driver.get(url)
        try:
            time.sleep(3)
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[1]/div[1]').click() # 01
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[2]/div[1]').click() # 02
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[3]/div[1]').click() # 03
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[4]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[5]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[6]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[7]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[8]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[9]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[10]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[11]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[12]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[13]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[14]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[15]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[16]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[17]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[18]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[19]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[20]/div[1]').click()
            script = "return arguments[0].scrollIntoView();";
            element = driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[21]/div[1]')
            driver.execute_script(script, element)
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[21]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[22]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[23]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[24]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[25]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[26]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[27]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[28]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[29]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[30]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[31]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[32]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[33]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[34]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[35]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[36]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[37]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[38]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[39]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[40]/div[1]').click()
            script = "return arguments[0].scrollIntoView();";
            element = driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[41]/div[1]')
            driver.execute_script(script, element)
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[41]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[42]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[43]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[44]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[45]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[46]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[47]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[48]/div[1]').click()
            driver.find_element(By.XPATH,'//*[@id="bet_0_0_warpper"]/div/div[2]/div/div/ul/div[49]/div[1]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]").click()
            time.sleep(1)

            # 投注金额
            match(amount):
                case 1:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                case 2:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]").click() # 2 
                case 3:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]").click() # 3 
                case 4:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]").click() # 4 
                case 5:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]").click() # 5 
                case 6:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[3]").click() # 6 
                case 7:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[1]").click() # 7 
                case 8:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[2]").click() # 8 
                case 9:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[3]").click() # 9 
                case 10:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 20:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]").click() # 2 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 30:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]").click() # 3 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 40:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]").click() # 4 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 50:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]").click() # 5 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 60:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[3]").click() # 6 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 70:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[1]").click() # 7 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 80:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[2]").click() # 8 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 90:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[3]").click() # 9 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 100:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 110:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 120:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]").click() # 2 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 130:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]").click() # 3 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 140:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]").click() # 4 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 150:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]").click() # 5 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 160:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[3]").click() # 6 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 170:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[1]").click() # 7 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 180:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[2]").click() # 8 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 190:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[3]").click() # 9
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 200:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]").click() # 2 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 300:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]").click() # 3 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 400:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]").click() # 4 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 500:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]").click() # 5 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 600:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[3]").click() # 6 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 700:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[1]").click() # 7 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 800:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[2]").click() # 8 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 900:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[3]").click() # 9 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 1000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 2000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]").click() # 2 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 3000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[3]").click() # 3 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 4000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]").click() # 4 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 5000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]").click() # 5 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 6000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]/div[3]").click() # 6 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 7000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[1]").click() # 7 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 8000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[2]").click() # 8 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 9000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[3]/div[3]").click() # 9 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                case 10000:
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]").click() # 1 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
                    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[5]/div[2]").click() # 0 
            driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[3]").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[3]/div[2]/span[2]").click()
            time.sleep(25)
        except:
            pass
        periods = periods - 1

# 创建按钮并绑定事件
execute_button = tk.Button(root, text="执行", command=login_and_bet)
execute_button.grid(row=2, column=1, columnspan=2)

# 运行GUI界面
root.mainloop()