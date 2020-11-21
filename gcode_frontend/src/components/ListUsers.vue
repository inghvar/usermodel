<template>
  <v-simple-table v-if="users && users.length">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Email
          </th>
          <th class="text-left">
            First Name
          </th>
          <th class="text-left">
            Last Name
          </th>
          <th class="text-left">
            Phone
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="user in users"
          v-bind:key="user.id"
        >
          <td>{{ user.email }}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{ user.phone }}</td>
        </tr>
      </tbody>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title v-if="previous != null"><a v-on:click="goPagePrevious">Previous</a></v-list-item-title>
        <v-list-item-subtitle v-if="next != null"><a v-on:click="goPageNext">Next</a></v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    </template>
  </v-simple-table>
  <div v-else>Login to view the list of users</div>
</template>

<script>

import axios from 'axios'

export default {
    data () {
        return {
            users: [],
            // pagination
            previous: '',
            next: ''
        }
    },
    created () {
        this.getUsers()
    },
    methods: {
        getUsers: function () {
            axios({
              method: 'get',
              headers: {
                  Authorization: 'Token' + ' ' + this.$store.state.savedCurrentUser.token
              },
              url: 'http://127.0.0.1:8000/api/v1/users_list'
                }).then(response => {
                    // console.log(response.data)
                    this.users = response.data.results
                    this.previous = response.data.previous
                    this.next = response.data.next
                })
        },
        goPageNext: function () {
            axios({
              method: 'get',
              headers: {
                  Authorization: 'Token' + ' ' + this.$store.state.savedCurrentUser.token
              },
              url: this.next
                }).then(response => {
                    // console.log(response.data)
                    this.users = response.data.results
                    this.previous = response.data.previous
                    this.next = response.data.next
                })
        },
        goPagePrevious: function () {
            axios({
            method: 'get',
            headers: {
                Authorization: 'Token' + ' ' + this.$store.state.savedCurrentUser.token
            },
            url: this.previous
              }).then(response => {
                  // console.log(this.previous)
                  this.users = response.data.results
                  this.previous = response.data.previous
                  this.next = response.data.next
              })
        }
    }
}
</script>
