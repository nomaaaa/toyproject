# -*- coding: utf-8 -*-
# 2022-01-02 start

import os,time
import requests,json

class default():
    def __init__(self):
        pass

    def run(self):
        #self.get_token()
        self.get_refresh_token()
        self.get_friends_list()

    # https://kauth.kakao.com/oauth/authorize?client_id=0e19086b0648722931961f1c9cac019f&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message,friends
    def get_token(self):
        url = 'https://kauth.kakao.com/oauth/token'
        rest_api_key = '0e19086b0648722931961f1c9cac019f'
        redirect_uri = 'https://localhost:3000'
        authorize_code = '2WFwxFpNOXVE86gf9BdNtQ19nbCamDz3lZnhtjpa_jhJrQEJfzzx6_AqPlpKylzoLSis2gopb1QAAAF-HTMQfg'
        
        data = {
            'grant_type':'authorization_code',
            'client_id':rest_api_key,
            'redirect_uri':redirect_uri,
            'code': authorize_code,
            }
        
        response = requests.post(url, data=data)
        tokens = response.json()
        print(tokens)
        
        # json 저장
        with open('kakao_code.json',"w") as fp:
            json.dump(tokens, fp)

    def get_refresh_token(self):
        url = "https://kauth.kakao.com/oauth/token"
        
        data = {
            "grant_type": "refresh_token",
            "client_id": "0e19086b0648722931961f1c9cac019f",
            "refresh_token": "2t_I16Fm97BmHbKVBWCIzYKU659a2qSSA_Q2KwopyNoAAAF-GWedYA"
        }
        response = requests.post(url, data=data)
        tokens = response.json()
        
        # kakao_code.json 파일 저장
        with open("kakao_token.json", "w") as fp:
            json.dump(tokens, fp)
    def get_friends_list(self):
        with open("kakao_token.json", "r") as fp:
            tokens = json.load(fp)    
            print(tokens["access_token"])

        url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
        header = {"Authorization": 'Bearer ' + tokens["access_token"]}
        
        result = json.loads(requests.get(url, headers=header).text)
        friends_list = result.get("elements")
        
        print(friends_list)
    
def main():
    try:
        DF = default()
        DF.run()
    except:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    stime = time.time()
    main()
    etime = time.time()
    print(round(etime-stime,3),' eclapsed')

