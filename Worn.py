# -*- coding: UTF-8 -*-
"""
@version: python-3.6
@author: lcz
@software: PyCharm
@time: 2020/2/6 18:01
"""
import time
from selenium import webdriver
import re
import sys

# #输入追溯码81207010336641484932

# 模拟访问
if __name__ == '__main__':

#     for i in range(1, len(sys.argv)):
#         key = sys.argv[i]
    key = "81207010336641484932"
    print(key)

    # 模拟访问
    opt = webdriver.ChromeOptions()
    #opt.add_argument("--proxy-server=221.2.175.238:8060")
    opt.add_argument("--headless")
    opt.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    opt.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=opt)
    driver.get('http://www.mashangfangxin.com/')
    #time.sleep(2)
    driver.find_element_by_id('scanCode').send_keys(key)  # 要查询的追溯码
    driver.find_element_by_class_name('code-btn').click()
    time.sleep(2)
    html = driver.page_source
    driver.close()
    driver.quit()

    notFound = re.findall(r'<div class="abnormal-exc">(.*?)</div>',html,re.S)[0]
    if notFound == '该药品未入驻“码上放心”，系统查无此码':
        print("-1")
    elif notFound == 'SM':
        print("-2")
    else:
        # 匹配对应的信息
        al = re.findall(r'<div class="drugDosage">(.*?)<div class="drugVerification">', html, re.S)[0]
        time = re.findall(r'<div class="text">(.*?)</div>', al, re.S)[0]
        dl = re.findall(r'<div class="drugVerification">(.*?)<script type="text/tmpl" id="main-tmpl">', html, re.S)[0]
        list = re.findall(r'<td class=.*?>(.*?)</td>', dl)
        # 清楚冗杂
        time = time.replace(" ", "")
        time = time.replace("\n", "")
        time = time.replace("\t", "")
        time = time.replace("\t\n", "")
        # 输出最后的结果
        druginfo={
            'drugid': '',
            'sourcecode': '',
            'expirytime': list[-1],
            'name': list[1],
            'producer': list[9],
            'form': list[5]
        }
        print(druginfo)