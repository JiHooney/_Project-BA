import os

#이미 파일이 존재하면 존재하는 파일삭제
c = os.path.exists( 'test.txt' )    
# if c:
#     os.remove( 'test.txt' )
#         #텍스트파일로 저장
#     with open( 'test.txt', 'w', encoding='utf-8' ) as f:
#         for line in data:
#             for l in line:
#                 f.write( l )
#             f.write( '\n' )
# else:
#         #텍스트파일로 저장
#     with open( 'test.txt', 'w', encoding='utf-8' ) as f:
#         for line in data:
#             for l in line:
#                 f.write( l )
#             f.write( '\n' )
