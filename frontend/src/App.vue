<template>
  <router-view/>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')
    // const token = this.$store.state.token
    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "JWT " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
    console.log('axios token is:' + axios.defaults.headers.common['Authorization'])
  },
}
</script>

