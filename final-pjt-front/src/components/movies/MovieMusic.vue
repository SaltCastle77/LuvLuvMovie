<template>
    <div>
        <h2>OST 들어보기</h2>
        <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
</template>

<script>
import axios from 'axios'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const YOUTUBE_API_KEY = 'AIzaSyBZcKjAvGHX7A0YycE2Kw8ZhHlnESF21zo'
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
export default {  
    name : "MovieMusic",
    data() {
        return {
            inputText : '',
            videoId : ''
        }
    }, 
    methods : {
        getMovieOST: function () {
    
            const params = {
            key: YOUTUBE_API_KEY,
            part: 'snippet',
            type: 'video',
            q: this.inputText,
            }
            axios.get(YOUTUBE_API_URL, {
                params,
            })
            .then((res) => {
            this.videoId = res.data.items[0].id.videoId
            })
            .catch((err) => {
                console.log(err)
            })
        },
    },
    computed: {
        videoURI: function () {
            const videoId = this.videoId
            return `https://www.youtube.com/embed/${videoId}`
            }
    },
    created() {
        this.inputText = this.$store.state.movieDetail.title + 'OST'
        // console.log(this.inputText)
        this.getMovieOST()
    }
}
</script>

<style>

</style>