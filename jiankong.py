import logging
import os
import re
import sys
import time

import requests
import urllib3

# 关闭安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.INFO,
                    filename=os.path.join(os.getcwd(), 'logs/jiankong.log'),
                    format='%(asctime)s - %(levelname)s: %(message)s')


def checkCount(token):
    i = 0
    while(True):
        try:
            i = i+1
            # 请求url,解析变量值
            response = requests.get(
                "https://www.yilibabyclub.com/malldetail.aspx?dataid=300406&giftid=8075&code=202206002", verify=False, proxies={'https': None})
            count_str = re.findall("var giftcount = (\d+);", response.text)

            count_int = int(count_str[0])

            logging.info("执行第%s次,当前库存%s", i, count_int)

            if(count_int != 0):
                # 执行通知
                data = {"title": "所选商品有货了", "desp": "所选设备已有，赶快去抢啊"}
                url = "https://sctapi.ftqq.com/"+token+".send"
                data = requests.post(
                    url, params=data, proxies={'https': None})
                break
            time.sleep(30)
        except:
            logging.info("发生异常")

if __name__ == '__main__':
    # 输入了token值
    if len(sys.argv) == 2:
        logging.info("开始执行库存监控")
        checkCount(sys.argv[1])
    elif len(sys.argv) == 1:
        sendKey = input("请输入你的Server酱SendKey值:")
        logging.info("开始执行库存监控")
        checkCount(sendKey)
    else:
        logging.info("本程序只支持1个参数，请勿多输")
