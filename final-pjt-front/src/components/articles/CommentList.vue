<template>
  <div class="comment-style">
      <li v-for="(comment,idx) in comments" :key="idx"> {{comment.user}} | {{ comment.content}}
          <span v-if="comment.user === username">
            <span v-show="!is_show">
              <b-button variant="link" @click="handle_toggle(comment.id)" size="sm">수정</b-button>
            </span>
          </span>
          <span v-if="comment.id === commentId">
            <span v-show="is_show">
              <input type="text" v-model="content" @keypress.enter="updateComment(idx,comment.user)"><b-button variant="link" @click="updateComment(idx,comment.user)">수정</b-button>
            </span>
          </span>
          <span v-if="comment.user === username">
            <b-button variant="link" @click="deleteComment(comment)" size="sm">삭제</b-button>
          </span>
      </li>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name : 'CommentList',
  data() {
    return {
      comments : [],
      articleDetail : {},
      is_show : false,
      commentId : '',
      content : '',
      idx : '',
      username : ''
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
    deleteComment (comment) {
      const config = this.setToken()
      axios.delete(LUVLUV_API_URL + `articles/${this.articleDetail.id}/comments/${comment.id}/`,config)
        .then((res) =>{
          // console.log(res)
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.comment_id
          })
          this.comments.splice(targetCommentIdx, 1)
        })
    },
    updateComment (idx,commentUser) {
      const commentItem = {
        id : this.commentId,
        content : this.content
      }
      const config = this.setToken()
      this.idx = idx
      axios.put(LUVLUV_API_URL + `articles/${this.articleDetail.id}/comments/${this.commentId}/`,commentItem,config)
      .then((res)=> {
        if (commentUser !== res.data.user){
          alert('권한이 없습니다.')
          this.is_show = !this.is_show
        }else {
        this.$store.state.comments[this.idx].id = res.data.id
        this.$store.state.comments[this.idx].content = res.data.content
        this.is_show = !this.is_show
        this.content = ''
        }
      })
    },
    handle_toggle(commentId) {
      this.is_show = !this.is_show
      this.commentId = commentId
     },
    getUser(){
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + 'accounts/username/',config)
      .then((res)=> {
        this.username = res.data
      })
    }
  },
  created() {
    this.comments = this.$store.state.comments
    this.articleDetail = this.$store.state.articleDetail
    this.getUser()
  }
  }
</script>

<style>
.comment-style {
  margin: 30px 0px;
  list-style: none;
  color: lightgray;
}
</style>
