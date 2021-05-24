# -*- coding: UTF-8 -*-
import requests as req
import json, os, random

# 系统变量
gh_token = os.getenv('GH_TOKEN')
gh_repo = os.getenv('GH_REPO')
ms_token = os.getenv('MS_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


# 获取token
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
            jsontxt = json.loads(html.text)
            return jsontxt['access_token']
        else:
            if retry_ == 3:
                print(r'微软密钥获取失败')
    return ""


def main(access_token):
    num = 0
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    url_list = [
        "https://graph.microsoft.com/v1.0/me/",
        "https://graph.microsoft.com/v1.0/users",
        "https://graph.microsoft.com/v1.0/me/people",
        "https://graph.microsoft.com/v1.0/groups",
        "https://graph.microsoft.com/v1.0/me/contacts",
        "https://graph.microsoft.com/v1.0/me/drive/root",
        "https://graph.microsoft.com/v1.0/me/drive/root/children",
        "https://graph.microsoft.com/v1.0/drive/root",
        "https://graph.microsoft.com/v1.0/me/drive",
        "https://graph.microsoft.com/v1.0/me/drive/recent",
        "https://graph.microsoft.com/v1.0/me/drive/sharedWithMe",
        "https://graph.microsoft.com/v1.0/me/calendars",
        "https://graph.microsoft.com/v1.0/me/events",
        "https://graph.microsoft.com/v1.0/sites/root",
        "https://graph.microsoft.com/v1.0/sites/root/sites",
        "https://graph.microsoft.com/v1.0/sites/root/drives",
        "https://graph.microsoft.com/v1.0/sites/root/columns",
        "https://graph.microsoft.com/v1.0/me/onenote/notebooks",
        "https://graph.microsoft.com/v1.0/me/onenote/sections",
        "https://graph.microsoft.com/v1.0/me/onenote/pages",
        "https://graph.microsoft.com/v1.0/me/messages",
        "https://graph.microsoft.com/v1.0/me/mailFolders",
        "https://graph.microsoft.com/v1.0/me/outlook/masterCategories",
        "https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta",
        "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules",
        "https://graph.microsoft.com/v1.0/me/messages?$filter=importance eq 'high'",
        "https://graph.microsoft.com/v1.0/me/messages?$search='hello world'",
        "https://graph.microsoft.com/beta/me/messages?$select=internetMessageHeaders&$top",
        "https://api.powerbi.com/v1.0/myorg/apps",
    ]
    # 执行随机条url
    for i in range(random.randint(1, len(url_list))):
        # 随机url
        get_url = random.randint[random.randint(0, len(url_list) - 1)]
        try:
            if req.get(get_url, headers=headers).status_code == 200:
                num += 1
            else:
                # 错误打印
                print(get_url)
        except Exception as e:
            print(e)
    return num


if __name__ == '__main__':
    access_token = getmstoken()
    for _ in range(random.randint(5, 20)):
        success_num = main(access_token)
        print("执行", success_num, "条url")
