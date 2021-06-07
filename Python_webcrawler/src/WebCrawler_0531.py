from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys 
import time 
import pyperclip
import re


#####로그인하기(우회해서)
driver = webdriver.Chrome('chromedriver')

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


######네이버 카페로 이동
driver.get('https://cafe.naver.com/casuallydressed')



#페이지 이동 함수 구축
#검색어 인코딩 및 문자치환하기
keyword = input()
keyword_ogn = keyword
keyword = keyword.encode('MS949')
keyword = str(keyword)
keyword = keyword.replace('\\x', '%')
keyword = keyword[2:-1]

#페이지이동 함수
def move_page(keyword,page):
    key_url = 'https://cafe.naver.com/casuallydressed?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=19943558%26search.media=0%26search.searchdate=all%26search.defaultValue=1%26search.exact=%26search.include=%26userDisplay=15%26search.exclude=%26search.option=0%26search.sortBy=date%26search.searchBy=1%26search.includeAll=%26search.query={}%26search.viewtype=title%26search.page={}'.format(keyword,page)
    return key_url
 

contents_temp = [] #내용저장배열
subjects_temp = [] #제목저장배열
dates_temp = [] #날짜저장배열

data = [] 

# 크롤링 / 리눅스기준 한 페이지 긁어오는데 약 1분 10초
for page in range(1,2):
    url = move_page(keyword, page)
    driver.get(url)
         # 프레임 변경

    driver.switch_to.frame('cafe_main')

    n = 1

#     if page == 1 :
#         driver.find_element_by_xpath('//*[@id="currentSearchByTop"]').click()
#         driver.find_element_by_xpath('//*[@id="sl_general"]/li[2]/a').click()
#         driver.find_element_by_xpath('//*[@id="main-area"]/div[1]/div[1]/form/div[4]/button').click()

    search_url = driver.page_source
    soup = BeautifulSoup(search_url, 'html.parser')

          # 제목 추출
    subj_locate = '#main-area > div:nth-child(n) > table > tbody > tr:nth-child(n) > td.td_article > div.board-list > div > a.article'
    subjects = soup.select(subj_locate)
    
    for subject in subjects:
        d = []
        
                   ##날짜
        date_locate = '#main-area > div:nth-child(7) > table > tbody > tr:nth-child({}) > td.td_date'.format(n)
        date = soup.select(date_locate)
        date = date[0].getText().strip()
        d.append(date)
        d.append( '|||' )
        


                     ## 제목
        sub = subject.text.strip()
        d.append( sub )
        d.append( '|||' )

                    ##내용
        content_link = subject.attrs['href']
        content_link = 'http://cafe.naver.com' + content_link
        driver.get(content_link)
        
                    #프레임 변경
        driver.switch_to.default_content()
        time.sleep(0.5)
        driver.switch_to.frame('cafe_main')

        time.sleep(0.5)
        content = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div').text

        content = content.replace('● 모든 게시물은 사진 + 글 첨부 필수 & 질문 게시글 삭제시 활동정지','').replace('● 모든 게시물은 사진 + 글 첨부 필수 https://cafe.naver.com/casuallydressed/44062 매뉴얼 확인 부탁드립니다.','').replace('\n','')

        d.append( content )

        driver.back()
        
                    
        #data에 집어넣기
        print( date, " //// ", sub, " //// ", content )
        data.append( d )
        
        
        n += 1


# import csv
# fields = ['Subject', 'Content','Date']
# with open('test.csv', 'w',newline='') as f: 
#     write = csv.writer(f) 
#     write.writerow(fields) 
#     write.writerows(data)

#텍스트파일로 저장
c = os.path.exists( 'test.txt' )
print( c )


with open( 'test.txt', 'w', encoding='utf-8' ) as f:
    for line in data:
        for l in line:
            f.write( l )
        f.write( '\n' )

    
    
    
    
    