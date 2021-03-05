<template>
  <v-app id="inspire">
    <v-container v-if="breakpoint.xs">
      <div class="d-flex mb-2">
        <h4 class="jg" style="color: orange;">{{ $store.state.accounts.userInfo.username }}</h4>
        <h4 class="jg">님의 추천 결과</h4>
      </div>
      <v-container class="pa-4 jg" v-for="(clusterList, idx) in resultMusic" :key="idx">
        <v-row>
          <h5 v-if="clusterList.cluster===0">어쿠스틱</h5>
          <h5 v-if="clusterList.cluster===1">밝고 경쾌한 음악</h5>
          <h5 v-if="clusterList.cluster===2">몽환적인 노래</h5>
          <h5 v-if="clusterList.cluster===3">발라드</h5>
          <h5 v-if="clusterList.cluster===4">잔잔한 댄스</h5>
        </v-row>
        <v-row>
          <div class="row" style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in clusterList.data" :key="idx">
              <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                <img :src="gm.album.images[1].url" alt="" @click="playMusic(gm)" style="width: 50px; height: 50px;">
                <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                  <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                  <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                </div>
                <div class="mt-2">
                  <v-btn icon>
                    <v-icon v-if="gm.preview_url" @click="playMusic(gm)" color="white">
                      mdi-play
                    </v-icon>
                    <v-icon v-else disabled color="white">
                      mdi-play
                    </v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon v-if="gm.youtube_urls" @click="getMV(gm.youtube_urls)" color="red">
                      mdi-youtube
                    </v-icon>
                    <v-icon v-else disabled color="red">
                      mdi-youtube
                    </v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon v-if="gm.youtube_mr" @click="getMR(gm)" color="#FFB74D">
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
        </v-row>
      </v-container>
    </v-container>
    <v-container v-else class="mb-2" grid-list-md>
      <div class="d-flex mb-2">
        <h2 class="jg" style="color: orange;">{{ $store.state.accounts.userInfo.username }}</h2>
        <h2 class="jg">님의 추천 결과입니다.</h2>
      </div>
          <v-container class="pa-4 jg" v-for="(clusterList, idx) in resultMusic" :key="idx">
            <v-row>
              <h5 v-if="clusterList.cluster===0">어쿠스틱</h5>
              <h5 v-if="clusterList.cluster===1">밝고 경쾌한 음악</h5>
              <h5 v-if="clusterList.cluster===2">몽환적인 노래</h5>
              <h5 v-if="clusterList.cluster===3">발라드</h5>
              <h5 v-if="clusterList.cluster===4">잔잔한 댄스</h5>
            </v-row>
            <v-row>
              <v-col
                class="bg-transparent mb-2"
                v-for="(music, idx) in clusterList.data"
                :key="idx"
                col="6"
                sm="4"
                md="3"
                lg="2"
              >
                <v-card
                  style="text-align: center; background: transparent; cursor: pointer; height: 190px; width: 150px;"
                  @click="playMusic(music)"
                >
                  <img v-if="music.album.images[0].url" :src="music.album.images[0].url" alt="" class="white--text align-end" style="width: 150px; height: 150px;">
                  <img v-else src="../assets/default_cover.png" alt="" class="white--text align-end" height="150" width="150">
                  <p class="m-0" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
    </v-container>
  </v-app>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'Result',

    props: {
      resultMusic: Array,
    },

    mounted() {
      // console.log('result mounted!!', this.resultMusic)
      const recommendMusic = {
        userid: localStorage.getItem('userid'),
        re_songs: []
      }

      for (let i of this.resultMusic) {
        for (let j of i.data) {
          recommendMusic.re_songs.push({ songid: j.id })
        }
      }
      console.log('re_song', recommendMusic)
      this.addRecommendSong(recommendMusic)
    },

    computed: {
      breakpoint () {
        return this.$vuetify.breakpoint
      },
    },

    data() {
      return {
        // selectMusic: [],
      }
    },
    methods: {
      ...mapActions('player', ['playMusic']),
      ...mapActions('karaoke', ['playMR']),
      ...mapActions('accounts', ['addRecommendSong']),

      getMV(youtube_urls) {
        window.open('https://www.youtube.com' + youtube_urls, "_blank")
      },

      getMR(gm) {
        console.log(gm)
        this.playMR(gm)
        this.$router.push("/karaoke")
      },

      // selectmusic(music) {
        // this.selectedMusic.push(music)
      // },
    }
  }
</script>

<style scoped>
.loader {
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 1;
    width: 150px;
    height: 150px;
    margin: -75px 0 0 -75px;
    border: 16px solid #f3f3f3;
    border-radius: 50%;
    border-top: 16px solid #3498db;
    width: 120px;
    height: 120px;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
}


/* @-webkit-keyframes spin {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
} */

/* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  background: transparent;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>

<style lang="scss">
.v-input--selection-controls .v-input__slot > .v-label, .v-input--selection-controls .v-radio > .v-label {
    margin-bottom: 0 !important;
  }
</style>