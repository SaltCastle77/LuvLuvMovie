# LuvLuvMovie API Document

## 회원가입 API
> 서버 자체 회원가입한다.

Request HTTP Example:
```bash
POST http://127.0.0.1:8000/accounts/signup/

{
  "username" : "ahyeon",
  "password" : "password",
  "passwordConfirmation" : "password"
}
```
  
Response HTTP Example:
```bash
HTTP_201_CREATED
{
    "username": "ahyeon"
}
```
  
```bash
HTTP_400_BAD_REQUEST
{
  'error': '비밀번호가 다릅니다'
}
```

  
## 로그인 API
> 로그인 토큰 발급  

Request HTTP Example:
```bash
POST http://127.0.0.1:8000/accounts/api-token-auth/
{
  "username" : "ahyeon",
  "password" : "password"
}
```
  
Response HTTP Example:
```bash
HTTP_200_OK
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImFoeWVvbjUiLCJleHAiOjE2MDU3NjIxMzksImVtYWlsIjoiIn0.QIODsLKYI5A4ev_Vgpwj5Dt0BphmtrBpM135HZ4t5Mg"
}
```

## 장르 리스트 API
> 장르 리스트  

Request HTTP Example:
```bash
GET http://127.0.0.1:8000/movies/genres/
```
Response HTTP Example:
```bash
HTTP_200_OK
[
    {
        "id": 12,
        "name": "모험"
    },
    {
        "id": 14,
        "name": "판타지"
    },
    ...
]
```

## 영화 리스트 API
> 영화 썸네일 리스트 API

Request HTTP Example:
```bash
GET http://127.0.0.1:8000/movies/movielist/
```


## 영화 API
> 영화 디테일 API

Request HTTP Example:
```bash
GET http://127.0.0.1:8000/movies/<movie_pk>/
```


## 영화 좋아요 API
```bash
POST http://127.0.0.1:8000/movies/like/11/

HEADERS
  Authorization: 'JWT <token>'
```

### 영화 Review API
```bash
http://127.0.0.1:8000/movies/12/reviews/
- Authorization
{
  content: "",
  score: 1
}
```