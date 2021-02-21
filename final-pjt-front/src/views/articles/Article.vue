<template>
  <div>
    <ul>
      <li v-for="(article,idx) in articles" :key="idx">
        <p>{{ article.title }}</p>
        <p>{{ article.content }} </p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL
export default {
  name: 'Article',
  data () {
    return {
      articles: []
    }
  },
  methods: {
    getArticle () {
      axios.get(LUVLUV_API_URL + 'articles/')
        .then((res) => {
          console.log(res.data)
          this.articles = res.data
        })
    }
  },
  created() {
    this.getArticle()
  }
}
</script>

<style>

</style>