<template>
  <v-container class="bg-img">
    <v-row justify="center">
      <v-col
        cols="12"
        sm="10"
        md="8"
        lg="5"
      >
<!--        <v-card>-->
          <v-card-text style="text-align: center;">
            <img src="../assets/p2.png" style="width: 70%; image-rendering: pixelated;">
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
                      name="password"
                      label="Password"
                      id="password"
                      v-model="password"
                      type="password"
                      required></v-text-field>
                  </v-col>
                </v-row>
                <v-row justify="end">
                  <p><a href="#">Forgot Password?</a></p>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn block type="submit" style="background-color: darkorange;">Login</v-btn>
                  </v-col>
                </v-row>
              </form>
              <v-row class="social-login" justify="center" align="center">
                <hr>
                <div class="ma-4">OR</div>
                <hr>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn block color="primary">
                    <v-icon class="mr-2">mdi-facebook</v-icon>
                    CONTINUE WITH FACEBOOK
                  </v-btn>
                </v-col>
              </v-row>
              <v-row justify="center">
                <p class="mr-2">Don't have an account?</p>
                <router-link :to="{name: 'Signup'}" style="color: darkorange;">Signup here</router-link>
              </v-row>
            </v-container>
          </v-card-text>
<!--        </v-card>-->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
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
        this.$router.push('/')
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

  .social-login > hr {
    width: 25%;
    background-color: #bdbebf;
  }
  
  .social-login > div {
    font-size: 15px;
    color: #bdbebf;
  }

</style>
