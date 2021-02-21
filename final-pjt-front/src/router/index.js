import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movies/Home.vue'
// accounts
import Mypage from '../views/accounts/Mypage.vue'
import Signup from '../views/accounts/Signup.vue'
import Login from '../views/accounts/Login.vue'
// articles
import ArticleList from '../views/articles/ArticleList.vue'
import ArticleCreate from '../views/articles/ArticleCreate.vue'
import ArticleDetail from '../views/articles/ArticleDetail.vue'
import ArticleUpdate from '../views/articles/ArticleUpdate.vue'
// import MovieHome from '@/views/movies/MovieHome'
const MovieHome = () => import('@/views/movies/MovieHome')
// import MovieDetail from '../components/movies/MovieDetail.vue'
import MovieDetailHome from '../views/movies/MovieDetailHome.vue'
import MovieMusic from '../components/movies/MovieMusic.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/mypage',
    name: 'Mypage',
    component: Mypage
  },
  {
    path: '/movies/moviehome',
    name: 'MovieHome',
    component: MovieHome
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/movies/article',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/components/articlecreate',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path : '/articles/articledetail',
    name : 'ArticleDetail',
    component : ArticleDetail
  },
  {
    path: '/articles/articleupdate',
    name: 'ArticleUpdate',
    component : ArticleUpdate
  },
  {
    path: '/movies/moviedetailhome',
    name: 'MovieDetailHome',
    component: MovieDetailHome
  },
  // {
  //   path: '/components/moviedetail',
  //   name: 'MovieDetail',
  //   component: MovieDetail
  // },
  {
    path: '/components/moviemusic',
    name : 'MovieMusic',
    component : MovieMusic
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
