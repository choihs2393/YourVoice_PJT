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
              <h4>Signup</h4>
            </v-row>
            <v-row justify="center">
              <hr class="logo-hr mt-0">
            </v-row>
            <v-container>
              <form @submit.prevent="onSignup">
                <v-row>
                  <v-col>
                    <v-text-field
                      class="mt-0 pt-0"
                      name="userid"
                      label="Userid"
                      id="userid"
                      v-model="userid"
                      type="text"
                      required>
                        <template v-slot:append-outer>
                          <v-btn outlined small rounded @click="idCheck(userid)">Check</v-btn>
                        </template>
                      </v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-text-field
                      class="mt-0 pt-0"
                      name="username"
                      label="Name"
                      id="username"
                      v-model="username"
                      type="text"
                      required></v-text-field>
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
                <v-row>
                  <v-col>
                    <v-text-field
                      class="mt-0 pt-0"
                      name="confirmPassword"
                      label="Confirm Password"
                      id="confirmPassword"
                      v-model="confirmPassword"
                      type="password"
                      :rules="[comparePasswords]"
                      ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col col="12" sm="6">
                    <v-text-field
                      name="borntime"
                      label="Birthday"
                      id="borntime"
                      v-model="borntime"
                      type="date"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      :items="items"
                      v-model="gender"
                      label="Gender"
                    ></v-select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn block type="submit" style="background-color: darkorange;">Signup</v-btn>
                  </v-col>
                </v-row>
              </form>
            </v-container>
          </v-card-text>
        <!-- </v-card> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import { mapActions } from "vuex";

  export default {
    name: 'Signup',
    
    data () {
      return {
        userid: '',
        username: '',
        password: '',
        confirmPassword: '',
        borntime: '',
        items: ['남자', '여자'],
        gender: ''
      }
    },
    computed: {
      comparePasswords () {
        return this.password === this.confirmPassword
      },
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
      ...mapActions('accounts', ['signup', 'idCheck']),

      onSignup: async function() {

        const signupData = {
          userid: this.userid,
          username: this.username,
          password: this.password,
          borntime: this.borntime,
          gender: this.gender,
        }
        await this.signup(signupData)
        this.$router.push('/')
      },
    },
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