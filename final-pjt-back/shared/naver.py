class NAVER_API_Maker:
    url = 'https://openapi.naver.com/v1/search/movie.json'

    '''
    GET /v1/search/movie.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&genre=1 HTTP/1.1
    Host: openapi.naver.com
    User-Agent: curl/7.49.1
    Accept: */*
    X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}
    X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}
    '''
    
    def __init__(self):
        self.client_id = 'kfEXB51LESzK03HgZsoa'
        self.client_secret = ''
        

'''
검색을 원하는 장르 코드
1: 드라마 2: 판타지 3: 서부 4: 공포 5: 로맨스 6: 모험 7: 스릴러
8: 느와르 9: 컬트 10: 다큐멘터리 11: 코미디 12: 가족 13: 미스터리 14: 전쟁
15: 애니메이션 16: 범죄 17: 뮤지컬 18: SF 19: 액션20: 무협 21: 에로
22: 서스펜스 23: 서사 24: 블랙코미디 25: 실험 26: 영화카툰 27: 영화음악 28: 영화패러디포스터
'''