import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false,
    token: '',
    refreshToken: '',
    expiredTime: '',
    username: '',
  },

  getters: {
  },

  mutations: {
    initializeStore(state) {
      // 判断是否过期

      // 判断refresh token 是否过期
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isLogin = true
      } else {
        state.token = ''
        state.isLogin = false
      }
    },

    setToken(state, token, refreshToken, expiredTime) {
        state.token = token
        state.refreshToken = refreshToken
        state.expiredTime = expiredTime
        state.isLogin = true
      },

    setUser(state, username) {
      state.username = username
    },

    removeToken(state) {
        state.token = ''
        state.refreshToken = ''
        state.expiredTime = ''
        state.isLogin = false
      },
    removeUser(state) {
      state.username = ''
    }

  
  },
  
  actions: {
  },
  modules: {
  }
})
