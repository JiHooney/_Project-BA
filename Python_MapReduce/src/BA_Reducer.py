#!/usr/bin/python3.6
# -*-coding:utf-8 -*

import sys

#테스트하기 위해서 2페이지만 긁어온 파일 읽기
# f = open( './test_reduce.txt', 'r')
# lines = f.readlines()

#입력키값 및 출력키값 변수 선언
input_key = None
input_value = 0
output_key = None
output_value = 0

tmp_list = []

n = 0 #행번호 출력을 위한 변수

#매퍼출력키값으로 하나의 리스트를 만듦
# for line in lines:
for line in sys.stdin:
    line = line.strip()     #문장 공백 제거
    tmp_list.append(line)

#while반복문은 tmp_list가 비워지면 반복중지
while len( tmp_list ) != 0: 
    
          #이 반복문은 동일한 키값을 찾아서 개수를 올리기위한 반복문
    for line in tmp_list:    
        cols = line.split( '|' )

        input_key = cols[0]     #내용,형태소
        input_value = int( cols[1] )    #1
    
                     #출력키와 입력키비교, 같으면 출력값 1증가, 그리고 다음 행으로 이동
                     #다르면 출력키 존재여부확인, 존재하면 다음행이동, 존재하지않으면 출력키 입력키로 정의
        if output_key == input_key:
            output_value += input_value
            continue
        else:
            if output_key:
                continue
            output_key = input_key
            output_value = input_value          
    
    remove_str = output_key+'|1'
    #remove_str과 같지 않은 요소들만 배열에 남겨서 출력했던 내용은 배열에서 삭제
    tmp_list = [ i for i in tmp_list if not i == remove_str ]
    
    n += 1
    output_key = str(n)+ ',' + output_key
    print( '%s,%s' %( output_key, output_value ) )  #출력결과: 행번호,내용,형태소,개수
    
          #다시 입출력 키값 초기화
    input_key = None
    input_value = 0
    output_key = None
    output_value = 0
    
    

    
    