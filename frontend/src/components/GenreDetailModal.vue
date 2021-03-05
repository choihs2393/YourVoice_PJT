<template>
    <v-app id="inspire" style="border: 1px solid gray; border-radius: 5px;">
        <div class="m-4 mb-2">
            <h3 class="jg">{{ this.title }}</h3>
        </div>
        <div v-if="this.arr.length===0">
            <v-progress-circular
                indeterminate
                color="orange"
                :size="100"
                :width="7"
                style="margin-left: 42%; margin-bottom: 10%;"
            ></v-progress-circular>
        </div>
        <div v-else class="container p-10 mb-2" style="overflow: auto; max-height: 600px;">
            <div v-for="(track, idx) in arr" :key="idx" class="ml-4 mt-4">
                <div class="d-flex justify-content-between ml-2 mr-2">
                    <div class="d-flex">
                        <div class="m-0 mr-3">
                            <img :src="track.album.images[1].url" style="width: 70px;">
                        </div>
                        <div>
                            <p class="mb-0 mt-1" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ track.artists[0].name }}</p>
                            <p class="mb-0 mt-1" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ track.name }}</p>
                        </div>
                    </div>
                    <div class="mt-5 d-flex">
                        <v-btn icon>
                            <v-icon v-if="track.preview_url" @click="playMusic_(track)" medium color="white">
                                mdi-play
                            </v-icon>
                            <v-icon v-else disabled medium color="white">
                                mdi-play
                            </v-icon>
                        </v-btn>
                        <v-btn icon @click="getMV(track.youtube_urls)">
                            <v-icon v-if="track.youtube_urls" medium color="red">
                                mdi-youtube
                            </v-icon>
                            <v-icon v-else disabled medium color="red">
                                mdi-youtube
                            </v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon v-if="track.youtube_mr" @click="getMR(track)" medium color="#FFB74D">
                                mdi-microphone-variant
                            </v-icon>
                            <v-icon v-else disabled medium color="#FFB74D">
                                mdi-microphone-variant
                            </v-icon>
                        </v-btn>
                    </div>
                </div>
            </div>
        </div>
        <div id="bottomSensor"></div>
    </v-app>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/scrollmonitor/1.2.0/scrollMonitor.js"></script>
<script>
import { mapActions } from 'vuex'
import axios from 'axios'
const SERVER_URL = "http://jlocalhost:8000/api/"

export default {
    name: 'GenreDetailModal',
    props: {
        genre: Number,
    },
    data() {
        return {
            arr: [],
            page: 0,
            title: '',
            urls: "www.youtube.com",
        }
  },
  methods: {
    ...mapActions('player', ['playMusic']),
    ...mapActions('karaoke', ['playMR']),

    getTrack_Genre: function() {

      if (this.genre == 0) {
          const _page = this.page++

          axios.get(SERVER_URL+'music/tracks/popularity/' +  _page + '/')
            .then(res => {
                this.arr = [...this.arr, ...res.data.data]
                // console.log(this.arr)
                // console.log(_page)              
            })
            .catch(err => console.error(err))
      } else if (this.genre == 5) {
           const _page = this.page++

          axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/' + 0 +'/')
            .then(res => {
                this.arr = [...this.arr, ...res.data.data]
                // console.log(this.arr)
                // console.log(_page)              
            })
            .catch(err => console.error(err))

        } else {
          const _page = this.page++

          axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/' + this.genre +'/')
            .then(res => {
                this.arr = [...this.arr, ...res.data.data]
                // console.log(this.arr)
                // console.log(_page)              
            })
            .catch(err => console.error(err))
      }
    },
    getMV(youtube_urls) {
        window.open('https://'+this.urls + youtube_urls, "_blank")
    },

    playMusic_(item){
        // console.log('playmusic at', item)
        this.playMusic(item)
    },
    
    getMR(gm) {
    //   console.log(gm)
      this.playMR(gm)
      this.$router.push("/karaoke")
    },

    addScrollWatcher: function () {
        const bottomSensor = document.querySelector('#bottomSensor')
        const watcher = scrollMonitor.create(bottomSensor)

        watcher.enterViewport(() => {
          setTimeout(() => {
            this.getTrack_Genre()
          }, 3000)
        })
    },
      
    loadUntilViewportIsFull: function () {
        const bottomSensor = document.querySelector('#bottomSensor')
        const watcher = scrollMonitor.create(bottomSensor)
        if (watcher.isFullyInViewport) {
          this.getTrack_Genre()
        }
      }
    },
    created() {
        this.getTrack_Genre()
    },
    mounted() {
        this.addScrollWatcher()
    },
    updated() {
        
        this.loadUntilViewportIsFull()

        if (this.genre == 0) {
            this.title = '인기 차트'
        } else if (this.genre == 1) {
            this. title = '밝고 경쾌한 음악'
        } else if (this.genre == 2) {
            this.title = '어쿠스틱'
        } else if (this.genre == 3) {
            this.title = '일렉트로 하우스'
        } else if (this.genre==4){
            this.title = '몽환적인 노래'
        } else {
            this.title = '잔잔한 댄스'
        }
    },

}
</script>

<style>
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
.v-application--wrap {
  min-height: 0 !important;
}
</style>
