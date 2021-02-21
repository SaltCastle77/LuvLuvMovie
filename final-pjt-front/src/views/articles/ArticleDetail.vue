<template>
    <div class="container">
        <h1>{{articleDetail.title}}</h1>
        <p class="time">작성시간 : {{articleDetail.created_at | moment('YYYY-MM-DD HH:mm:ss')}}</p>
        <p class="time"> | </p>
        <p class="time">수정시간 : {{articleDetail.updated_at | moment('YYYY-MM-DD HH:mm:ss')}}</p>
        <div class="content">
            {{articleDetail.content}}
        </div>
        <b-button class="btnStyle" pill variant="outline-success" @click="updateArticle(articleDetail)">업데이트</b-button>
        <b-button class="btnStyle" pill variant="outline-success" @click="deleteArticle">삭제</b-button>
        <hr class="hr-style">
        <CommentCreate/>
        <CommentList/>
    </div>
</template>

<script>
import axios from 'axios'
import CommentCreate from '@/components/articles/CommentCreate'
import CommentList from '@/components/articles/CommentList'

const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
    name : 'ArticleDetail',
    data () {
        return {
            articleDetail : {}
        }
    },
    components : {
        CommentCreate,
        CommentList,
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
        deleteArticle () {
        const config = this.setToken()
        axios.delete(LUVLUV_API_URL + `articles/${this.articleDetail.id}`,config)
            .then((res) => {
            console.log(res)
            this.$router.push({name:'ArticleList'})
            })
            .catch(()=>{
                alert('삭제 권한이 없습니다.')
            })
        },
        updateArticle (articleDetail) {
            const config = this.setToken()
            axios.get(LUVLUV_API_URL + `articles/${articleDetail.id}`,config)
                .then((res) => {
                this.articleDetail = res.data
                this.$store.dispatch('articleDetail',res.data)
                this.$router.push({name : 'ArticleUpdate'})
            })
        }
    },
    created () {
        this.articleDetail = this.$store.state.articleDetail
        // console.log(this.articleDetail)
    },
}
</script>

<style>
.container {
    padding-top: 80px;
    text-align: left;
}
.time {
    color: darkgray;
    display: inline;
    margin-right: 10px;
}
.content {
    margin: 30px 0px;
    font-size: 1.4rem;
}
.hr-style {
    background-color: gray;
}
</style>