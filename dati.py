import hashlib

import time
import requests
import random
from datetime import datetime
from sendNotify import *
import userid
pmsg = {}


def submitAffair(user,prox,rand):
    userid, name = user
    url = 'https://sczxdt.028hongtu.com/addons/exam/paper/submit_grade'
    shijianchuo = str(int(time.time() * 1000))
    radom_number = str(random.randint(0, 999))
    my = 'okMYL45A8ljLj5SfpIFaNerRTtSI'
    radom_goals = 50 if rand  else random.randint(20, 45)
    print("分数：",radom_goals)
    print(rand)
    print(user,'\n')

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
    response = requests.post(url, headers=headers, data=data, proxies=prox,timeout=10)
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
    requests.post(url, headers=headers, data=data,proxies=prox,timeout=10)

def random_pick(d):
    if d:
        key = random.choice(list(d.keys()))
        value = d.pop(key)
        return key, value
    else:
        return None
if __name__ == '__main__':
    i =1
    users = {'oSHH802t16mrBQJnYDGg9GCiMRAw': '文苏梅', 'oSHH809gP-12u_i4uH-51QbNigWU': '赵容', 'oSHH80x55QXiXgAZFpPt-IiPThhc': '刘琼英', 'oSHH802WPt2-2415xAmFo_aM4bvQ': '魏永红', 'oSHH80wVFzMcALn4UrJ6CwJMDQX0': '王广', 'oSHH803qAVFPoSDq2A8b0to1v7VM': '周定贵', 'oSHH80_KcsZrkeF12ckwgIq7uxjw': '杜明哲', 'oSHH80yH41smJNMTtL_Jn_NMDRII': '苏洲', 'oSHH8051VG25I4vLMWXqtKsF6P3c': '何洪禄', 'oSHH8052qROxj6uvnMalTjA8rztg': '秦秋菊', 'oSHH80_msmw69UVcAYLBIMLv4Qa8': '陈明', 'oSHH80zZ-65QwWyzXieO5WbxPlV8': '朱伟婷', 'oSHH804nirwPseq73_L2iEoX_F9k': '唐思兵', 'oSHH801RTEj6YwzYbK67dhznjA1M': '赵森林', 'oSHH807zndjRKC2V3eeJ-QfEHx1c': '胡峰', 'oSHH80zgTxg_6ontPa7kLENI5ah4': '李明广', 'oSHH801E6f9LmEeQ2nKVGpwpighk': '谷爱珍', 'oSHH80221yNpQ2NHCOyXUizTQjmE': '谷长军', 'oSHH803gkfZjbzE8VR_R4H5AmaKU': '李霞', 'oSHH8093Ani5vs6CeOQG0X_ewQLg': '田辉钊', 'oSHH802W0ScIsoJB696EKz9cqUvE': '王红', 'oSHH8035IAmAzEos-VK3521y-sWc': '任晓玲', 'oSHH80xFqDMgQk5hc5XW1cHeZtvw': '赵艺榕', 'oSHH80y-tGP8qSW6pgOHEaB0AlsI': '张洪胜', 'oSHH80_inFy12ic8_LOCKgucLlKM': '张洪源', 'oSHH8029_KQhel4ei6XkMKg42OOA': '张鹏飞', 'oSHH801H2t-xwI4f_G2R8HPO6fhM': '张仁杰', 'oSHH800XSi6w-5RDjbg_BaRZSqXI': '岳俭君', 'oSHH807d2zvJMuzxHVq2HGdPJBIs': '李明鉴', 'oSHH801gWaooPFHkfiG8UPJ79NUo': '陈佳', 'oSHH8016hlZN6C04-oxEiVuPHOT4': '王峰', 'oSHH803Qmxcl7lFyVo3IXmq0t7PA': '王峰一', 'oSHH803Nb8r6LEOpXebejv0o5DlQ': '吴小静', 'oSHH801gPpGoFzcYipDQWd-llhdo': '赵颖', 'oSHH80y1lr9Yk6nM8qkMcjOX1eOY': '张森', 'oSHH80_XV1T7Njtvx4DNLhVOjLy0': '蒲浩格', 'oSHH800HLCzBrl2ZMWyM6y2w6zQ0': '刘兰', 'oSHH804nElW-NxUSx9SAaB0Iqq1g': '杨大杰', 'oSHH80_dcXxA05NJFs4oi8MdgBow': '吴尚可', 'oSHH805_rMjuDUrT37Az50Qaf5kM': '张淇', 'oSHH801TwA7RYug6ZyeMPb4Gwpdg': '邹焱', 'oSHH802Ystrev1yTdKGouztZLN2Q': '魏松', 'oSHH808zHzs528oIYEB6Qs8WugpE': '王天申', 'oSHH803Xx3IZZEDXmUbMYOjaDN7g': '徐珠波', 'oSHH80z6LwfYi3JiRiKe32SYGoho': '杨博文', 'oSHH80-GsYTJG_dO3EMGu2Cg6hn0': '王杰', 'oSHH806CAm3NpkOo2NrkSOO42BsI': '吴鑫', 'oSHH80zpOfi2IMyqIeaxiJgeYvPI': '胡海英', 'oSHH80wPDnldorCZFQO0_luTtJaI': '邱家', 'oSHH805h8mpeC3HrBc9anB2M7D4E': '邱家', 'oSHH80_UjWiIQa0e35Le0_gOE9sk': '张岭韬', 'oSHH804ARfYBE5KGA1fIAMhRWvPA': '孙晓菊', 'oSHH8052f2pJruSkjOGYSQ7u4MOY': '苏琼', 'oSHH80yf1R6sSVZYspnTs4n4QTD8': '张莉', 'oSHH80-jA_B6k8ieA02AIMaieRNg': '冯华章', 'oSHH808XqrqHfhAPLAlPSOROaMig': '王秋悦', 'oSHH80wXaR2FinuvOWb2HD3xILD0': '谢金凤', 'oSHH80wbKwCoP29NVMltKoKdIWQc': '唐彬', 'oSHH800mVClkJV9hlFEcwRDll6Nk': '岳琳', 'oSHH80-LN_KeclagUO7rcMnKeuLM': '魏佳邑', 'oSHH804UScUArlNIj2O9EIOw8tLE': '陈刚', 'oSHH803V-NhvG6o7wyFPJlRB5iD8': '魏吕鹏', 'oSHH80xoDdNVTCAl0v54qmhZT3oQ': '吴海林', 'oSHH803ks5vXp3inDPJeT2Cwh6k4': '邓川东', 'oSHH8022mGhxYuszC9NGkeXOpS4k': '马晶晶', 'oSHH80zQV5FXfrCDcumwnBtFAkV4': '王延英', 'oSHH80wRiqcvn4hde2xE2RYA44Jw': '刘峰', 'oSHH807oZC0u2U0fUqtpXVk4McDM': '王德文', 'oSHH806_YYT8M7i8yMPYT_5EvFbg': '吴彪', 'oSHH803Dni_e0sAsw_4Olhd7zH8k': '王文渊', 'oSHH806SmOLcTRdYzq8gG-5JKO2o': '蔺易', 'oSHH803m_Bt-Zh3e747SnZCfbYs0': '易守乾', 'oSHH80y2j92rG_oCI_VWaF0mmDh4': '韩泰然', 'oSHH806YDdtZdZ5wSEddTI-5UHuk': '冯剑波', 'oSHH80_NjXRds-HbOo9Gv0Ou49HY': '苏琢', 'oSHH802Pdbln6xZx5h_ySZj-600Y': '汪勇', 'oSHH809QAFM4zXaUz7nS1Km2ENpc': '苟志平', 'oSHH80ymcW8cL0B5Px-3eMadmnRc': '何茂功', 'oSHH80yuPTSOiswFR3QvqaQcX30s': '刘银山', 'oSHH8056YsmpRMeAZMxn2K_c35To': '李智亮', 'oSHH802VfcBYKz1_OTbDTrd8J3CQ': '何晓丽', 'oSHH80xDapMo6uoeB836TpJr0yAI': '魏晓芳', 'oSHH80yruu1UUhgvQLLVKV9PQQlE': '王丽婷', 'oSHH80zZYVf7BcNJ9ZYOsRZtNLt4': '李静', 'oSHH80wJWR4QD-xbW0nrPecyxxNQ': '马荣华', 'oSHH80980Ub3C7txmQP2F0CFNWdc': '李小芳', 'oSHH80yH3VaMFrWeXofzDxqY2M50': '夏红梅', 'oSHH802DtCK4KlELW8ddX65oirNc': '李坤', 'oSHH80z9LjRZcsGpIEOiB4p1AP_M': '冯玉华', 'oSHH802eX3bAOFCKk62Ib9c8kQgo': '孙鹏', 'oSHH805PR28INHN_ipYFDOJ0iZzU': '王圆圆', 'oSHH805B2sYSazb3xkvBcYTSmp9E': '李玉山', 'oSHH80xi3CX9rcfB4twU0iwpeJK4': '杨志强', 'oSHH80wtD2337LOs3rHaUe0kyMnY': '何明俊', 'oSHH805RBqUWi2AzQ1DaGWWDhrGQ': '张海', 'oSHH80wHLWKEtoyN_lbyLj7NLlaM': '白燕', 'oSHH80xzb128FepE7-8GnKLdITuw': '吴天冬', 'oSHH802oiav_4WG_ZfZGBKyFaFyE': '王德明', 'oSHH807NozmKph8Y5peMZ9imfuOc': '王雪梅', 'oSHH804W3McqA77LWLSKyJX8HCNg': '向瑶', 'oSHH807nDW6ERCIrtPsKC87jNPBc': '孙波', 'oSHH803KRE9yoQEIwwhukTQ8jPoA': '王珍平', 'oSHH80x9swohhPZwkWKykEQ0DVKk': '赵高峰', 'oSHH809O2CO98IRHThlqse896JFY': '苟志平', 'oSHH8066bISJ915pK7nL2BRLsQvU': '王伯承', 'oSHH801Vg8jXcQhC0VM2P2L4w2uc': '白云', 'oSHH800mzWcmt7FnIPJx3GolTlIE': '白海波', 'oSHH802n1ICvOY8qB3AWvY3SEQiQ': '王咪', 'oSHH80xVrNlvxttmG8Y5llSL7tDw': '何鸿', 'oSHH801QwevLNnQ1Mo_a2Sf2jM-4': '赵佳楠', 'oSHH80178lckTomsOzUp5Jowjogc': '唐燕', 'oSHH80wzBITcxIZj_zUmwOXVvoY0': '王婧婧', 'oSHH809UyICYIPfx_Hnmbcza7Ilc': '杨镇涛', 'oSHH808COqScDu_ShKe_MZWWEoRw': '蔡凤琼', 'oSHH808bKN6bMIhKlEstzcE4qbnM': '张蓝心', 'oSHH804a1HIODyZa8VwPjSvW3HY4': '谢中华', 'oSHH805Pm4UfGRVuYtJy_VLu-XIo': '张灿', 'oSHH809DASYAzmc1XqHUuvT4jD_c': '王珊', 'oSHH801pmFH5ZBUdfCkyRK1yn-Xw': '邱小丽', 'oSHH805IFPABpAoyxeHC7TxT0up4': '张洁', 'oSHH80y0qcv521N5u3m5IY1eEQng': '杨华', 'oSHH80_AAAMtLayPSezYDQECNkt0': '秦峰', 'oSHH806h4RZtMIT0dAooUsf2wheo': '向本上', 'oSHH800_viosMF_kUfb-ANqyjlok': '杜正伟', 'oSHH80-3Rrqi0FIbMl-9tJ0WNMRc': '李勇平', 'oSHH80w3HkTPftHw6UNZ2yvLu9to': '苏均成'}

    proxes = userid.getproxies()
    while users:
        user = random_pick(users)
        i += 1
        # if i % 40 == 0:
        #     proxes = userid.getproxies()
        print(i)
        print(proxes)
        try:
                if user[0] in userid.userspecial:
                    submitAffair(user, proxes, rand=True)
                else:
                    submitAffair(user, None, rand=False)
        except Exception as e:
                print("错了一个",user,proxes)
                print(f'Error: {e}')
                proxes =  userid.getproxies()
                users[user[0]] = user[1]
                continue

    title = "??消息提醒：技能答题"
    msg = f"?{str(datetime.now())[:19]}\n" + ''
    for key, value in pmsg.items():
        msg += f"{key}: {value}\n"
    send(title, msg)