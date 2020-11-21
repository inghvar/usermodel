<template>
<v-layout justify-center>
  <v-form
    ref="form"
    lazy-validation
  >
  <v-row>
    <h1><p>Login</p></h1>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="email"
          :error-messages="emailErrors"
          label="Email"
          required
          @input="$v.email.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="password"
          :error-messages="passwordErrors"
          label="Password"
          type="password"
          required
          @input="$v.password.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

    <v-btn
      color="success"
      class="mr-4"
      @click="submit"
    >
      Login
    </v-btn>
    <p v-if="submitStatus === 'OK'"> You are logged in! </p>
    <p v-if="submitStatus === 'ERROR'"> Please fill the form correctly. </p>
    <p v-if="submitStatus === 'PENDING'"> Sending... </p>
  </v-form>
</v-layout>
</template>

<script>
import axios from 'axios'
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'

export default {
    mixins: [validationMixin],

    validations: {
      email: { required, email },
      password: { required, maxLength }
    },

    data: function () {
      return {
        email: '',
        password: '',
        submitStatus: null
      }
    },

    computed: {
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.required && errors.push('Email is required.')
        !this.$v.email.email && errors.push('Must be valid e-mail')
        return errors
      },
      passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Password is required')
        return errors
      }
    },

    methods: {
        submit () {
          console.log('submit!')
          this.$v.$touch()
          if (this.$v.$invalid) {
            this.submitStatus = 'ERROR'
          } else {
            console.log('send...')
            this.Login()
            this.submitStatus = 'PENDING'
            setTimeout(() => {
              this.submitStatus = 'OK'
            }, 100)
          }
        },

        Login: function () {
          const formData = new FormData()
          if (this.email !== '') {
              formData.append('email', this.email)
          }
          if (this.password !== '') {
              formData.append('password', this.password)
          }

          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/login',
            data: formData,
            headers: { 'Content-Type': 'multipart/form-data' }
            }).then(response => {
                    if (response.status === 200) {
                      console.log(response.data)
                      this.get_user = response.data
                      // save user info in store
                      this.$store.commit('savedCurrentUser', this.get_user)
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
