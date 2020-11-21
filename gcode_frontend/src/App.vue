<template>
<v-app>
  <v-navigation-drawer app>
    <div class="menu-link">
      <v-btn to="/">Login</v-btn>
    </div>
    <div class="menu-link">
      <v-btn to="/profile">Create Profile</v-btn>
    </div>
    <div class="menu-link">
      <v-btn to="/users-list">List of Users</v-btn>
    </div>
    <div class="menu-link">
      <v-btn @click="logout">Logout</v-btn>
    </div>
  </v-navigation-drawer>

  <v-app-bar app>
     <div class="info">
       <p v-if="$store.state.savedCurrentUser.user">Hello, {{ $store.state.savedCurrentUser.user.first_name }} {{$store.state.savedCurrentUser.user.last_name}}</p>
       <p v-else> Hello, Anonymus User</p>
     </div>
  </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-main>

    <!-- Provides the application the proper gutter -->
    <v-container fluid>

      <!-- If using vue-router -->
      <router-view></router-view>
    </v-container>
  </v-main>

  <v-footer app>
    <!-- -->
  </v-footer>
</v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  components: {
    // HelloWorld
  },

  data: () => ({
    //
  }),

    methods: {

        logout: function () {
          axios({
            method: 'get',
            headers: {
              Authorization: 'Token' + ' ' + this.$store.state.savedCurrentUser.token
            },
            url: 'http://127.0.0.1:8000/api/v1/logout'
            }).then(response => {
                if (response.status === 200) {
                  console.log(response.data)
                  // remove user info from store
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
}
</script>

<style>
.menu-link {
  padding: 10px 0px 0px 10px;
}
</style>
