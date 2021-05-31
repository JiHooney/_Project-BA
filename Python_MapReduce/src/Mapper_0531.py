#!/usr/bin/env python3

import sys  #시스템 패키지
import datetime #문자열을 날짜형식변환 패키지
from dateutil.relativedelta import relativedelta    #3개월 빼주는 패키지
import re   #정규식 패키지
from konlpy.tag import Okt    #형태소 분석 패키지


#테스트하기 위해서 2페이지만 긁어온 파일 읽기
f = open( './test.txt', 'r')
lines = f.readlines()

outVal = 1

#for line in sys.stdin:
for line in lines:
    line = line.strip() #라인 뒤에 붙어있는 공백제거
    col = line.split( '|||' )   #|||를 기준으로 리스트로 나눔
    
         ###1. 한 분기(3개월)의 글만 추출하기 시작
    date = col[0][:-1]
    date_tmp = datetime.datetime.strptime( date, "%Y.%m.%d" )   #3개월전 월을 구하기 위한 변수
    
    now_month = str( date[5:7] )    #현재 월
    end_month = str( ( date_tmp - relativedelta(months=3) ) )[5:7]  #3개월 전의 월
    
          #월 비교
    if now_month != end_month:  #현재월과 3개월전의 월이 같으면 반복문 종료
                    ###2. 정규표현식으로 한글 외의 문자 제거 시작
        con = re.compile( '[가-힣]+' ).findall( col[1] + col[2] ) #한글만 남기면서 단어들로 분리
        content = ''
        for s in con: content = content + s + ' '
        
                    #형태소 객체생성
        okt = Okt()
        print( okt.pos(content) )
                
                
        #print( content )
    else:
        break
    #print( now_month )
    # print( content )
    
    
#리듀서로 보내질 매퍼의 결과물
print()
    
    