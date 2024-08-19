import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Personal from '../views/Personal.vue'
import ChangePassword from '../views/ChangePassword.vue'
import store from '../store'
import ActivateEmail from '../views/ActivateEmail.vue'
import Collect from '../views/Collect.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: "/movie/:id",
    name: "MovieDetail",
    component: MovieDetail
  },
  {
    path: "/register",
    name: "SigRegisternUp",
    component: Register
  },
  
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/activate/:uid/:token",
    name: "ActivateEmail",
    component: ActivateEmail
  },

  {
    path: "/personal",
    name: "Personal",
    component: Personal,
    meta: {
      requireLogin: true
    }
  },
  {
    path: "/change_password",
    name: "ChangePassword",
    component: ChangePassword,
    meta: {
      requireLogin: true
    }
  },
  {
    path: "/collect",
    name: "Collect",
    component: Collect,
    meta: {
      requireLogin: true
    }
  },
 

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  // console.log('router beforeahc islogin:' + store.state.isLogin)
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isLogin) {
    next({ name:'Login', query: {to: to.path} });
  } else {
    next()
  }
})

// router.beforeEach(async (to, from) => {
//   await store.dispatch('refreshToken')
// })

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.dispatch('checkLogin')) {
//     next({ name:'Login', query: {to: to.path} });
//   } else {
//     next()
//   }
// })

// router.beforeEach((to, from, next) => {

//   const isLoggedIn = store.dispatch('checkLogin')
//   console.log('beforeEach isLoggedIn:' + isLoggedIn)
//   if (to.matched.some(record => record.meta.requireLogin)) {
//     console.log('执行match requireAuth')
//     if (!isLoggedIn) {
//       next({ name: 'Login' }) 
//     } else {
//       next()
//     }

//   } else {
//     next() 
//   }

// })


export default router
