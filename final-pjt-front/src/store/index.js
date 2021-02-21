import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articleDetail: {},
    comments: [],
  },
  mutations: {
    ARTICLE_DETAIL: function(state, articleDetailItem){
      this.state.articleDetail = articleDetailItem
    },
    UPDATE_COMMENTS: function(state, comments){
      this.state.comments = comments
    },
    ADD_COMMENT: function(state, comment){
      this.state.comments.push(comment)
    },
    MOVIE_DETAIL: function(state, movieItem){
      this.state.movieDetail = movieItem
    },
  },
  actions: {
    articleDetail: function ({ commit }, articleDetailItem) {
      commit('ARTICLE_DETAIL', articleDetailItem)
    },
    updateComments: function ({ commit }, comments) {
      commit('UPDATE_COMMENTS', comments)
    },
    addComment: function ({ commit }, comment) {
      commit('ADD_COMMENT', comment)
    },
    movieDetail: function({ commit }, movie) {
      commit('MOVIE_DETAIL', movie)
    },
  },
  plugins :[
    createPersistedState()
  ]
})

