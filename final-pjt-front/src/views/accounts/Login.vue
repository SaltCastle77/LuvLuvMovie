<template>
  <div class="loginBox">
    <h1>로그인</h1>
    <div>
      <input
        type="text"
        id="username"
        v-model="credentials.username"
        placeholder="아이디"
        class="login-input"
      >
    </div>
    <div>
      <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        @keypress.enter="login"
        placeholder="비밀번호"
        class="login-input"
      >
    </div>
    <b-button pill variant="danger" @click="login">로그인</b-button>
  </div>
</template>

<script>
import axios from 'axios'
const LUVLUV_API_URL = process.env.VUE_APP_API_URL
export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        curUser:''
      }
    }
  },
  methods: {
    login: function () {
      axios.post(LUVLUV_API_URL + `accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch(() => {
          alert('잘못입력하셨습니다.')
        })
    }
  }
}
</script>
<style>
.loginBox {
  background-color: black;
  background-color: #0a0a0a4d;
  width: 30%;
  margin: 100px auto;
  padding: 100px 0px;

}

.login-input{
  width: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  border: 0px;
  border-radius: 24px;
  padding: 5px 20px;
  margin : 5px auto;
}
</style>
