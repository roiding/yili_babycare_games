import logging
import os
import random
import sys
import time

import requests
import urllib3

# 关闭安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logging.basicConfig(level=logging.INFO,
                    filename=os.path.join(os.getcwd(), 'logs/shuafen.log'),
                    format='%(asctime)s - %(levelname)s: %(message)s')

game_level = 1
curr_score = 0
# 有4000个钻石就停止


def start_game(authorization):
    global game_level, curr_score
    while(curr_score <= 4000):
        # 请求头
        header = {'Host': 'babyclub.msxapi.digitalyili.com', 'Connection': 'keep-alive',
                  'Accept': 'application/json, text/plain, */*',
                  #   修改此处为自己的微信auth
                  'Authorization': 'XXXX',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
                  'Content-Type': 'application/json;charset=UTF-8',
                  'Sec-Fetch-Site': 'same-site',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Dest': 'empty',
                  'Referer': 'https://babyclub.msx.digitalyili.com//',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'en-us,en'}
        header['Authorization'] = authorization
        response = requests.get(
            "https://babyclub.msxapi.digitalyili.com/api/v1/game/play_auth", headers=header, verify=False)
        # 提交分数token
        score_token = response.json()['data']['score_token']
        game_level = response.json()['data']['game_level']
        logging.info("当前进度：%s",game_level)
        # 暂停60s 与游戏时间保持一致 防止被查
        time.sleep(60)
        request_data = {
            "score_type": "success",
            "auth_token": "723f4dca1fcf424b",
            "score": 115,
            "game_level": 31,
            "activity_ids": []
        }
        request_data['auth_token'] = score_token
        request_data['game_level'] = game_level+1
        request_data['score'] = 5*random.randint(19, 28)
        score_response = requests.post("https://babyclub.msxapi.digitalyili.com/api/v1/game/submit_score",
                                       json=request_data, headers=header, verify=False)
        logging.info("%s:成绩已提交:分数为%s",game_level,request_data['score'])
        curr_score = score_response.json()['data']['history_total_score']
        logging.info("当前共赚取%s钻石",curr_score)
        time.sleep(2)


if __name__ == '__main__':
    # 输入了auth值
    if len(sys.argv) == 2:
        logging.info("开始执行钻石获取")
        start_game(sys.argv[1])
    elif len(sys.argv) == 1:
        authorization = input("请输入你的微信登录Authorization值:")
        logging.info("开始执行钻石获取")
        start_game(authorization)
    else:
        logging.info("本程序只支持1个参数，请勿多输")
