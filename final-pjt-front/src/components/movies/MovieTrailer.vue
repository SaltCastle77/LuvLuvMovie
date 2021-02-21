<template>
  <div>
    <iframe class="video" :src="videoURI" frameborder="0"></iframe>
  </div>
</template>

<script>
import axios from 'axios'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
    name : 'MovieTrailer',
    data() {
        return {
            inputText : '',
            videoId : ''
        }
    },
    methods : {
        onInputChange: function () {
    
            const params = {
                key: YOUTUBE_API_KEY,
                part: 'snippet',
                type: 'video',
                q: this.inputText + '예고편'
            } 
            axios.get(YOUTUBE_API_URL, {
                    params,
            })
                .then((res) => {
                this.videoId = res.data.items[0].id.videoId
                })
                .catch((err) => {
                    // console.log('errororororo')
                    console.log(err)
                })
            },
    },
    computed: {
        videoURI: function () {
        const videoId = this.videoId
        return `https://www.youtube.com/embed/${videoId}/`
        }
    },
    created() {
        this.inputText = this.$store.state.movieDetail.title
        this.onInputChange()
    }
}
</script>

<style>
.video {
  width: 100%;
  height: 50vh;
  margin-bottom: 50px;
}
</style>