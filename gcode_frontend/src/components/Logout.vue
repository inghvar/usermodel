<script>

import axios from 'axios'

export default {
    created () {
        this.Logout()
    },
    Logout: function () {
      axios({
        method: 'get',
        headers: {
          Authorization: 'Token' + ' ' + this.$store.state.savedCurrentUser.token
        },
        url: 'http://127.0.0.1:8000/api/v1/logout'
        }).then(response => {
            if (response.status === 200) {
               console.log(response.data)
               this.$store.commit('savedCurrentUser', '')
            } else {
              console.log(response.data)
            }
         })
         .catch((error) => {
              console.log(JSON.stringify(error.response.data))
          })
    }
}
</script>
