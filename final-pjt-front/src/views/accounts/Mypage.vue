<template>
  <div class="container">
    <h2 class="text-center">안녕하세요. {{ username }}님</h2>
    <div id="title">내가 찜한 영화 </div>
    <div class="d-flex flex-wrap">
      <div v-for="(likemovie,idx) in likeMovies" :key="idx">
        <div class="hovereffect">
          <img class="likeimg img-responsive" @click="clickMovieCard(likemovie.id)" :src="likemovie.poster_path" alt="">
            <div class="overlay">
              <h2> {{ likemovie.title }} </h2>
              <button @click="clickMovieCard(likemovie.id)" class="block"></button>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'Mypage',
  data () {
    return {
      likeMovies : [],
      username: ' '
    }
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getLikeMovie() {
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + `movies/mymovies/`, config)
      .then((res)=>{
        this.likeMovies = res.data
      })
    },
    clickMovieCard(id) {
      axios.get(LUVLUV_API_URL + `movies/${id}/`)
        .then((res) => {
          console.log(res.data)
          this.$store.dispatch('movieDetail', res.data)
          this.$router.push({name : 'MovieDetailHome'})
      })
    },
    getUser(){
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + 'accounts/username/', config)
      .then((res)=> {
        this.username = res.data
      })
    }
  },
  created() {
    this.getLikeMovie()
    this.getUser()
  },
}
</script>

<style>
.likeimg{
  height: 200px;
  width: 180px;
  margin: 5px auto;
  padding: 10px;
  border-radius: 10%;
}
.container{
  text-align: center;
}

#title {
  font-size: 150%;
}

.block {
  /* display: block; */
  width: 100%;
  height: 100%;
  border: none;
  opacity: 0;
}

.hovereffect {
  width: 100%;
  height: 100%;
  float: left;
  overflow: hidden;
  position: relative;
  text-align: center;
  cursor: default;
}

.hovereffect .overlay {
  width: 100%;
  height: 100%;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
}

.hovereffect img {
  display: block;
  position: relative;
  -webkit-transition: all 0.4s ease-in;
  transition: all 0.4s ease-in;
}

.hovereffect:hover img {
  filter: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feColorMatrix type="matrix" color-interpolation-filters="sRGB" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0" /><feGaussianBlur stdDeviation="3" /></filter></svg>#filter');
  filter: grayscale(1) blur(3px);
  -webkit-filter: grayscale(1) blur(3px);
  -webkit-transform: scale(1.2);
  -ms-transform: scale(1.2);
  transform: scale(1.2);
}

.hovereffect h2 {
  text-transform: uppercase;
  text-align: center;
  position: relative;
  font-size: 17px;
  padding: 10px;
  background: rgba(0, 0, 0, 0.6);
}

.hovereffect a.info {
  display: inline-block;
  text-decoration: none;
  padding: 7px 14px;
  border: 1px solid #fff;
  margin: 50px 0 0 0;
  background-color: transparent;
}

.hovereffect a.info:hover {
  box-shadow: 0 0 5px #fff;
}

.hovereffect a.info, .hovereffect h2 {
  -webkit-transform: scale(0.7);
  -ms-transform: scale(0.7);
  transform: scale(0.7);
  -webkit-transition: all 0.4s ease-in;
  transition: all 0.4s ease-in;
  opacity: 0;
  filter: alpha(opacity=0);
  color: #fff;
  text-transform: uppercase;
}

.hovereffect:hover a.info, .hovereffect:hover h2 {
  opacity: 1;
  filter: alpha(opacity=100);
  -webkit-transform: scale(1);
  -ms-transform: scale(1);
  transform: scale(1);
}

</style>