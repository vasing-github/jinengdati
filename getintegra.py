import random
from datetime import datetime
from sendNotify import *
import userid
pmsg = {}
allcode = 0
def submitAffair(user,prox):
    global allcode
    userid, name = user
    url = 'https://sczxdt.028hongtu.com/addons/exam/question/get_integral'
    shijianchuo = str(int(time.time() * 1000))
    radom_number = str(random.randint(0, 999))
    my = 'okMYL45A8ljLj5SfpIFaNerRTtSI'

    data = {
        'page': 1,
        'limit': 20,
        'token': hashlib.sha1((hashlib.md5((shijianchuo + radom_number).encode()).hexdigest() + my).encode()).hexdigest(),
        'str': shijianchuo,
        'radom': radom_number,
        'user_id': userid
    }

    headers = {
        'authority': 'sczxdt.028hongtu.com',
        'method': 'POST',
        'path': '/addons/exam/question/get_integral',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '127',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://dt.028hongtu.com',
        'Referer': 'https://dt.028hongtu.com/',
        'Sec-Ch-Ua': '',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': (
            'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/116.0.0.0')
    }
    print(user)
    response = requests.post(url, headers=headers, data=data, proxies=prox,timeout=10)
    print(response.text)
    allgoals = 0
    if response.json()['status'] != 200:
        print("cuole")
    else:
        for item in response.json()['result']:
            allgoals += item["num"]
        allcode += allgoals
        pmsg[name] = '积分：' + str(allgoals)
def get_random_proxy():
    response = requests.get(
        'https://dps.kdlapi.com/api/getdps/?secret_id=owbh0fuoz2h61zjhloyj&num=1&signature=nhwyduwme4yr1cad21d6v4kfxw2zwuwm&pt=1&sep=1')
    proxies = {
        'http': response.text,
        'https': response.text,
    }
    return proxies

def random_pick(d):
    if d:
        key = random.choice(list(d.keys()))
        value = d.pop(key)
        return key, value
    else:
        return None
i =1
users = userid.usersall
proxes =  {'http': '106.119.160.179:16816', 'https': '106.119.160.179:16816'}
while users:
    user = random_pick(users)
    i += 1
    # if i % 6 == 0:
    #     proxes = get_random_proxy()
    print(i)
    print(proxes)
    try:
        submitAffair(user,proxes)
        time.sleep(random.randint(2, 5))
    except Exception as e:
        print("错了一个",user,proxes)
        print(f'Error: {e}')
        proxes = get_random_proxy()
        users[user[0]] = user[1]
        continue

title = "??消息提醒：分数统计"
msg = f"?{str(datetime.now())[:19]}\n" + ''
msg += f"累计刷分：{allcode}\n\n"
# for key, value in pmsg.items():
#     msg += f"{key}: {value}\n"
print(f"累计刷分：{allcode}\n\n")
send(title, msg)