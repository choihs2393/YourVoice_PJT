<template>
  <v-app id='inspire'>
    <div class="container jg">
      <h1>Artists</h1>
      <!-- <h1>arr: {{ ids }}</h1> -->
      <v-container class="mb-2" grid-list-md>
        <v-layout row>
            <v-flex xs6 sm4 md3 lg4 xl4 class="bg-transparent mb-2" style="height: 200px;" v-for="(gm, idx) in arr" :key="idx">
              <!-- <div v-for="k in 30" :key="k.id"> -->
                <v-hover>
                  <template v-slot:default="{ hover }">
                    <v-card class="bg-light" @click="artistDetail(gm)" style="text-align: center; cursor: pointer;">
                      <v-img
                        class="white--text align-end"
                        height="200px"
                        :src="gm.images[0].url"
                      >
                  <!-- <v-img
                    class="white--text align-end"
                    height="200px"
                    :src="require(`../assets/album/${gm.thumbnail}.jpg`)"
                  > -->
                    <!-- <v-card-title>{{ gm.name }}</v-card-title> -->
                      </v-img>

                      <v-fade-transition>
                        <v-overlay
                            v-if="hover"
                            absolute
                            color="#FFA726"
                        >
                        <h3>{{ gm.name }}</h3>
                        </v-overlay>
                    </v-fade-transition>
                  </v-card>
              </template>
              </v-hover>
              <!-- </div> -->
            </v-flex>
            <div id="bottomSensor"></div>
        </v-layout>
      </v-container>
    </div>
  </v-app>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/scrollmonitor/1.2.0/scrollMonitor.js"></script>
<script>
// import ArtistDetail from '../components/ArtistDetail.vue'
import axios from 'axios'
const SERVER_URL = "http://localhost:8000/api/"

export default {
  name: 'ArtistList',

  data() {
      return{
          overlay: false,
          page: 0,
          recommend: false,
          select_musics: [],
          arr: [],
        }
  },
  components: {
    // ArtistDetail
  },
  methods: {
    artistDetail(gm) {
      // console.log('artist', gm)
      this.$router.push({name: 'ArtistDetail', query: {artistId: gm.id}})
    },
    
    getArtist: function () {

        const _page = this.page++
        // console.log(_page)

        axios.get(SERVER_URL+'music/artists/follwers/' +  _page + '/')
          .then(res => {
            // console.log(res)
            this.arr = [...this.arr, ...res.data.data]
            // console.log(this.arr)
            // console.log(_page)              
          })
          .catch(err => console.error(err))
      },
      
      addScrollWatcher: function () {
        const bottomSensor = document.querySelector('#bottomSensor')
        const watcher = scrollMonitor.create(bottomSensor)

        watcher.enterViewport(() => {
          setTimeout(() => {
            this.getArtist()
          }, 1000)
        })
      },
      
      scrollToTop: function () {
        scroll(0, 0)
      },
      
      loadUntilViewportIsFull: function () {
        const bottomSensor = document.querySelector('#bottomSensor')
        const watcher = scrollMonitor.create(bottomSensor)
        if (watcher.isFullyInViewport) {
          this.getArtist()
        }
      }
    },
    created() {
      this.getArtist()
    },
    mounted() {
      this.addScrollWatcher()
    },
      
    updated() {
      this.loadUntilViewportIsFull()
    },
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
    border-top: 16px solid darkorange;
    width: 120px;
    height: 120px;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
}


@-webkit-keyframes spin {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.row{
  display: flex !important;
  flex-wrap: wrap !important;
  flex: 1 1 auto !important;
}
</style>