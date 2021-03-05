<template>
  <v-app id="inspire">
      <div class="container">

          <div v-if="breakpoint.xs">
              <div class="d-flex">
                    <h3 class="jg" style="color: orange;">{{ userInfo.username}}</h3><h3 class="jg">님을 위한</h3>
                </div>
                <h3 class="jg">맞춤 추천 노래입니다.</h3>

                <div v-if="result_arr.length===0">
                  <v-progress-circular
                    indeterminate
                    color="orange"
                    :size="70"
                    style="margin-left: 40%; margin-top: 5%;"
                    ></v-progress-circular>
                </div>

                <div class="row" v-else style="height: 240px; overflow: auto;">
                    <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(recommend, idx) in result_arr" :key="idx">
                        <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                            <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                            <img :src="recommend.album.images[1].url" alt="" style="width: 50px; height: 50px;">
                            <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                            <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                                <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.album.artists[0].name }}</p>
                                <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.name }}</p>
                            </div>
                            <div class="mt-2">
                            <v-btn icon>
                                <v-icon v-if="recommend.preview_url" @click="playMusic_(recommend)" color="white">
                                mdi-play
                                </v-icon>
                                <v-icon v-else disabled color="white">
                                mdi-play
                                </v-icon>
                            </v-btn>
                            <v-btn icon>
                                <v-icon v-if="recommend.youtube_urls" @click="getMV(recommend.youtube_urls)" color="red">
                                mdi-youtube
                                </v-icon>
                                <v-icon v-else disabled color="red">
                                mdi-youtube
                                </v-icon>
                            </v-btn>
                            <v-btn icon>
                                <v-icon v-if="recommend.youtube_mr" @click="getMR(recommend)" color="#FFB74D">
                                mdi-microphone-variant
                                </v-icon>
                                <v-icon v-else disabled color="#FFB74D">
                                mdi-microphone-variant
                                </v-icon>
                            </v-btn>
                            </div>
                        </div>
                    </div>
                </div>

                <v-divider></v-divider>

                 <div class="d-flex">
                    <h5 class="jg">이 노래는 어떠세요?</h5>
                </div>

                <div v-if="result_arr.length===0">
                  <v-progress-circular
                    indeterminate
                    color="orange"
                    :size="70"
                    style="margin-left: 40%; margin-top: 5%;"
                    ></v-progress-circular>
                </div>

                <div class="row" v-else style="height: 240px; overflow: auto;">
                    <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(recommend, idx) in result_arr" :key="idx">
                        <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                            <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                            <img :src="recommend.album.images[1].url" alt="" style="width: 50px; height: 50px;">
                            <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                            <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                                <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.album.artists[0].name }}</p>
                                <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.name }}</p>
                            </div>
                            <div class="mt-2">
                            <v-btn icon>
                                <v-icon v-if="recommend.preview_url" @click="playMusic_(recommend)" color="white">
                                mdi-play
                                </v-icon>
                                <v-icon v-else disabled color="white">
                                mdi-play
                                </v-icon>
                            </v-btn>
                            <v-btn icon>
                                <v-icon v-if="recommend.youtube_urls" @click="getMV(recommend.youtube_urls)" color="red">
                                mdi-youtube
                                </v-icon>
                                <v-icon v-else disabled color="red">
                                mdi-youtube
                                </v-icon>
                            </v-btn>
                            <v-btn icon>
                                <v-icon v-if="recommend.youtube_mr" @click="getMR(recommend)" color="#FFB74D">
                                mdi-microphone-variant
                                </v-icon>
                                <v-icon v-else disabled color="#FFB74D">
                                mdi-microphone-variant
                                </v-icon>
                            </v-btn>
                            </div>
                        </div>
                    </div>
                </div>

          </div>

          <div v-else>
              <div class="d-flex">
                    <h1 class="jg" style="color: orange;">{{ userInfo.username}}</h1>
                    <h1 class="jg">님을 위한 맞춤 추천 노래입니다.</h1>
                </div>

              <div>
                  <!-- <div class="d-flex">
                    <h3 class="jg" style="color: orange;">{{ userInfo.username}}</h3>
                    <h3 class="jg">님, 이 가수의 노래는 어떠세요?</h3>
                </div>
                  <v-container class="mb-2" grid-list-md>
                        <v-layout row>
                            <v-flex xs6 sm4 md3 lg2 xl2 class="bg-transparent mb-2" style="height: 200px;" v-for="(recommend, idx) in result_arr" :key="idx">
                            <v-card
                                class="ma-3"
                                height="180"
                                width="140"
                            >
                                <v-img lazy-src="../assets/default_cover.png" :src="recommend.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
                                <p class="m-0" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.album.artists[0].name }}</p>
                                <p class="m-0" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.name }}</p>
                            
                            </v-card>

                            </v-flex>
                        </v-layout>
                    </v-container> -->

                <!-- <v-divider></v-divider> -->

              </div>
              <div v-if="result_arr.length===0">
                  <v-progress-circular
                    indeterminate
                    color="orange"
                    :size="70"
                    style="margin-left: 40%; margin-top: 5%;"
                ></v-progress-circular>
              </div>
              <div v-else class="d-flex mr-10 justify-content-between">

                <v-slide-group
                    class="pa-4"
                    active-class="secondary"
                    show-arrows
                >
                    <v-slide-item
                    v-for="(recommend, idx) in result_arr" 
                    :key="idx"
                    v-slot:default="{ active, toggle }"
                    >
                    <v-card
                        :color="active ? undefined : 'transparent lighten-1'"
                        class="ma-3"
                        @click="toggle"
                        height="185"
                        width="145"
                    >
                        <v-img lazy-src="../assets/default_cover.png" :src="recommend.album.images[1].url" alt="musicPic" @click="playMusic_(recommend)" style="width: 145px;"></v-img>
                        <p class="m-0" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.album.artists[0].name }}</p>
                        <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.name }}</p>
                    
                    </v-card>
                </v-slide-item>
            </v-slide-group>

            </div>

            <v-divider></v-divider>

            <div class="d-flex">
                <h3 class="jg">이 노래는 어떠세요?</h3>
            </div>

            <div v-if="recommendTaste.length===0 && userInfo.re_songs.length">
                  <v-progress-circular
                    indeterminate
                    color="orange"
                    :size="70"
                    style="margin-left: 40%; margin-top: 5%;"
                ></v-progress-circular>
            </div>
            
            <v-container class="jg" v-else-if="!userInfo.re_songs.length">
                <v-row justify="center">
                    <h4>추천 데이터가 충분하지 않습니다.</h4>
                </v-row>
                <v-row justify="center">
                    <h4>내 취향으로 추천받기를 이용하여 노래를 추천 받아보세요!</h4>
                </v-row>
            </v-container>

            <div v-else class="d-flex mr-10 justify-content-between">

                </div>

                <v-slide-group
                    class="pa-4"
                    active-class="secondary"
                    show-arrows
                >
                    <v-slide-item
                    v-for="(recommend, idx) in recommendTaste" 
                    :key="idx"
                    v-slot:default="{ active, toggle }"
                    >
                    <v-card
                        :color="active ? undefined : 'transparent lighten-1'"
                        class="ma-3"
                        @click="toggle"
                        height="185"
                        width="145"
                    >
                        <v-img lazy-src="../assets/default_cover.png" :src="recommend.album.images[1].url" alt="musicPic" @click="playMusic_(recommend)" style="width: 145px;"></v-img>
                        <p class="m-0" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.album.artists[0].name }}</p>
                        <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ recommend.name }}</p>
                    
                    </v-card>
                </v-slide-item>
            </v-slide-group>
              
          </div>

          
      </div>
      
      <!-- <p>{{ result_arr }}</p> -->

  </v-app>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'
import api from '../api'
const SERVER_URL = "http://localhost:8000/api/"

export default {
    data() {
        return{
            result_arr: [],
            recommendTaste: [],
            singer: []
        }
    },
    computed: {
        ...mapGetters('accounts', ['isLoggedIn', 'userInfo']),

        breakpoint () {
        return this.$vuetify.breakpoint
        }
  },
  created() {
    //   this.$store.dispatch("accounts/getUserInfo", {
    //     userid: localStorage.getItem('userid')
    //   })
  },
  mounted() {
      if (!localStorage.getItem('authorization')) {
        this.$router.push('/')
      } else {
        this.get_voice_recommend()
        this.getUserReSongs()
      }
  },
  methods: {
    ...mapActions('player', ['playMusic']),
    ...mapActions('accounts', ['addPiRecommendSong']),

    playMusic_(item){
    //   console.log('playmusic at', item)
      this.playMusic(item)
    },

    get_voice_recommend: async function() {
        // console.log(this.userInfo)
        await axios.post(SERVER_URL + 'music/pitch/recommend/', {
            'userid': localStorage.getItem('userid')
        }).then(async res => {
            // console.log('결과!!!!',res.data)
            // this.result_arr = [...this.result_arr, ...res.data]
            // this.result_arr.push(res)
            this.result_arr = res.data.data
            }
        )
        .catch(err => console.error(err.response.data))

        const recommendMusic = {
            userid: localStorage.getItem('userid'),
            pi_re_songs: []
        }

        for (let i of this.result_arr) {
            recommendMusic.pi_re_songs.push({ songid: i.id })
        }

        this.addPiRecommendSong(recommendMusic)
    },

    getUserReSongs: async function() {
        const params = {
            userid: localStorage.getItem('userid'),
            page: 0
        }

        await api.getUserReSongs(params)
          .then(res => {
            // console.log('결과', res.data.data)
            this.recommendTaste = res.data.data

            // if (this.recommendTaste) {
            //   this.loading = false
            // }
          })
          .catch(err => console.error(err.response.data))
      },
  }
}
</script>

<style>

</style>