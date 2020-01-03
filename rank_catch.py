# -*- coding: utf-8 -*-

import os, time, requests, urllib
from datetime import datetime

class default():
    def __init__(self):
        pass

    def run(self):
        now_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        max_page = 40 
        keyword_ko = '전기면도기'
        keyword_en = urllib.quote(keyword_ko)
        store_name = '어니스트원'
        
        
        for page in range(1,max_page,1):
            url='https://search.shopping.naver.com/search/all.nhn?origQuery='+'%s' % keyword_en+'&pagingIndex='+'%s' % page+'&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EC%A0%84%EA%B8%B0%EB%A9%B4%EB%8F%84%EA%B8%B0' 

            payload = {'key1': 'value1', 'key2': 'value2'}
            r = requests.post(url, data=payload)
            result = r.text
            enc_result = result.encode('utf8')
            if enc_result.find('%s' % store_name) > -1:
                print '%s 키워드: %s page : %s\n' % (now_time,keyword_ko,page)
                file=open('ranking.txt','a')
                file.write('%s 키워드: %s page : %s\n' % (now_time,keyword_ko,page))
                file.close()
def main():
    DF = default()
    DF.run()

if __name__ == "__main__":
    stime = time.time()
    main()
    etime = time.time()
    print round(etime-stime,3),' eclapsed'

