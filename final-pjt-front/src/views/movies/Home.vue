<template>
  <div>
    <slider animation="fade"
      height="100vh"
      class="popular"
    >
      <slider-item
      class="popular"
      v-for="(img, index) in backgroundImgs"
      :key="index"
      >
      <img :src="img.backdrop_path" class="popular" alt="">
      </slider-item>
    </slider>
  </div>

</template>

<script>
import axios from 'axios'
import { Slider, SliderItem } from 'vue-easy-slider'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'Home',
  data() {
    return {
      backgroundImgs: []
    }
  },
  components: {
    Slider,
    SliderItem
  },
  methods: {
    getBackgroundImg() {
      axios.get(LUVLUV_API_URL + 'movies/category/popular/')
        .then(res => {
          console.log(res.data)
          this.backgroundImgs = res.data
        })
    }
  },
  created() {
    this.getBackgroundImg()
    console.log(this.LUVLUV_API_URL)
  }
}
</script>
<style>
.popular {
  height: 100vh;
  width: 100%;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
}
</style>
