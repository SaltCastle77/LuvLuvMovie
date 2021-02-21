

# 👭LuvLuvMovie👬

> 내가 좋아하는 장르를 기반으로 영화를 추천해주는 커 [fianl-pjt-readme.md](fianl-pjt-readme.md) 뮤니티 애플리케이션

📒 협업 규칙
커밋시 팀원에게 알릴 것
삽질은 나만!, 삽질 또는 공부중 발견한 Insight, Reference는 트렐로를 통해 공유

## i. 팀원 정보 및 업무 분담 내역

- 길아현
  - gitlab 주소 :
  - 영화 서버(django) 및 프론트(vue) 개발
  - API 크롤링
- 염성훈
  - gitlab 주소 :
  - 게시판 서버(django) 및 프론트(vue) 개발

## ii.목표 서비스 구현 및 실제 구현정도

- 목표 서비스
  - 사용자가 영화 상세 페이지에 평점을 남기면 평점을 남긴 영화의 장르를 DB에 저장해서 사용자가 입력한 장르의 영화를 추천한다.
  - TMDB API를 활용하여 최근 상영중인 영화와 인기영화 추천
  - 영화 상세페이지에서 YOUTUBE API를 활용하여 예고편과 해당 영화의 OST를 표기
  - 영화 뿐만 아니라 자유롭게 사용할 수 있는 게시판 CRUD 및 댓글 CRUD 구현
  - 사용자가 좋아요한 영화를 마이페이지 목록에서 구현

## iii 데이터베이스 모델링(ERD)

## iiii 필수 기능에 대한 설명 

1) 영화 상세 정보에 평점을 기록하면 평점을 남긴 장르를 모아서 사용자에게 해당 장르의 영화를 추천해준다.

2) TMDB API를 활용하여 전문가 평점을 기반으로 인기영황와 현재 상영영화 추천 

- movies/view.py

```python
@api_view(['GET'])
def movie_category(request, where):
    movies = Movie.objects.all().filter(where=where).order_by('-vote_average')[:10]
    serializer = MovieBackdropSerializer(movies, many=True)
    # print(serializer.data)
    return Response(serializer.data)
```

where에는 인기영화 카테고리가 들어가고 `vote_average`를 기준으로 상위 10개의 영화 정보를 가져와서 사용자에게 출력해준다.

- 실행화면

3) 영화 상세페이지에서 YOUTBUE API를 활용하여 예고편과 OST표기 (유투브 영상으로)

- MovieTrailer.vue

```vue
export default {  
    name : "MovieMusic",
    data() {
        return {
            inputText : '',
            videoId : ''
        }
    }, 
    methods : {
        getMovieOST: function () {
    
            const params = {
            key: YOUTUBE_API_KEY,
            part: 'snippet',
            type: 'video',
            q: this.inputText,
            }
            axios.get(YOUTUBE_API_URL, {
                params,
            })
            .then((res) => {
            this.videoId = res.data.items[0].id.videoId
            })
            .catch((err) => {
                console.log(err)
            })
        },
    },
```

YOUTUBE API를 활용하여 정보를 받아왔으며 서버에 형식대로 맞춰서 보내주기 위해 params를 활용해서 서버에 요청을 보내 비디오 정보를 받아와 inputText에 영화명 + OST, 예고편으로 검색해 해당 비디오를 영화 상세페이지에 띄워 줬다.

- 실행화면

4)게시판 CRUD구현

-  articles/models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
```

게시판과 댓글은 유저와 1:N관계로 설정했고 게시판 진입은 로그인을 하지않을 시 접근하지 못하게 했습니다. 댓글또한 마찬가지로 유저에따라 수정 삭제가 가능하도록 하였습니다.