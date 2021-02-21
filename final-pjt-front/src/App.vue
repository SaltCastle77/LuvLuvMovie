<template>
  <div id="app">
    <div id="nav">
        <b-navbar class="header nav-style" fixed="top" toggleable="lg">
          <b-navbar-brand href="#">
            <router-link :to="{ name : 'Home'}">

            <img src="@/assets/logo_transparent.png" width="50" height="50" alt="">
            Home
            </router-link>
          </b-navbar-brand>
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item class="nav_text" @click="authMovie">영화</b-nav-item>
              <b-nav-item class="nav_text" @click="authArticle"> 커뮤니티 </b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
              <b-nav-item-dropdown right>
                <template #button-content>
                  <em>User</em>
                </template>
                <span v-if="login">
                  <b-dropdown-item variant="dark" @click="logout">Logout</b-dropdown-item>
                  <b-dropdown-item variant="dark" :to="{ name : 'Mypage'}">mypage</b-dropdown-item>
                </span>
                <span v-else>
                <b-dropdown-item variant="dark" :to="{ name : 'Signup'}">Signup</b-dropdown-item>
                <b-dropdown-item variant="dark" :to="{ name : 'Login'}">Login</b-dropdown-item>
                </span>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
    </div>
    <router-view @login="login = true"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      login: false,
      movies: []
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: 'Login' })
    },
    search(input) {
      const url = 'https://api.themoviedb.org/3/search/movie'
      const params = {
        api_key: '0bd0f25bbc346f3c9ea7effba6fb6710',
        language: 'ko',
        query: input, 
      }
      if (input.length < 3) {
        return []
      }
      console.log(input)
      axios.get(url, { params })
        .then(res => {
          return res.data
        })
        .then(data => {
          console(data)
          return data.query.search
        })
        .catch(error => {
          console.log(error)
        })
    },
    authArticle() {
      if (localStorage.getItem('jwt')) {
        this.$router.push({ name: 'ArticleList'})
      } else {
        alert('커뮤니티에 들어가려면 로그인하십시오.')
        this.$router.push({name:'Login'})
      }
    },
    authMovie() {
      if (localStorage.getItem('jwt')) {
        this.$router.push({ name: 'MovieHome'})
      } else {
        alert('영화홈으로 들어가려면 로그인하십시오.')
        this.$router.push({name:'Login'})
      }
    }
  },

  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }
  }
}
</script>

<style>
#app {
  /* -webkit-font-smoothing: antialiased; */
  /* -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
  overflow: auto;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  font-weight: bold;
  color: rgb(74, 255, 207);
}
.navbar {
  background: rgb(34, 34, 34, 0.5);
}

.nav_text:hover {
 text-decoration: underline;
}
</style>
