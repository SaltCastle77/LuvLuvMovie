<template>
  <div>
    <input type="text" placeholder="댓글을 입력하세요" class="input-style" v-model="comment" @keypress.enter="createComment">
    <b-button pill @click="createComment">입력</b-button>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name : 'CommentCreate',
  data () {
    return {
      comment : '',
      articleid : '',
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
    createComment () {
      const data = {
        'content': this.comment
      }
      const config = this.setToken()

      axios.post(LUVLUV_API_URL + `articles/${this.articleid}/comments/`, data , config)
      .then((res) => {
        const comment = res.data 
        // console.log(comment)
        this.$store.dispatch('addComment', comment)
        this.comment = ""
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created () {
    this.articleid = this.$store.state.articleDetail.id
    this.comment = this.$store.state.articleDetail.comment
  }
}
</script>

<style>
.input-style {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px 20px;
  border: 0px;
  border-radius: 24px;
  margin-right: 10px;
  width: 80%;
}
</style>