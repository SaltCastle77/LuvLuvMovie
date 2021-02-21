<template>
  <div class="container">
    <div class="video-container">
      <MovieTrailer />
      <div>
        <span id="font"> {{ moviedata.title }}</span>
        <span>  개봉일 : {{ moviedata.release_date }}</span>
        <span style="float:right;">
          <button class="btn btn-link" :style="btnStyle" @click="clickHeart">
            <i class="fas fa-heart"></i>
          </button>
        </span>
      </div>
      <hr class="hr-style">
      <p>{{ moviedata.overview }}</p>
      <div>
        <span v-for="(genre,idx) in moviedata.genres" :key="idx">#{{ genre.name }} </span>
      </div>
    </div>
    <MovieMusic />
    <div class="container">
      <p>평점</p>
      <b-form-rating id="star" v-model="score" variant="warning" no-border inline size="lg"></b-form-rating>
      <input v-model="content" @keypress.enter="createReview" type="text" class="rating-input" placeholder="한줄평을 입력하세요">
      <b-button @click="createReview">등록</b-button>
    
      <div class="comment-style">
        <li v-for="(review,idx) in reviews" :key="idx">
          <span>{{review.user}} | {{ review.content}} </span>
          <b-form-rating id="star" v-model="review.score" show-value color="lightgray" no-border readonly inline size="sm"></b-form-rating>
        </li>
      </div>
    </div>
    <hr class="hr-style">
  </div>
</template>

<script>
import axios from 'axios'
import MovieTrailer from '@/components/movies/MovieTrailer'
import MovieMusic from '@/components/movies/MovieMusic'

const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name : 'MovieDetailHome',
  components : {
    // MovieDetail,
    MovieTrailer,
    MovieMusic,
  },
  data() {
    return {
      moviedata: {},
      movieDetailInfo : {},
      heart: null,
      content: "",
      score: 0,
      reviews: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
          }
      }
      return config
    },
    getMovieDetail() {
      axios.get(LUVLUV_API_URL + `movies/${this.movieDetailInfo.id}/`)
        .then((res) => {
          // console.log(res.data)
          this.moviedata = res.data
          this.reviews = res.data.review_set
        })
    },
    clickHeart() {
      const config = this.setToken()
      // console.log(config)
      // console.log(this.movieDetailInfo.id)
      axios.post(LUVLUV_API_URL + `movies/${this.movieDetailInfo.id}/like/`, {}, config)
        .then((res) => {
          // console.log(res.data)
          this.heart = res.data.like
        })
    },
    isLiked() {
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + `movies/${this.movieDetailInfo.id}/like/`, config)
        .then((res) => {
          // console.log(res.data)
          this.heart = res.data
        })
    },
    createReview() {
      const config = this.setToken()
      const reviewItem = {
        score : this.score,
        content : this.content
      }
      axios.post(LUVLUV_API_URL + `movies/${this.movieDetailInfo.id}/reviews/`, reviewItem, config)
        .then((res) => {
          this.reviews.push(res.data)
          this.score = 0
          this.content = ""
        })
        .catch(error => {
          console.log(error)
        })
    },

  },
  computed: {
    btnStyle() {
      if (this.heart) {
        return {'color': 'crimson'}
      } else {
        return {'color': 'gray'}
      }
    }
  },
  created() {
    this.movieDetailInfo = this.$store.state.movieDetail
    this.getMovieDetail()
    this.isLiked()
  },
}
</script>

<style>
#star {
  background-color: rgba(0, 0, 0, 0);
}
.video-container {
  width: 100%;
  margin: 30px auto;
  border-radius: 30px;
  background-color:rgb(50, 50, 50, 0.3);
  padding: 40px;
  box-sizing: border-box;
  /* box-shadow: 0px 8px 33px #202120; */
}
#font {
  font-size: x-large;
}
#heart {
  font-size : 25px;
}
.rating-input {
  width: 70%;
  background-color: rgba(255, 255, 255, 0.2);
  border: 0px;
  border-radius: 24px;
  padding: 5px 20px;
  margin-right: 30px;
}
</style>