<template>
  <div class="container">
    <h1>새 글 작성</h1>
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
            placeholder="제목을 입력하세요."
            class="article-input"
          >
        </b-form-group>

        <b-form-group id="input-group-2" label="내용 : " label-for="input-2">
          <textarea
            id="input-2"
            v-model.trim="content"
            required
            placeholder="내용을 입력하세요"
            rows="20"
            class="article-input"
          ></textarea>
        </b-form-group>

        <b-button @click="createArticle" pill variant="success">작성</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name : 'ArticleCreate',
  data() {
    return {
      title : '',
      content : '',
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
    createArticle () {
      const articleItem = {
        title : this.title,
        content : this.content
      }
      const config = this.setToken()

      if (articleItem.title === ''){
        alert('제목을 입력하십시오.')
      } else if (articleItem.content === ''){
        alert('내용을 입력하십시오.')
      } else {
        axios.post(LUVLUV_API_URL + 'articles/',articleItem, config)
          .then((res) => {
            console.log(res)
            this.$router.push({name :'ArticleList'})
          })
          .catch((err) => {
            console.log(err)
          })
        }
    }
  },
}
</script>

<style>
label {
  text-align: left;
}

#input-1 {
 color: white
}

#input-2 {
  color: white
}

.article-input {
  width: 100%;
  background-color: rgba(255, 255, 255, 0.2);
  border: 0px;
  border-radius: 24px;
  padding: 5px 20px;
}
</style>