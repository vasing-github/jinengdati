import hashlib

import time
import requests
import random
from datetime import datetime
from sendNotify import *
import userid
pmsg = {}


def submitAffair(user,prox):
    userid, name = user
    url = 'https://sczxdt.028hongtu.com/addons/exam/paper/submit_grade'
    shijianchuo = str(int(time.time() * 1000))
    radom_number = str(random.randint(0, 999))
    my = 'okMYL45A8ljLj5SfpIFaNerRTtSI'
    radom_goals = random.randint(40, 50)
    print(user,'\n')
    # for i in range(50 - radom_goals):
    #     addwrong(user,prox)
    #     time.sleep(random.randint(2, 5))

    data = {
        'cate_id': '3',
        'num': '50',
        'good_num': radom_goals,
        'goods_grade':radom_goals * 2 ,
        'token': hashlib.sha1((hashlib.md5((shijianchuo + radom_number).encode()).hexdigest() + my).encode()).hexdigest(),
        'str': shijianchuo,
        'radom': radom_number,
        'user_id': userid
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'sczxdt.028hongtu.com',
        'Origin': 'https://dt.028hongtu.com',
        'Referer': 'https://dt.028hongtu.com/',
        'Sec-Ch-Ua': '\"\"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '\"\"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/116.0.0.0'
    }
    response = requests.post(url, headers=headers, data=data, proxies=prox)
    if response.json()['status'] != 200:
        pmsg[name] = '状态：' + response.json()['result'] + '\t\t\t分数:0'
    else:
        pmsg[name] = '状态：' + response.json()['result'] + '\t\t\t分数:'+str(radom_goals * 2)

def addwrong(user,prox):
    userid, name = user
    url = 'https://sczxdt.028hongtu.com/addons/exam/question/wrongAdd'
    shijianchuo = str(int(time.time() * 1000))
    radom_number = str(random.randint(0, 999))
    my = 'okMYL45A8ljLj5SfpIFaNerRTtSI'
    radom_questionid = random.randint(1, 7810)

    data = {
        'question_id': radom_questionid,
        'token': hashlib.sha1((hashlib.md5((shijianchuo + radom_number).encode()).hexdigest() + my).encode()).hexdigest(),
        'str': shijianchuo,
        'radom': radom_number,
        'user_id': userid
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'sczxdt.028hongtu.com',
        'Origin': 'https://dt.028hongtu.com',
        'Referer': 'https://dt.028hongtu.com/',
        'Sec-Ch-Ua': '\"\"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '\"\"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/116.0.0.0'
    }
    requests.post(url, headers=headers, data=data,proxies=prox,timeout = 10)

def random_pick(d):
    if d:
        key = random.choice(list(d.keys()))
        value = d.pop(key)
        return key, value
    else:
        return None


i =1
users = userid.usersall
proxes =  userid.getproxies()
while users:
    user = random_pick(users)
    i += 1
    if i % 40 == 0:
        proxes = userid.getproxies()
    print(i)
    print(proxes)
    try:
        for j in range(5):
            addwrong(user, proxes)

    except Exception as e:
        print("错了一个",user,proxes)
        print(f'Error: {e}')
        proxes = userid.getproxies()
        users[user[0]] = user[1]
        continue

title = "??消息提醒：添加错题"
msg = f"?{str(datetime.now())[:19]}\n" + ''
for key, value in pmsg.items():
    msg += f"{key}: {value}\n"
send(title, msg)