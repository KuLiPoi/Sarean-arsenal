# 用于青龙面板的任务
# 青龙面板需要满足以下条件：
# docker镜像必须使用【whyour/qinglong:debian】，否则依赖无法安装。
# 请安装【requirement.txt】内的Python依赖
# 请安装【zbar-tools】linux依赖
# 请确保已经填写好【config.ini】配置文件，此任务将不会引导您填写配置文件。
import configparser

from Utility.sqMall import sqMallDoSign as sqMallSign
from Utility.risingStones import signIn as rs_signin
from Utility.risingStones import rs_login
from Utility.risingStones import getSignReward as getSignReward
from Utility.risingStones.rs_login import is_rs_login as rs_userInfo

sqMallSign.main()

noc_config = configparser.RawConfigParser()
noc_config.read('config.ini', encoding='utf-8')
if noc_config.get('Notification', 'noc-enable') == 'True':
    import Utility.Notifications.push as pusher

    rs_cookies = rs_login.login()
    rs_result = rs_signin.rs_signin(rs_cookies)
    rs_reward = getSignReward.getReward(rs_cookies)
    userInfo = rs_userInfo(rs_cookies)["msg"]
    accountinfo = "当前登录账户:" + userInfo["character_name"] + "@" + userInfo["group_name"]
    pusher.push('石之家任务结果', accountinfo + '\n' + str(rs_result) + '\n' + str(rs_reward))
else:
    rs_cookies = rs_login.login()
    rs_result = rs_signin.rs_signin(rs_cookies)
    rs_reward = getSignReward.getReward(rs_cookies)
    userInfo = rs_userInfo(rs_cookies)["msg"]
    accountinfo = "当前登录账户:" + userInfo["character_name"] + "@" + userInfo["group_name"]
    print('石之家任务结果', accountinfo + '\n' + str(rs_result) + '\n' + str(rs_reward))
