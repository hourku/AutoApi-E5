# -*- coding: UTF-8 -*-
import requests as req
import json, os, time, random

gh_token = os.getenv('GH_TOKEN')
gh_repo = os.getenv('GH_REPO')
ms_token = os.getenv('MS_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

num = 0

def getmstoken():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': ms_token,
        'client_id': client_id,
        'client_secret': client_secret
    }
    for retry_ in range(4):
        html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
        if html.status_code < 300:
            print(r'微软密钥获取成功')
            break
        else:
            if retry_ == 3:
                print(r'微软密钥获取失败')
    jsontxt = json.loads(html.text)
    return jsontxt['access_token']


def main():
    global num
    localtime = time.asctime(time.localtime(time.time()))
    access_token = getmstoken()
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root', headers=headers).status_code == 200:
            num += 1
            print("1调用成功" + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive', headers=headers).status_code == 200:
            num += 1
            print("2调用成功" + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root', headers=headers).status_code == 200:
            num += 1
            print('3调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/users ', headers=headers).status_code == 200:
            num += 1
            print('4调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages', headers=headers).status_code == 200:
            num += 1
            print('5调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
                   headers=headers).status_code == 200:
            num += 1
            print('6调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
                   headers=headers).status_code == 200:
            num += 1
            print('7调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers).status_code == 200:
            num += 1
            print('8调用成功' + str(num) + '次')
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps', headers=headers).status_code == 200:
            num += 1
            print('8调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders', headers=headers).status_code == 200:
            num += 1
            print('9调用成功' + str(num) + '次')
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories', headers=headers).status_code == 200:
            num += 1
            print('10调用成功' + str(num) + '次')
            print('此次运行时间为 :', localtime)
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    for _ in range(random.randint(10, 100)):
        main()
