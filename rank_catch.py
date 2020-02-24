# -*- coding: utf-8 -*-

import os, time, requests, urllib
from datetime import datetime

class default():
    def __init__(self):
        pass

    def run(self):
        now_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        max_page = 30 
        keyword_ko = '마블 케이스'
        keyword_en = urllib.parse.quote(keyword_ko)
        store_name = '유니폰'
        count = 0
        
        
        for page in range(1,max_page,1):
            count +=1
            print(count)

            url='https://search.shopping.naver.com/search/all.nhn?origQuery='+'%s' % keyword_en+'&pagingIndex='+'%s' % page +'&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EB%A7%88%EB%B8%94%20%EC%BC%80%EC%9D%B4%EC%8A%A4'

            payload = {'key1': 'value1', 'key2': 'value2'}
            r = requests.post(url, data=payload)
            result = r.text
            #enc_result = result.encode('utf8')
            #enc_result = enc_result.decode()
            #if enc_result.find('%s' % store_name) > -1:
            if result.find('%s' % store_name) > -1:
                print('%s 키워드: %s page : %s\n' % (now_time,keyword_ko,page))
                file=open('ranking.txt','a')
                print('rankin.txt make success')
                file.write('%s 키워드: %s page : %s\n' % (now_time,keyword_ko,page))
                file.close()
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

