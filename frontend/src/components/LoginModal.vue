<template>
  <v-app id="inspire" style="border: 1px solid gray; border-radius: 5px;">
      <v-container class="bg-img">
        <v-row justify="end">
          <v-btn @click="close()" icon class="mr-4" style="position: absolute;">
            <v-icon>mdi-close</v-icon>
          </v-btn>
      </v-row>
        <v-row justify="center">
         <v-col cols="10" class="pt-0 pb-0">
          <v-card-text style="text-align: center;">
            <img src="../assets/p1.png" style="width: 70%; image-rendering: pixelated;">
            <v-row justify="center">
              <h4>Login</h4>
            </v-row>
            <v-row justify="center">
              <hr class="logo-hr mt-0">
            </v-row>
            <v-container>
              <form @submit.prevent="onLogin">
                <v-row>
                  <v-col>
                    <v-text-field
                      class="mt-0 pt-0"
                      color="orange"
                      name="userid"
                      label="ID"
                      id="userid"
                      v-model="userid"
                      type="text"
                      required>
                      </v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-text-field
                      class="mt-0 pt-0"
                      color="orange"
                      name="password"
                      label="Password"
                      id="password"
                      v-model="password"
                      type="password"
                      required></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn block type="submit" style="background-color: darkorange;">Login</v-btn>
                  </v-col>
                </v-row>
              </form>
              <v-row class="social-login" justify="center" align="center">
                <hr>
              </v-row>
              <v-row>
                <v-col>
                </v-col>
              </v-row>
              <v-row justify="center">
                <p class="mr-2 mb-0">Don't have an account?</p>
                <!-- <router-link :to="{name: 'Signup'}" style="color: darkorange;">Signup here</router-link> -->
                <p @click="gotoSignup" style="color: darkorange; cursor: pointer;">Signup here</p>
              </v-row>
            </v-container>
          </v-card-text>
      </v-col>
    </v-row>
      </v-container>
  </v-app>
</template>

<script>
import SignupModal from '../components/SignupModal.vue'
import { mapActions } from 'vuex'

  export default {
    name: "Login",
    data () {
      return {
        userid: '',
        password: '',
      }
    },
    computed: {
      user () {
        return this.$store.getters.user
      }
    },
    watch: {
      user (value) {
        if (value !== null && value !== undefined) {
          this.$router.push('/')
        }
      }
    },
    methods: {
      ...mapActions('accounts', ['login']),

      onLogin: async function() {

        const loginData = {
          userid: this.userid,
          password: this.password,
        }
        await this.login(loginData)
        // this.$router.push('/')
        this.$emit('close')
      },
      gotoSignup() {
          this.$modal.show(SignupModal, {
          modal: this.$modal},{
              // resizable: true,
              // dynamic: true,
              scrollable: true,
              // minHeight: 450
              height: 'auto',
      })
      this.$emit('close')
      },

      close() {
        this.$emit('close')
      }
    }
  }
</script>

<style scoped>
.bg-img {
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;
  }

  .bg-img::after {
    width: 100%;
    height: 100%;
    content: "";
    background-image: url("https://cdn.pixabay.com/photo/2016/11/23/15/48/audience-1853662__340.jpg");
    /* background-image: url("https://img.hankyung.com/photo/201909/7383c761302e9fc005dec616762dae15.jpg"); */
    background-position: center;
    background-size: cover;
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    opacity: 0.5;
  }

  .logo-hr {
    width: 15%;
    height: 1px;
    background-color: darkorange;
  }
</style>