import os
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys 
from datetime import datetime
import time 
import pyperclip
import re
 

 

#####로그인하기(우회해서)
driver = webdriver.Chrome('C:\\chromedriver_win32\chromedriver')


uid = 'ieese12' 
upw = 'nadnr!23' #네이버 로그인 페이지로 이동 
 

url = ('https://nid.naver.com/nidlogin.login')
 

driver.get(url) 
time.sleep(2) #로딩 대기 


#아이디 입력폼 
tag_id = driver.find_element_by_name('id') 
#패스워드 입력폼 
tag_pw = driver.find_element_by_name('pw') 
 

 

# id 입력 
# 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기 
tag_id.click() 
pyperclip.copy(uid) 
tag_id.send_keys(Keys.CONTROL, 'v') 
time.sleep(1)

 

# pw 입력 
# 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기 
tag_pw.click() 
pyperclip.copy(upw) 
tag_pw.send_keys(Keys.CONTROL, 'v') 
time.sleep(1) 


 

#로그인 버튼 클릭 
login_btn = driver.find_element_by_id('log.login') 
login_btn.click() 
time.sleep(2)
 

 

######네이버 카페 옷 착샷 페이지로 이동

#페이지이동 함수
def move_page( page ):
    key_url = 'https://cafe.naver.com/casuallydressed?iframe_url=/ArticleList.nhn%3Fsearch.clubid=19943558%26search.menuid=79%26search.boardtype=I%26search.totalCount=201%26search.page={}'.format(page)
    return key_url

data = []  #전체 게시글을 담을 리스트

##페이지 반복
for i in range( 1, 101 ):
    url = move_page( i )
    driver.get( url )
    
    #소스를 뽑아내기 위해 프레임 변경
    driver.switch_to.frame('cafe_main')
    
    search_url = driver.page_source
    soup = BeautifulSoup(search_url, 'html.parser')
    
    subj_locate = '#main-area > ul.article-album-sub > li:nth-child(n) > dl > dt > a.tit > span > span'
    subjects = soup.select(subj_locate)

    #print( subjects ) 
    
    #제목을 순회하면서 제목, 날짜를 긁어온다.
    for subject in subjects:
        d = []  #게시글 하나의 제목과 날짜를 임시로 담을 리스트

        ## 제목
        sub = subject.text.strip()
        d.append( sub )
        d.append( '|||' )
        
        
        ##날짜
        date_locate = '#main-area > ul.article-album-sub > li:nth-child(n) > dl > dd.date_num > span.date'
        date = soup.select(date_locate)
        date = date[0].getText().strip()
        
        if len(date) <= 5:  #오늘 글쓴 경우 시간만 나오므로 오늘 날짜로 변경해준다.
            date = datetime.today().strftime( "%Y.%m.%d." )
            
        d.append(date)
        
        
        data.append(d)  #최종적으로 d리스트에 있는 값들을 data리스트에 저장한다.
        
        print( d )



c = os.path.exists( 'test.txt' )    
if c:
    os.remove( 'test.txt' )
        
#텍스트파일로 저장
with open( 'test_brand.txt', 'w', encoding='utf-8' ) as f:
    for line in data:
        for l in line:
            f.write( l )
        f.write( '\n' )

