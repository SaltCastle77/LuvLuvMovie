<template>
  <div class="loginBox">
    <h1>회원가입</h1>
    <div>
      <span> 아이디: </span>
       <input
        type="text"
        id="username"
        v-model="credentials.username"
        placeholder="아이디"
        class="login-input"
      >
    </div>
    <div>
      <span> 비밀번호: </span>
       <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        placeholder="비밀번호"
        class="login-input"
      >
    </div>
    <div>
      <span for="passwordConfirmation">비밀번호 확인: </span>
      <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
        placeholder="비밀번호"
        class="login-input"
      >
    </div>
    <b-button pill variant="danger" @click="signup">회원가입</b-button>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios.post(LUVLUV_API_URL + `accounts/signup/`, this.credentials)
        .then(() => {
          this.$router.push({ name: 'Login'})
        })
        .catch(() => {
          alert('비밀번호가 다릅니다.')
        })
    }
  }
}
</script>

<style scoped>
</style>