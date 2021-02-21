<template>
  <div class="container">
    <h2>글 수정 </h2>
    <div>
     <b-form>
        <b-form-group
          id="input-group-1"
          label="제목 : "
          label-for="input-1"
        >
          <input
            id="input-1"
            v-model.trim="title"
            type="text"
            required
            class="article-input"
          >
        </b-form-group>
       
        <b-form-group id="input-group-2" label="내용 : " label-for="input-2">
          <textarea
            id="input-2"
            v-model.trim="content"
            required
            rows="20"
            class="article-input"
          ></textarea>
        </b-form-group>
      <b-button @click="updateDetail" pill variant="danger">수정</b-button>
    </b-form> 
    </div>
</div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
    name : "ArticleUpdate",
    data () {
        return {
            id : '',
            title: '',
            content: '',
            created_at : '',
            updated_at : '',
            comment_count : '',
            comment_set : []
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
      updateDetail () {
          const detailItem = {
              id: this.id,
              title: this.title,
              content: this.content,
              created_at: this.created_at ,
              updated_at: this.updated_at,
              comment_count: this.comment_count,
              comment_set: this.comment_set,
          }
          const config = this.setToken()
          axios.put(LUVLUV_API_URL + `articles/${this.id}/`,detailItem,config)
            .then((res)=> {
              this.$store.state.articleDetail = res.data
              this.$router.push({name : 'ArticleDetail'})
            })
            .catch(()=>{
                alert('권한이 없습니다.')
                this.$router.push({name: 'ArticleDetail'})
            })
        }
    },
    created() {
        this.id = this.$store.state.articleDetail.id
        this.title = this.$store.state.articleDetail.title
        this.content = this.$store.state.articleDetail.content
        this.created_at = this.$store.state.articleDetail.created_at
        this.updated_at = this.$store.state.articleDetail.updated_at
        this.comment_count = this.$store.state.articleDetail.comment_count
        this.comment_set = this.$store.state.articleDetail.comment_set
    }
}
</script>

<style>

</style>