<template>
  <v-container class="pt-0 pb-sm-12 jg">
    <!-- <div class="loader" v-if='!artists.length && !music.length'></div> -->

      <!-- mobile screen -->
      <v-tabs
        fixed-tabs
        show-arrows
        color="white"
        background-color="#121212"
        center-active
        v-if="breakpoint.xs"
      >

        <!-- <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if="loading"
          :width="7"
          style="margin-left: 40%"
        ></v-progress-circular> -->
        <!-- <v-tab>ALL</v-tab> -->
        <v-tab>MUSIC</v-tab>
        <v-tab>ARTISTS</v-tab>
        <v-tab>ALBUMS</v-tab> 

        

        <!-- <v-tab-item>
          <v-expansion-panels v-model="panel">
              <v-expansion-panel>
                <v-expansion-panel-header expand-icon="" color="#272727">
                  <div>Music</div>
                </v-expansion-panel-header>
                <v-expansion-panel-content style="height: 300px; overflow: auto;">
                  <div class="row" style="overflow: auto;">
                    <div class="p-0 pb-1 col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in music" :key="idx">
                        <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                            <img :src="gm.album.images[1].url" alt="" @click="onPlayMusic(gm)" style="width: 50px; height: 50px;">
                            <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                                <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                                <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                            </div>
                            <div class="">
                              <v-btn icon>
                                <v-icon v-if="gm.preview_url" @click="onPlayMusic(gm)" color="white">
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
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header expand-icon="" color="#272727">
                  <div>Artists</div>
                </v-expansion-panel-header>
                <v-expansion-panel-content style="height: 300px; overflow: auto;">
                  <v-container class="mb-2" grid-list-md>
                    <v-layout row>
                      <v-flex xs6 sm4 md3 lg4 xl4 class="bg-transparent mb-4" style="height: 200px;" v-for="(artist, idx) in artists" :key="idx.id">
                        <v-card style="text-align: center; cursor: pointer;" @click="toArtistDetail(artist.id)">
                          <v-img
                            v-if="artist.images.length"
                            class="white--text align-end"
                            height="160px"
                            :src="artist.images[0].url"
                          >
                          </v-img>
                          <v-img
                            v-else
                            class="white--text align-end"
                            height="160px"
                            src="../assets/default_cover.png"
                          >
                          </v-img>
                          <p class="m-0" style="font-size: 15px; text-align: center;">{{ artist.name }}</p>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header expand-icon="" color="#272727">
                  <div>Albums</div>
                </v-expansion-panel-header>
                <v-expansion-panel-content style="height: 300px; overflow: auto;">
                  <v-container class="mb-2" grid-list-md>
                    <v-layout row>
                      <v-flex xs6 sm4 md3 lg4 xl4 class="bg-transparent mb-2" style="height: 200px;" v-for="(album, idx) in albums" :key="idx.id">
                        <v-card @click="albumtrack(album)" style="text-align: center; cursor: pointer;">
                          <v-img
                            v-if="album.images.length"
                            class="white--text align-end"
                            height="160px"
                            :src="album.images[0].url"
                          >
                          </v-img>
                          <v-img
                            v-else
                            class="white--text align-end"
                            height="160px"
                            src="../assets/default_cover.png"
                          >
                          </v-img>
                          <p class="m-0" style="font-size: 15px; text-align: center;">{{ album.name }}</p>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-expansion-panel-content>
              </v-expansion-panel>
          </v-expansion-panels>
        </v-tab-item> -->

        
          <!-- music -->
          <v-tab-item color="#121212">
            <div v-if="!music.length && loading">
              <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                :width="7"
                style="margin-left: 40%"
              ></v-progress-circular>
            </div>
            <v-container class="jg" v-else-if="!music.length">
              <v-row class="ma-4" justify="center">
                <h5>음악 검색 결과가 없습니다.</h5>
              </v-row>
            </v-container>
            <div v-else class="row" style="overflow: auto;">
              <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in music" :key="idx">
                  <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                      <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                      <img :src="gm.album.images[1].url" alt="" @click="onPlayMusic(gm)" style="width: 50px; height: 50px;">
                      <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                      <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                          <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                          <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                      </div>
                      <div class="mt-2">
                        <v-btn icon>
                                  <v-icon v-if="gm.preview_url" @click="onPlayMusic(gm)" color="white">
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
          </v-tab-item>

          <!-- artists -->
          <v-tab-item color="#121212">
            <div v-if="!artists.length && loading">
              <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                :width="7"
                style="margin-left: 40%"
              ></v-progress-circular>
            </div>
            <v-container class="jg" v-else-if="!artists.length">
              <v-row class="ma-4" justify="center">
                <h5>가수 검색 결과가 없습니다.</h5>
              </v-row>
            </v-container>
            <v-container v-else class="mb-2" grid-list-md>
              <v-layout row>
                <v-flex xs6 sm4 md3 lg4 xl4 class="bg-transparent mb-4" style="height: 200px;" v-for="(artist, idx) in artists" :key="idx.id">
                  <v-card style="text-align: center; background: transparent; cursor: pointer;" @click="toArtistDetail(artist.id)">
                    <v-img
                      v-if="artist.images.length"
                      class="white--text align-end"
                      height="170px"
                      :src="artist.images[0].url"
                    >
                    </v-img>
                    <v-img
                      v-else
                      class="white--text align-end"
                      height="170px"
                      src="../assets/default_cover.png"
                    >
                    </v-img>
                    <p class="m-0" style="font-size: 18px; text-align: center;">{{ artist.name }}</p>
                  </v-card>
                </v-flex>
                <!-- <div id="bottomSensor"></div> -->
              </v-layout>
            </v-container>
          </v-tab-item>

          <!-- albums -->
          <v-tab-item color="#121212">
            <div v-if="!albums.length && loading">
              <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                :width="7"
                style="margin-left: 40%"
              ></v-progress-circular>
            </div>
            <v-container class="jg" v-else-if="!albums.length">
              <v-row class="ma-4" justify="center">
                <h5>음악 검색 결과가 없습니다.</h5>
              </v-row>
            </v-container>
            <v-container v-else class="mb-2" grid-list-md>
              <v-layout row>
                <v-flex xs6 sm4 md3 lg4 xl4 class="bg-transparent mb-2" style="height: 200px;" v-for="(album, idx) in albums" :key="idx.id">
                  <v-card @click="albumtrack(album)" style="text-align: center; background: transparent; cursor: pointer;">
                    <v-img
                      v-if="album.images.length"
                      class="white--text align-end"
                      height="160px"
                      :src="album.images[0].url"
                    >
                    </v-img>
                    <v-img
                      v-else
                      class="white--text align-end"
                      height="160px"
                      src="../assets/default_cover.png"
                    >
                    </v-img>
                    <p class="m-0" style="font-size: 14px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">{{ album.name }}</p>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-tab-item>
      </v-tabs>
      <!-- mobile screen -->

      <!-- desktop and large screen -->
      <v-container v-else class="ma-4">
        <h3>Artists</h3>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if="!artists.length && loading"
          :width="7"
          style="margin-left: 40%"
        ></v-progress-circular>
        <v-container class="jg ma-4" v-else-if="!artists.length">
          <v-row justify="center">
            <h5>가수 검색 결과가 없습니다.</h5>
          </v-row>
        </v-container>
        <v-container v-else class="mb-2" grid-list-md>
          <v-row>
            <v-slide-group class="pa-4" active-class="secondary" show-arrows>
              <v-slide-item
                v-for="(artist, idx) in artists"
                :key="idx.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  class="ma-3"
                  :color="active ? undefined : 'transparent lighten-1'"
                  @click="toggle, toArtistDetail(artist.id)"
                  height="165"
                  width="140"
                >
                  <v-img
                    v-if="artist.images[0]"
                    :src="artist.images[0].url"
                    height="140"
                    width="140"
                  ></v-img>
                  <v-img
                    v-else
                    src="../assets/default_cover.png"
                    height="140"
                    width="140"
                  ></v-img>
                  <p class="m-0" style="font-size: 15px; text-align: center;">{{ artist.name }}</p>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-row>
        </v-container>

        <h3>Music</h3>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if="!music.length && loading"
          :width="7"
          style="margin-left: 40%"
        ></v-progress-circular>
        <v-container class="jg ma-4" v-else-if="!music.length">
          <v-row justify="center">
            <h5>음악 검색 결과가 없습니다.</h5>
          </v-row>
        </v-container>
        <v-container v-else class="mb-2" grid-list-md>
          <v-data-table
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

          </v-data-table>

          <div class="text-center pt-2">
            <v-pagination
              v-model="page_"
              :length="pageCount"
              color="orange"
            ></v-pagination>
          </div>
        </v-container>

        <h3>Albums</h3>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if="!albums.length && loading"
          :width="7"
          style="margin-left: 40%"
        ></v-progress-circular>
        <v-container class="jg ma-4" v-else-if="!albums.length">
          <v-row justify="center">
            <h5>앨범 검색 결과가 없습니다.</h5>
          </v-row>
        </v-container>
        <v-container v-else class="mb-2" grid-list-md>
          <v-row>
            <v-slide-group class="pa-4" active-class="secondary" show-arrows>
              <v-slide-item
                v-for="(album, idx) in albums"
                :key="idx.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  class="ma-3"
                  :color="active ? undefined : 'transparent lighten-1'"
                  @click="toggle, albumtrack(album)"
                  height="180"
                  width="140"
                >
                  <v-img
                    v-if="album.images[0]"
                    :src="album.images[0].url"
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
                  <p class="m-0" style="font-size: 14px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">{{ album.name }}</p>
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
  import api from '../api'
  import { mapActions } from 'vuex'

  import AlbumTrack from '../components/AlbumTrack.vue'

  export default {
    name: 'Seach',

    mounted() {
      // console.log('Search mounted')
      this.searchMusicInfo()
    },

    data() {
      return {
        page_: 1,
        pageCount: 0,
        itemsPerPage: 10,
        music: [],
        albums: [],
        artists: [],
        page: 0,
        headers: [
          { text: 'Title', align: 'start', sortable: false, value: 'name', width: 400 },
          { text: 'Artist', sortable: false, value: 'artists[0].name' },
          { text: 'Popularity', sortable: false, value: 'popularity' },
          // { text: 'Music', value: 'preview_url' },
          { text: 'Music', sortable: false, value: 'preview_url' },
          { text: 'Karaoke', sortable: false, value: 'youtube_mr' },
          { text: 'MV', sortable: false, value: 'youtube_urls' },
        ],
        avg_p: 0,
        max_p: 0,
        min_p: 0,
        obj_music: null,
        loading: true,
        panel: 0,
      }
    },

    computed: {
      breakpoint () {
        return this.$vuetify.breakpoint
      },
    },

    methods: {
      ...mapActions('player', ['playMusic', 'getAlbum']),
      ...mapActions('karaoke', ['playMR']),

      
      getMR(gm) {
        // console.log(gm)
        this.playMR(gm)
        this.$router.push("/karaoke")
      },
      searchMusicInfo: async function() {
        if (this.$route.query.keyword) {

          await api.searchMusicInfo(this.page, this.$route.query.keyword)
          .then(res => {
            this.artists = [...this.artists, ...res.data.data.artist]
            this.albums = [...this.albums, ...res.data.data.album.name, ...res.data.data.album.artist]
            this.music = [...this.music, ...res.data.data.track.name, ...res.data.data.track.artist]

            this.music.sort(function(a, b) {
              return a.name < b.name ? -1 : a.name > b.name ? 1 : 0
            })

            // console.log('가수목록', this.artists)
            // console.log('앨범목록', this.albums)
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

          this.loading = false
        }
      },

      getColor (popularity) {
        if (popularity == this.max_p) return 'red'
        else if (popularity >= this.avg_p) return 'orange'
        else if (popularity > this.min_p) return 'green'
        else return 'dark-yellow'
      },

      getMV(youtube_urls) {
        window.open('https://www.youtube.com' + youtube_urls, "_blank")
      },

      onPlayMusic(item){
        this.obj_music = {
          album: item.album,
          preview_url: item.preview_url,
          name: item.name,
          artists: item.artists,
          youtube_urls: item.youtube_urls
        }
        this.playMusic(this.obj_music)
      },

      albumtrack: async function(gm) {
        // console.log('gm', gm)
        await api.getAlbum(gm.id)
          .then(res => {
            // console.log('완료?', res.data)
            this.$modal.show(AlbumTrack, {
              album: res.data.data,
              modal: this.$modal
              },
              {
                // resizable: true,
                // dynamic: true,
                scrollable: true,
                // minHeight: 450
                height: 'auto',
              })
          })
          .catch(err => console.error(err.response.data))
      },

      toArtistDetail(artistId) {
        this.$router.push({name: 'ArtistDetail', query: {artistId: artistId}})
      }
    },
  }
</script>

<style>
  /* .loader {
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
  } */
  .v-expansion-panels {
    z-index: 0;
  }
</style>