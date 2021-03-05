<template>
    <v-app id="inspire" class="p-2" style="border: 1px solid gray; border-radius: 5px;">
      <div v-if="!breakpoint.xs">
        <div v-if="this.album_detail == null">
          <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              style="margin-left: 45%;"
          ></v-progress-circular>
        </div>
        <div v-else>
          <div class="container" style="overflow: auto; max-height: 450px;">
            <div class="d-flex">
              <div>
                <v-img
                  class="white--text align-end mr-1"
                  width="100px"
                  height="100px"
                  :src="album_detail.images[0].url"
                >
                </v-img>
              </div>
              <div class="ml-2 mt-2">
                <h4>{{ album_detail.name }}</h4>
                <div class="d-flex">
                  <div class="mr-2">Artists: </div>
                  <div class="mr-2" v-for="artist in album_detail.artists" :key="artist.id">{{ artist.name }}  </div>
                </div>
                <div>Release date: {{ album_detail.release_date }}</div>
              </div>
            </div>
            <br>
            <!-- <div class="d-flex" v-for="track in album_detail.trackslist" :key="track.id">
              <div class="m-0 mr-1">
                <div>{{ track.track_number}}.</div>
              </div>
              <div>
                <p class="mb-0">{{ track.name }}</p>
            </div>
          </div> -->
        </div>

        <div>
          <v-data-table
            :headers="headers"
            :items="album_detail.trackslist"
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
                  color="#FFB74D"
                  disabled
                >
                mdi-microphone-variant
                </v-icon>
              </v-btn>
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
                  color="red"
                  disabled
                >
                mdi-youtube
                </v-icon>
              </v-btn>
            </template>

            <template v-slot:item.preview_url="{ item }">
              <v-btn icon>
                <v-icon
                  v-if="item.preview_url"
                  @click="playMusic_(item)"
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
        </div>
        </div>
      </div>
    
    <div v-else>
      <div v-if="this.album_detail == null">
        <v-progress-circular
            indeterminate
            color="orange"
            :size="30"
            style="margin-left: 45%;"
        ></v-progress-circular>
      </div>
      <div v-else class="container" style="overflow: auto; max-height: 450px;">
          <div class="d-flex">
            <div>
              <v-img
                class="white--text align-end mr-1"
                width="100px"
                height="100px"
                :src="album_detail.images[0].url"
              >
              </v-img>
            </div>
            <div class="ml-2 mt-2">
              <h5>{{ album_detail.name }}</h5>
              <div class="d-flex">
                <div class="mr-2">Artists: </div>
                <div class="mr-2" v-for="artist in album_detail.artists" :key="artist.id">{{ artist.name }}  </div>
              </div>
              <div>Release date: {{ album_detail.release_date }}</div>
            </div>
          </div>
          <br>
          <div v-for="track in album_detail.trackslist" :key="track.id">
            <!-- <v-menu offset-y>
              <template v-slot:activator="{ attrs, on }">
                <div class="d-flex" v-bind="attrs" v-on="on"> -->
                <div class="d-flex justify-content-between">
                  <div>
                    <div class="m-0 mr-3" style="width: 65%;">
                      <div>{{ track.track_number}}</div>
                    </div>
                    <div>
                      <p class="mb-0 mt-1" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ track.name }}</p>
                    </div>
                  </div>
                  <div class="mt-2 d-flex">
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
                <!-- </template>
                <v-list>
                  <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                  >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu> -->
            <v-divider class="m-0 mt-1 mb-1"></v-divider>
          </div>
      </div>
    </div>
    
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
import axios from 'axios'
const SERVER_URL = "http://localhost:8000/api/"


export default {
    data() {
      return {
        page_: 1,
        pageCount: 0,
        itemsPerPage: 5,
        // items: [
        //   { title: 'Click Me' },
        //   { title: 'Click Me' },
        //   { title: 'Click Me' },
        //   { title: 'Click Me 2' },
        // ],
        headers: [
          {
            text: 'Title',
            align: 'start',
            sortable: false,
            value: 'name',
            class: 'title'
            // width: '100px',
          },
          { text: 'Number', sortable: false, value: 'track_number' },
          { text: 'Popularity', sortable: false, value: 'popularity' },
          // { text: 'Music', value: 'preview_url' },
          { text: 'Music', sortable: false, value: 'preview_url' },
          { text: 'Karaoke', sortable: false, value: 'youtube_mr' },
          { text: 'MV', sortable: false, value: 'youtube_urls' },
        ],
        avg_p: 0,
        max_p: 0,
        min_p: 0,
        urls: "www.youtube.com",
        obj_music: null,
        tmp: null,
        album_detail: null,
        obj_mr: null,
      }
    },
    props: {
      album: Object,
    },
    computed: {
        breakpoint () {
        return this.$vuetify.breakpoint
        }
    },
    methods: {
      ...mapActions('player', ['playMusic']),
      ...mapActions('karaoke', ['playMR']),

      getTrack() {
        axios.get(SERVER_URL + 'music/album/' + this.album.id + '/')
          .then(res => {
            this.tmp = res.data
            this.album_detail = this.tmp.data
            this.average_p()    
          })
          .catch(err => console.error(err))
      },
      getColor (popularity) {
        if (popularity == this.max_p) return 'red'
        else if (popularity >= this.avg_p) return 'orange'
        else if (popularity > this.min_p) return 'green'
        else return 'dark-yellow'
      },
      average_p () {
        var num_p = 0
        var arr = []
        for (var i = 0; i < this.album_detail.total_tracks ; i++) {
          num_p += this.album_detail.trackslist[i].popularity
          arr.push(this.album_detail.trackslist[i].popularity)
        }
        this.avg_p = num_p / this.album_detail.total_tracks
        this.max_p = Math.max.apply(null, arr);
        this.min_p = Math.min.apply(null, arr);
      },
      getMV(youtube_urls) {
        window.open('https://'+this.urls + youtube_urls, "_blank")
      },
      getMR(item) {
        console.log("!!!",item)
        console.log('222', item, this.album_detail)
        this.obj_mr = { album: this.album_detail, cluster: item.cluster, preview_url: item.preview_url, name: item.name, artists: item.artists, youtube_urls: item.youtube_urls, youtube_mr: item.youtube_mr, id: item.id}
        this.playMR(this.obj_mr)
        this.$router.push("/karaoke")
        this.$emit('close')
      },

      // getMusic(preview_url) {
      //   window.open('https://'+this.urls + preview_url, "_blank")
      // }
      playMusic_(item){
        // console.log('playmusic at', item)
        this.obj_music = {album: this.album_detail, preview_url: item.preview_url, name: item.name, artists: item.artists, youtube_urls: item.youtube_urls}
        // console.log('obj', this.obj_music)
        this.playMusic(this.obj_music)
        // this.playMusic(item)
        // this.$store.dispatch("playMusic", {
        //   item: item
        // })
      },
    },
    mounted() {
      // this.average_p()
      this.getTrack()
    }
}
</script>

<style>
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

.v-application--wrap {
  min-height: 0 !important;
}

  /* td.text-start {
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    overflow:hidden;
  } */
</style>


<style lang="scss" scoped>
.v-application--wrap {
    min-height: 0 !important;
}
</style>