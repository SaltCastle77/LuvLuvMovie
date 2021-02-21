<template>
  <div class="movie-home">
    <div class="my-favorite">
      <div class="f">
        <p class="f2" data-sal="slide-up" >2020 SSAFY FINAL PROJECT</p>
        <h1 class="f1">Luv Luv Movie</h1>
        <p class="f3">LET'S STREAM</p>
      </div>
    </div>
    <div class="container">
      <b-button
        class="btnStyle"
        pill variant="outline-success"
        v-for="(movieGenre,idx) in movieGenres"
        :key="idx"
        @click="getMovieThumbnail(movieGenre.id, movieGenre.name)"
      >
        {{movieGenre.name}}
      </b-button>
    </div>
    <h2>{{genreName}} TOP 10</h2>
    <carousel-3d
      ref="treeExplorer"
      :display="7"
      :height="550"
      :border="0"
      :autoplay=true
      :autoplayTimeout="1000"
      :controlsVisible=true
      :count="movies.length"
    >
      <slide
        v-for="(movie, i) in movies"
        :index="i"
        :key="movie.id"
        :style="{
          borderRadius: '24px',
          'box-shadow': '0px 20px 30px black',
          backgroundImage: `url(${movie.poster_path})`
        }"
      >
      <h1 class="scoreStyle">{{ i+1 }}</h1>
      <button @click="clickMovieCard(movie.id)" class="block"></button>
      </slide>
    </carousel-3d>
    <b-container>
      <h2>{{username}}님, 이런 영화 어때요?</h2>
      <b-row>
        <b-col cols="2" v-for="(recommendMovie,idx) in recommendMovies" :key="idx">
          <div class="hovereffect">
            <img class="image img-responsive" @click="clickMovieCard(recommendMovie.id)" :src="recommendMovie.poster_path" alt="" width="160" height="240">
            <div class="overlay">
                <h2> {{ recommendMovie.title }} </h2>
                <button @click="clickMovieCard(recommendMovie.id)" class="block"></button>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <h2>최근 뜨는 영화</h2>
      <b-row>
        <b-col cols="2" v-for="(popularMovie,idx) in popularMovies" :key="idx">
          <div class="hovereffect">
            <img class="image img-responsive" @click="clickMovieCard(popularMovie.id)" :src="popularMovie.poster_path" alt="" width="160" height="240">
            <div class="overlay">
              <h2> {{ popularMovie.title }} </h2>
              <button @click="clickMovieCard(popularMovie.id)" class="block"></button>
              </div>
            </div>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <h2>상영 중인 영화</h2>
      <b-row>
        <b-col cols="2" v-for="(movie,idx) in playingMovies" :key="idx">
          <div class="hovereffect">
            <img class="image img-responsive" @click="clickMovieCard(movie.id)" :src="movie.poster_path" alt="" width="160" height="240">
            <div class="overlay">
              <h2> {{ movie.title }} </h2>
              <button @click="clickMovieCard(movie.id)" class="block"></button>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'

const LUVLUV_API_URL = process.env.VUE_APP_API_URL
export default {
  name: "MovieHome",
  data() {
    return {
      movies: [],
      movieGenres : [],
      genreTitle: '',
      popularMovies : [],
      playingMovies: [],
      recommendMovies: [],
      username: "",
    }
  },
  components: {
    Carousel3d,
    Slide,
  },
  computed: {
    genreName() {
      return this.genreTitle
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
    getUsername() {
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + 'accounts/username/', config)
        .then(res => {
          this.username = res.data
        })
    },
    getMovieThumbnail: function (genreId, genreTitle) {
      axios.get(LUVLUV_API_URL+`movies/genres/movielist/${genreId}/`)
        .then((res) => {
          this.movies = res.data
          // console.log(res.data)
          this.genreTitle = genreTitle
        })
    },
    getMovieGenres() {
      axios.get(LUVLUV_API_URL+'movies/genres/')
        .then((res) =>{
          this.movieGenres = res.data
        })
    },
    clickMovieCard(id) {
      axios.get(LUVLUV_API_URL+`movies/${id}/`)
        .then((res) => {
          this.$store.dispatch('movieDetail', res.data)
          this.$router.push({name : 'MovieDetailHome'})
      })
    },
    getMoviePopluar(){
      axios.get(LUVLUV_API_URL+`movies/category/popular/`)
      .then((res)=> {
        this.popularMovies = res.data
      })
    },
    getMoviePlaying(){
      axios.get(LUVLUV_API_URL+`movies/category/now_playing/`)
      .then((res)=> {
        this.playingMovies = res.data
      })
    },
    getMovieRecommend(){
      const config = this.setToken()
      axios.get(LUVLUV_API_URL+'movies/recommend/', config)
        .then(res => {
          this.recommendMovies = res.data
        })
    },
  },
  created () {
    // console.log('생겼다')
    this.getUsername()
    this.getMovieThumbnail(10770, '장르별')
    // console.log(this.movies)
    this.getMovieGenres()
    this.getMoviePopluar()
    this.getMoviePlaying()
    this.getMovieRecommend()
  },
  updated() {
    this.$refs.treeExplorer.goSlide(this.$refs.treeExplorer.currentIndex)
  }
}
</script>

<style>
.movie-home {
  overflow: auto;
  
}
.my-favorite {
  background: rgb(34, 34, 34);
  height: 100vh;
  text-align: center;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  position: relative;
}
.f{
  position: absolute;
  top: 40%;
  margin-top: -50px;
  width: 100%;
  height: 100px;
  font-family: sans-serif;
}
.f1{
  font-weight: 800;
  font-size: 4.4rem;
  color: rgb(74, 255, 207);
}
.f2{
  font-weight: 300;
  font-size: 1.88rem;
}
.f3 {
  font-size: 1.375rem;
  font-weight: normal;
  font-style: oblique;
  letter-spacing: 3px;
  margin-bottom: 2rem;
}
.block {
  /* display: block; */
  width: 100%;
  height: 100%;
  border: none;
  opacity: 0;
}
.container {
  margin-top: 60px;
  margin-bottom: 70px;
}
.btnStyle {
  color: rgb(74, 255, 207);
  border-color: rgb(74, 255, 207);
  width: 100px;
  margin: 5px;
  padding: 10px;
}
.scoreStyle {
  color: white;
  margin-top: 10px;
  margin-left: 10px;
  font-weight: 900;
}

.image {
  border-radius: 10%;
}

</style>