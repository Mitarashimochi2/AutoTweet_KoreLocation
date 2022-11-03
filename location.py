
from sre_constants import SUCCESS
from urllib import response
import requests
import os
import json
import schedule
import tweepy
import time

# To set your enviornment variables in your terminal run the following line:

bearer_token = "YOUR BEARER_TOKEN"

# 認証に必要なキーとトークン
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



def create_url():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=korekore19"
    user_fields = "user.fields=location"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()



def write():
    url = create_url()
    #位置情報の文字列
    json_response = connect_to_endpoint(url)

    #開く
    f = open("location.txt", "a")
    #書き込み
    f.write( "\n" + json_response["data"][0]["location"])
    f.close()

    print("書き込まれた")





class main:
    #読み込む関数
    def __init__(self):
        #最新の行だけ開いて読む
        with open('location.txt', "r") as f:
            for line in f:
                pass
            self.last = line
        print(self.last)

        print("読み込まれた")


    def get(self):

        api = tweepy.API(auth)

        #プロフィールJSONの取得
        url = create_url()
        json_response = connect_to_endpoint(url)
        #位置情報のみに整形
        kore_now = json_response["data"][0]["location"]

        #最新のリストの位置情報を読み込む
        self.__init__()
        if kore_now != self.last:
            #ツイート
            api.update_status("😷位置情報が更新されました😷 \n " + " \nコレコレ\n「" + kore_now + "」 \n" + " \n更新前は \n「" + self.last + "」でした \n" + " \n#コレコレ")
            write()
            print("【一致しなかったのでツイートされました】")
            print("位置情報:" + kore_now + "リストの最後:" + self.last)

        elif kore_now == self.last:
            print("【一致したのでツイートされませんでした】")
            print("位置情報:" + kore_now + "リストの最後:" + self.last)
            pass
        else:
            print("【エラー】")
            print("位置情報:" + kore_now + "リストの最後:" + self.last)
            


write()
out = main()

#読み込みとツイート判断の繰り返し
schedule.every(1).minutes.do(out.get)

while True:
    schedule.run_pending()
    time.sleep(5)





