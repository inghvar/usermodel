<template>
<v-layout justify-center>
  <v-form
    ref="form"
    lazy-validation
  >
  <v-row>
    <h1><p>Create Profile</p></h1>
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

  <v-row>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="repeatPassword"
          :error-messages="repeatPasswordErrors"
          label="Repeat Password"
          type="password"
          required
          @input="$v.repeatPassword.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="first_name"
          :error-messages="first_nameErrors"
          label="First Name"
          required
          @input="$v.first_name.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="last_name"
          :error-messages="last_nameErrors"
          label="Last Name"
          required
          @input="$v.last_name.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="10" lg="12">
        <v-text-field
          v-model="phone"
          label="Phone"
          @input="$v.phone.$touch()"
        ></v-text-field>
    </v-col>
  </v-row>

    <v-btn
      color="success"
      class="mr-4"
      :disabled="submitStatus === 'PENDING'"
      @click="submit"
    >
      Create
    </v-btn>
    <p v-if="submitStatus === 'OK'"> Thanks for your submission! </p>
    <p v-if="submitStatus === 'ERROR'"> Please fill the form correctly. </p>
    <p v-if="submitStatus === 'PENDING'"> Sending... </p>
  </v-form>
</v-layout>
</template>

<script>
import axios from 'axios'
import { validationMixin } from 'vuelidate'
import { required, minLength, email, sameAs } from 'vuelidate/lib/validators'

export default {
    mixins: [validationMixin],

    validations: {
      email: { required, email },
      password: { required, minLength: minLength(6) },
      repeatPassword: { required, sameAsPassword: sameAs('password') },
      first_name: { required },
      last_name: { required }
    },

    data: function () {
      return {
        email: '',
        password: '',
        repeatPassword: '',
        first_name: '',
        last_name: '',
        phone: '',
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
        !this.$v.password.minLength && errors.push('Password must be at least 6 characters')
        return errors
      },
      repeatPasswordErrors () {
        const errors = []
        if (!this.$v.repeatPassword.$dirty) return errors
        !this.$v.repeatPassword.sameAsPassword && errors.push('Passwords must be identical')
        return errors
      },
      first_nameErrors () {
        const errors = []
        if (!this.$v.first_name.$dirty) return errors
        !this.$v.first_name.required && errors.push('First Name is required')
        return errors
      },
      last_nameErrors () {
        const errors = []
        if (!this.$v.last_name.$dirty) return errors
        !this.$v.last_name.required && errors.push('Last Name is required')
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
            // do your submit logic here
            console.log('send...')
            this.Registration()
            this.submitStatus = 'PENDING'
            setTimeout(() => {
              this.submitStatus = 'OK'
            }, 500)
          }
        },

        Registration: function () {
          const formData = new FormData()
          if (this.email !== '') {
              formData.append('email', this.email)
          }
          if (this.password !== '') {
              formData.append('password', this.password)
          }
          if (this.repeatPassword !== '') {
              formData.append('repeatPassword', this.repeatPassword)
          }
          if (this.first_name !== '') {
              formData.append('first_name', this.first_name)
          }
          if (this.last_name !== '') {
              formData.append('last_name', this.last_name)
          }
          if (this.phone !== '') {
              formData.append('phone', this.phone)
          }
          console.log(formData)
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/registration',
            data: formData,
            headers: { 'Content-Type': 'multipart/form-data' }
            }).then(response => {
                    if (response.status === 200) {
                      console.log(response.data)
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
