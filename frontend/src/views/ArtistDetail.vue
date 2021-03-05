<template>
  <v-app id="inspire">
    <v-container color="#121212" class="jg" v-if="breakpoint.xs">

      <v-tabs
        fixed-tabs
        show-arrows
        color="white"
        background-color="#121212"
        center-active
        v-if="breakpoint.xs"
      >
        <!-- <v-tab>ALL</v-tab> -->
        <v-tab>ARTISTS</v-tab>
        <v-tab>MUSIC</v-tab>
        <v-tab>ALBUMS</v-tab>
        
        <v-tab-item color="#121212" class="mt-2">  
        <!-- <h3>Artists</h3> -->
        <div v-if='arr.length === 0'>
            <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                style="margin-left: 40%; margin-top: 40%;"
                v-if="breakpoint.xs"
            ></v-progress-circular>
            <v-progress-circular
                indeterminate
                color="orange"
                :size="100"
                v-else
                :width="7"
                style="margin-top: 15%; margin-left: 45%"
            ></v-progress-circular>
        </div>
        <div v-else style="background: #121212;">
            <div>
                <v-card class="bg-light" style="text-align: center; width: 100%;">
                    <v-img
                        class="white--text align-end"
                        height="300px"
                        :src="artistData.images[0].url"
                    >
                    </v-img>
                </v-card>
                <div class="ml-4 mt-4">
                    <h3 style="color: white;">{{artistData.name}}</h3>
                    <v-divider></v-divider>
                    <h5 style="color: white;">Followers: {{artistData.followers}} (명)</h5>
                    <div class="d-flex">
                      <h5 class="mr-2" style="color: white;">Genres: </h5>
                      <div style="max-height: 162px; overflow: hidden;">
                          <h5 style="color: white;" v-for="(genre,idx) in artistData.genres" :key="idx" class="mr-2">{{genre.genre}}</h5>
                        </div>
                    </div>
                    <h5 style="color: white;">Popularity: 상위 {{100 - artistData.popularity}}%</h5>
                </div>
            </div>
            <hr>
          </div>
        </v-tab-item>

        <v-tab-item color="#121212" class="mt-2"> 
          <!-- <h3>Music</h3> -->
          <v-container color="#121212" grid-list-md>
              <div v-if="this.music.length==0">
                  <v-progress-circular
                      indeterminate
                      color="orange"
                      :size="70"
                      style="margin-left: 40%;"
                  ></v-progress-circular>
              </div>
              <div class="row jg" v-else style="overflow: auto;">
                <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in music" :key="idx">
                    <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                        <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                        <img :src="gm.album.images[1].url" alt="" style="width: 50px; height: 50px;">
                        <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
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

            <!-- <v-data-table
              v-else
              :headers="headers"
              :items="music"
              class="elevation-1"
            >
              <template v-slot:item.popularity="{ item }">
                <v-chip
                  :color="getColor(item.popularity)"
                  dark
                >
                  {{ item.popularity }}
                </v-chip>
              </template>
              
              <template v-slot:item.youtube_urls="{ item }">
                <v-btn icon>
                  <v-icon
                    v-if="item.youtube_urls"
                    color="red"
                    @click="getMV(item.youtube_urls)"
                  >
                  mdi-youtube
                  </v-icon>
                  <v-icon
                    v-else
                    disabled
                    color="red"
                  >
                  mdi-youtube
                  </v-icon>
                </v-btn>
              </template>

              <template v-slot:item.youtube_mr="{ item }">
                <v-btn icon>
                  <v-icon
                    v-if="item.youtube_mr"
                    color="#FFB74D"
                    @click="getMR(item)"
                  >
                    mdi-microphone-variant
                  </v-icon>
                  <v-icon
                    v-else
                    disabled
                    color="#FFB74D"
                  >
                    mdi-microphone-variant
                  </v-icon>
                </v-btn>
              </template>

              <template v-slot:item.preview_url="{ item }">
                <v-btn icon>
                  <v-icon
                    v-if="item.preview_url"
                    @click="onPlayMusic(item)"
                  >
                  mdi-play
                  </v-icon>
                  <v-icon
                    v-else
                    disabled
                  >
                  mdi-play
                  </v-icon>
                </v-btn>
              </template>

            </v-data-table> -->
          </v-container>
        </v-tab-item>

        <v-tab-item color="#121212">
          <!-- <h3>Albums</h3> -->
            <v-container class="mb-2" grid-list-md>
              <v-layout row>
                  <v-flex xs6 sm4 md3 lg3 xl3 class="bg-transparent mb-2" style="height: 200px;" v-for="gm in arr" :key="gm.id">
                  <!-- <div v-for="k in 30" :key="k.id"> -->
                      <v-hover>
                          <template v-slot:default="{ hover }">
                              <v-card @click="albumtrack(gm)" class="bg-light" style="text-align: center; cursor: pointer;">

                                  <v-img
                                      class="white--text align-end"
                                      height="200px"
                                      :src="gm.images[0].url"
                                  >
                                  </v-img>
                                  <v-fade-transition>
                                      <v-overlay
                                          v-if="hover"
                                          absolute
                                          color="#FFA726"
                                      >
                                      <p>{{ gm.name }}</p>
                                      </v-overlay>
                                  </v-fade-transition>

                              </v-card>
                          </template>
                      </v-hover>
                  </v-flex>
              </v-layout>
              
          </v-container>
          </v-tab-item>
        </v-tabs>
      <modals-container />
      
    </v-container>




    <v-container v-else class="jg">
      <h1>Artists</h1>
      <div v-if='arr.length === 0'>
          <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              style="margin-left: 40%; margin-top: 40%;"
              v-if="breakpoint.xs"
          ></v-progress-circular>
          <v-progress-circular
              indeterminate
              color="orange"
              :size="100"
              v-else
              :width="7"
              style="margin-top: 15%; margin-left: 45%"
          ></v-progress-circular>
      </div>
      <div v-else style="margin-bottom:96px">
          <div class="d-flex">
              <v-card class="bg-light" style="text-align: center; width: 50%;">
                  <v-img
                      class="white--text align-end"
                      height="300px"
                      :src="artistData.images[0].url"
                  >
                  </v-img>
              </v-card>
              <!-- test-->
              <div class="ml-4">
                  <h1>{{artistData.name}}</h1>
                  <v-divider></v-divider>
                  <h5>Followers: {{artistData.followers}} (명)</h5>
                  <div class="d-flex">
                    <h5 class="mr-2">Genres: </h5>
                    <!-- <div v-for="(genre,idx) in artistData.genres" :key="idx"> -->
                      <div style="max-height: 162px; overflow: hidden;">
                        <h5 v-for="(genre,idx) in artistData.genres" :key="idx" class="mr-2">{{genre.genre}}</h5>
                      </div>
                      
                      <!-- <span class="mr-1" v-for="(genre,idx) in artistData.genres" :key="idx" style="font-size: 20px; padding-bottom: 8px;">{{genre.genre}} </span> -->
                    <!-- </div> -->
                  </div>
                  <h5 class="mb-0">Popularity: 상위 {{100 - artistData.popularity}}%</h5>
              </div>
          </div>
          <hr>

        <h3>Music</h3>
        <v-container class="mb-2" grid-list-md>
            <div v-if="this.music.length==0">
                <v-progress-circular
                    indeterminate
                    color="orange"
                    :size="70"
                    style="margin-left: 45%;"
                ></v-progress-circular>
            </div>
          <v-data-table
            v-else
            :headers="headers"
            :items="music"
            class="elevation-1"
            hide-default-footer
            @page-count="pageCount = $event"
            :page.sync="page_"
            :items-per-page="itemsPerPage"
          >
            <template v-slot:item.popularity="{ item }">
              <v-chip
                :color="getColor(item.popularity)"
                dark
              >
                {{ item.popularity }}
              </v-chip>
            </template>
            
            <template v-slot:item.youtube_urls="{ item }">
              <v-btn icon>
                <v-icon
                  v-if="item.youtube_urls"
                  color="red"
                  @click="getMV(item.youtube_urls)"
                >
                mdi-youtube
                </v-icon>
                <v-icon
                  v-else
                  disabled
                  color="red"
                >
                mdi-youtube
                </v-icon>
              </v-btn>
            </template>

            <template v-slot:item.youtube_mr="{ item }">
              <v-btn icon>
                <v-icon
                  v-if="item.youtube_mr"
                  color="#FFB74D"
                  @click="getMR(item)"
                >
                  mdi-microphone-variant
                </v-icon>
                <v-icon
                  v-else
                  disabled
                  color="#FFB74D"
                >
                  mdi-microphone-variant
                </v-icon>
              </v-btn>
            </template>

            <template v-slot:item.preview_url="{ item }">
              <v-btn icon>
                <v-icon
                  v-if="item.preview_url"
                  @click="playMusic(item)"
                >
                mdi-play
                </v-icon>
                <v-icon
                  v-else
                  disabled
                >
                mdi-play
                </v-icon>
              </v-btn>
            </template>

          </v-data-table>
          <div class="text-center pt-2">
            <v-pagination
              v-model="page_"
              :length="pageCount"
              color="orange"
            ></v-pagination>
          </div>
        </v-container>

          <h2>Albums</h2>
              <v-container class="mb-2" grid-list-md>
              <v-layout row>
                  <v-flex xs6 sm4 md3 lg3 xl3 class="bg-transparent mb-2" style="height: 200px;" v-for="gm in arr" :key="gm.id">
                  <!-- <div v-for="k in 30" :key="k.id"> -->
                      <v-hover>
                          <template v-slot:default="{ hover }">
                              <v-card @click="albumtrack(gm)" class="bg-light" style="text-align: center; cursor: pointer;">

                                  <v-img
                                      class="white--text align-end"
                                      height="200px"
                                      :src="gm.images[0].url"
                                  >
                                  </v-img>
                                  <v-fade-transition>
                                      <v-overlay
                                          v-if="hover"
                                          absolute
                                          color="#FFA726"
                                      >
                                      <p>{{ gm.name }}</p>
                                      </v-overlay>
                                  </v-fade-transition>

                              </v-card>
                          </template>
                      </v-hover>
                  </v-flex>
              </v-layout>
          </v-container>
      </div>
      <modals-container />
    </v-container>
  </v-app>
</template>

<script>
import AlbumTrack from '../components/AlbumTrack.vue'
import axios from 'axios'
import api from '../api'
import { mapActions } from 'vuex'
const SERVER_URL = "http://localhost:8000/api/"

export default {
  name: 'ArtistDetail',
  mounted() {
    // console.log('ArtistDetail mounted!!')
    this.getArtist()
    this.getAlbum()
    // this.searchMusicInfo()
    // console.log('w0ow', this.artistData)
  },

  data() {
      return {
          page_: 1,
          pageCount: 0,
          itemsPerPage: 10,
          music: [],
          arr: [],
          page: 0,
          page_1: 0,
          overlay: false,
          show: false,
          artistId: '',
          artistData: '',
          avg_p: 0,
            max_p: 0,
            min_p: 0,
          headers: [
          { text: 'Title', align: 'start', sortable: false, value: 'name', width: 400 },
          { text: 'Artist', sortable: false, value: 'artists[0].name' },
          { text: 'Popularity', sortable: false, value: 'popularity' },
          // { text: 'Music', value: 'preview_url' },
          { text: 'Music', sortable: false, value: 'preview_url' },
          { text: 'Karaoke', sortable: false, value: 'youtube_mr' },
          { text: 'MV', sortable: false, value: 'youtube_urls' },
        ],
      }
  },
  computed: {
      breakpoint () {
      return this.$vuetify.breakpoint
      },
  },
  methods: {
    ...mapActions('karaoke', ['playMR']),
    ...mapActions('player', ['playMusic', 'getAlbum']),
    
    getMR(gm) {
      // console.log(gm)
      this.playMR(gm)
      this.$router.push("/karaoke")
    },

    getMV(youtube_urls) {
        window.open('https://www.youtube.com' + youtube_urls, "_blank")
    },

    getArtist: async function() {
      this.artistId = this.$route.query.artistId
      await api.getArtist(this.artistId)
        .then(res => {
          this.artistData = res.data.data
          this.searchMusicInfo()
          // console.log('w0ow', this.artistData)
        })
        .catch(err => console.error(err.response.data))
    },

    getAlbum: async function() {

    const _page = this.page++
    // console.log(_page)

    await axios.get(SERVER_URL+'music/artists/albums/' +  _page + '/' + this.artistId + '/')
        .then(res => {
        // console.log(res.data.data)
        this.arr = [...this.arr, ...res.data.data]
        // console.log(this.arr)
        // console.log(this.arr[0].id)
        // console.log('!', this.arr)
        // console.log(_page)              
        })
          .catch(err => console.error(err.response.data))
      },

      albumtrack(gm) {
          // console.log('gm', gm)
          this.$modal.show(AlbumTrack, {
              album: gm,
              modal: this.$modal},{
                  // resizable: true,
                  // dynamic: true,
                  scrollable: true,
                  // minHeight: 450
                  height: 'auto',
          })
          // console.log('wowowowow')
      },

      searchMusicInfo: async function() {
          
        if (this.artistData.name) {

          await api.searchMusicInfo(this.page_1, this.artistData.name)
          .then(res => {
            this.music = [...this.music, ...res.data.data.track.artist]

            if (this.music) {
              this.loading = false
            }

            this.music.sort(function(a, b) {
              return a.name < b.name ? -1 : a.name > b.name ? 1 : 0
            })

            // console.log('노래목록', this.music)

            var num_p = 0
            var arr = []

            for (var i = 0; i < this.music.length ; i++) {
              num_p += this.music[i].popularity
              arr.push(this.music[i].popularity)
            }
            this.avg_p = num_p / this.music.length
            this.max_p = Math.max.apply(null, arr)
            this.min_p = Math.min.apply(null, arr)
          })
          .catch(err => console.error(err.response.data))
        }
      },
      getColor (popularity) {
        if (popularity == this.max_p) return 'red'
        else if (popularity >= this.avg_p) return 'orange'
        else if (popularity > this.min_p) return 'green'
        else return 'dark-yellow'
      },

  },
}
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}

.v-window-item {
  background-color: #121212;
  /* color: #121212; */
}

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

.row{
  display: flex !important;
  flex-wrap: wrap !important;
  flex: 1 1 auto !important;
}

@-webkit-keyframes spin {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* .with-chevron[aria-expanded='true'] i {
  display: block;
  transform: rotate(180deg) !important;
} */
</style>
