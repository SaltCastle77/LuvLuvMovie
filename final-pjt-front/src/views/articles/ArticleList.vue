<template>
  <div class="container">
    <div class="text-right"><b-button class="btnStyle" pill variant="outline-success" @click="goArticleCreate">글쓰기</b-button></div>
    <ul>
        <b-table
          hover
          :items="articles"
          :fields="fields"
          @row-clicked="pushArticleid"
          :outline="outline"
          :no-border-collapse="noCollapse"
          class="tableStyle"
          >
        </b-table>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const LUVLUV_API_URL = process.env.VUE_APP_API_URL
export default {
  name: 'ArticleList',
  data () {
    return {
      articles: [],
      fields: [
        {
          key:'id',
          label: '번호',
          sortable: true
        },
        {
          key: 'title',
          label: '제목',
          sortable: true
        },
        {
          key: 'user',
          label: '글쓴이'
        },
        {
          key: 'created_at',
          label: '작성시간'
        }
        ],
        dark : true,
        outline : true,
        noCollapse : true,
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
    getArticle () {
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + 'articles/',config)
        .then((res) => {
          this.articles = res.data
        })
    },
    pushArticleid (item) {
      const config = this.setToken()
      axios.get(LUVLUV_API_URL + `articles/${item.id}`,config)
        .then((res) => {
          this.$store.dispatch('articleDetail', res.data)
          this.$store.dispatch('updateComments', res.data.comment_set)
          this.$router.push({name : 'ArticleDetail'})
        })
    },
    goArticleCreate() {
      this.$router.push({name:'ArticleCreate'})
    }
  },
  created() {
    this.getArticle()
  }
}
</script>

<style>
.container {
  margin-top: 70px;
}
.tableStyle {
  color: white !important;
}
.btnStyle {
  margin-bottom: 20px;
}
</style>

