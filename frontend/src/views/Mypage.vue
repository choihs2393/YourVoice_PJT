<template>
  <v-container class="pt-0 mb-8 pb-6 pb-sm-12">

    <!-- <div v-if="loading">
      <v-progress-circular
        indeterminate
        color="orange"
        :size="100"
        v-if="!breakpoint.xs"
        :width="7"
        style="margin-top: 20%; margin-left: 45%;"
      ></v-progress-circular>

      <v-progress-circular
        indeterminate
        color="orange"
        :size="70"
        v-if="breakpoint.xs"
        :width="7"
        style="margin-top: 50%; margin-left: 40%;"
      ></v-progress-circular>
    </div> -->

    <!-- mobile screen -->
      <v-tabs
        fixed-tabs
        show-arrows
        color="white"
        background-color="#121212"
        center-active
        v-if="breakpoint.xs"
      >
        <!-- <v-tab>ALL</v-tab> -->
        <v-tab>VOICE</v-tab>
        <v-tab>TASTE</v-tab> 
        <v-tab>KARAOKE</v-tab>

        <!-- <v-tab-item>
          <h3>Artists</h3>
          <h3>Music</h3>
          <h3>Albums</h3>
        </v-tab-item> -->

        <!-- music -->
        <v-tab-item color="#121212">
          <div v-if="recommendVoice.length===0 && userInfo.pi_re_songs.length">
            <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                style="margin-left: 40%;"
            ></v-progress-circular>
          </div>
          <v-container class="jg" v-else-if="!userInfo.pi_re_songs.length">
            <v-row justify="center">
              <h5 class="ma-4" style="color: white;">데이터가 없습니다.</h5>
            </v-row>
          </v-container>
          <div v-else class="row" style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(music, idx) in recommendVoice" :key="idx.id">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="music.album.images[1].url" alt="" @click="playMusic(music)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon @click="playMusic(music)">
                        <v-icon color="white">
                          mdi-play
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMV(music.youtube_urls)">
                        <v-icon color="red">
                          mdi-youtube
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMR(music)">
                        <v-icon color="#FFB74D">
                          mdi-microphone-variant
                        </v-icon>
                      </v-btn>
                    </div>
                </div>
            </div>
          </div>
        </v-tab-item>
        <v-tab-item color="#121212">
          <div v-if="recommendTaste.length===0 && userInfo.re_songs.length">
            <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                style="margin-left: 40%;"
            ></v-progress-circular>
          </div>
          <v-container class="jg" v-else-if="!userInfo.re_songs.length">
            <v-row justify="center">
              <h5 class="ma-4" style="color: white;">데이터가 없습니다.</h5>
            </v-row>
          </v-container>
          <div v-else class="row" style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(music, idx) in recommendTaste" :key="idx.id">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="music.album.images[1].url" alt="" @click="playMusic(music)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon @click="playMusic(music)">
                        <v-icon color="white">
                          mdi-play
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMV(music.youtube_urls)">
                        <v-icon color="red">
                          mdi-youtube
                        </v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon color="#FFB74D" @click="getMR(music)">
                          mdi-microphone-variant
                        </v-icon>
                      </v-btn>
                    </div>
                </div>
            </div>
          </div>
        </v-tab-item>
        <v-tab-item color="#121212">
          <div v-if="sangMusic.length===0 && userInfo.sang_songs.length">
            <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                style="margin-left: 40%;"
            ></v-progress-circular>
          </div>
          <v-container class="jg" v-else-if="!userInfo.sang_songs.length">
            <v-row justify="center">
              <h5 class="ma-4" style="color: white;">데이터가 없습니다.</h5>
            </v-row>
          </v-container>
          <div v-else class="row" style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(music, idx) in sangMusic" :key="idx.id">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="music.album.images[1].url" alt="" @click="playMusic(music)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon @click="playMusic(music)">
                        <v-icon color="white">
                          mdi-play
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMV(music.youtube_urls)">
                        <v-icon color="red">
                          mdi-youtube
                        </v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon color="#FFB74D" @click="getMR(music)">
                          mdi-microphone-variant
                        </v-icon>
                      </v-btn>
                    </div>
                </div>
            </div>
          </div>
        </v-tab-item>
      </v-tabs>

      <!-- Desktop -->
      <v-container v-else>
        <h1>My Page</h1>
        <v-container class="mt-2 mb-2 jg" grid-list-md>
          <h4>목소리 추천 노래</h4>
          <div v-if="!recommendVoice.length && userInfo.pi_re_songs.length">
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              :width="7"
              style="margin-left: 45%;"
            ></v-progress-circular>
          </div>
          
          <v-container class="jg ma-4" v-else-if="!userInfo.pi_re_songs.length">
            <v-row justify="center">
              <h5>데이터가 없습니다.</h5>
            </v-row>
          </v-container>

          <v-row v-else>
            <v-slide-group class="pa-4" active-class="secondary" show-arrows>
              <v-slide-item
                v-for="music in recommendVoice"
                :key="music.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  class="ma-3"
                  :color="active ? undefined : 'transparent lighten-1'"
                  @click="toggle, playMusic(music)"
                  height="180"
                  width="140"
                >
                  <v-img
                    v-if="music.album.images[0]"
                    :src="music.album.images[0].url"
                    lazy-src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <v-img
                    v-else
                    src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <p class="m-0" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-row>

          <h4>취향 추천 노래</h4>
          <div v-if="!recommendTaste.length && userInfo.re_songs.length">
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              :width="7"
              style="margin-left: 45%;"
            ></v-progress-circular>
          </div>
          
          <v-container class="jg ma-4" v-else-if="!userInfo.re_songs.length">
            <v-row justify="center">
              <h5>데이터가 없습니다.</h5>
            </v-row>
          </v-container>
          <v-row v-else>
            <v-slide-group class="pa-4" active-class="secondary" show-arrows>
              <v-slide-item
                v-for="music in recommendTaste"
                :key="music.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  class="ma-3"
                  :color="active ? undefined : 'transparent lighten-1'"
                  @click="toggle, playMusic(music)"
                  height="180"
                  width="140"
                >
                  <v-img
                    v-if="music.album.images[0]"
                    :src="music.album.images[0].url"
                    lazy-src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <v-img
                    v-else
                    src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <p class="m-0" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-row>

          <h4>내가 부른 노래</h4>
          <div v-if="!sangMusic.length && userInfo.sang_songs.length">
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              :width="7"
              style="margin-left: 45%;"
            ></v-progress-circular>
          </div>
          
          <v-container class="jg ma-4" v-else-if="!userInfo.sang_songs.length">
            <v-row justify="center">
              <h5>데이터가 없습니다.</h5>
            </v-row>
          </v-container>
          <v-row v-else>
            <v-slide-group class="pa-4" active-class="secondary" show-arrows>
              <v-slide-item
                v-for="music in sangMusic"
                :key="music.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  class="ma-3"
                  :color="active ? undefined : 'transparent lighten-1'"
                  @click="toggle, playMusic(music)"
                  height="180"
                  width="140"
                >
                  <v-img
                    v-if="music.album.images[0]"
                    :src="music.album.images[0].url"
                    lazy-src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <v-img
                    v-else
                    src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <p class="m-0" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-row>
        </v-container>
      </v-container>
      <!-- desktop and large screen -->
    </v-container>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import api from '../api'

  export default {
    name: "Mypage",

    mounted() {
      const params = {
        userid: localStorage.getItem('userid'),
        page: 0
      }
      this.getUserSangSongs(params)
      this.getUserPiReSongs(params)
      this.getUserReSongs(params)
    },

    data() {
      return {
        sangMusic: [],
        recommendTaste: [],
        recommendVoice: [],
        loading: true,
      }
    },

    computed: {
      // ...mapState({
        // userInfo: state => state.accounts.userInfo,
      // }),

      ...mapGetters('accounts', ['userInfo']),

      breakpoint () {
        return this.$vuetify.breakpoint
      },
    },

    methods: {
      ...mapActions('player', ['playMusic']),
      ...mapActions('karaoke', ['playMR']),

      getMV(youtube_urls) {
        window.open('https://www.youtube.com' + youtube_urls, "_blank")
      },

      getMR(gm) {
        // console.log(gm)
        this.playMR(gm)
        this.$router.push("/karaoke")
      },

      getUserSangSongs: async function(params) {
        await api.getUserSangSongs(params)
          .then(res => {
            // console.log('결과', res.data.data)
            this.sangMusic = res.data.data

            if (this.sangMusic) {
              this.loading = false
            }
          })
          .catch(err => console.error(err.response.data))
      },

      getUserPiReSongs: async function(params) {
        await api.getUserPiReSongs(params)
          .then(res => {
            // console.log('결과', res.data.data)
            this.recommendVoice = res.data.data

            if (this.recommendVoice) {
              this.loading = false
            }
          })
          .catch(err => console.error(err.response.data))
      },

      getUserReSongs: async function(params) {
        await api.getUserReSongs(params)
          .then(res => {
            // console.log('결과', res.data.data)
            this.recommendTaste = res.data.data

            if (this.recommendTaste) {
              this.loading = false
            }
          })
          .catch(err => console.error(err.response.data))
      }
    },
  }
</script>
