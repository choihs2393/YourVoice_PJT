<template>
  <v-app id="inspire">
    <!-- <v-container> -->
      <v-container class="mb-4" v-if="!recommend">
        <div v-if="breakpoint.xs">
        <div class="d-flex">
          <h1>Recommend</h1>
          <v-tooltip bottom color="black">
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon class="mt-3">
                <v-icon style="font-size: 20px;" v-bind="attrs" v-on="on">
                  mdi-help-circle-outline        
                </v-icon>
              </v-btn>
            </template>
            <span>
              <div class="m-2 jg" style="text-align: left;">
                <p class="m-0">사용자 취향 별 분석을 통한 맞춤 음악 추천 서비스입니다.</p>
                <p class="m-0">직접 원하는 노래를 선택해 클릭한 뒤,</p>
                <div class="d-flex">
                  <p class="m-0">하단 아래의</p><p class="m-0 ml-1 mr-1" style="color: orange;">'RECOMMEND'</p><p class="m-0"> 버튼을 눌러주세요.</p>
                </div>
                <p class="m-0">직접 고른 노래를 기반으로 빅데이터 분석을 통해 추천 음악을 제공합니다.</p>
                <!-- <p class="m-0">맞춤 노래 추천 서비스입니다.</p> -->
              </div>
            </span>
          </v-tooltip>
        </div>
        <v-row class="m-1">
            <v-radio-group
              v-model="selectedGenre"
              :mandatory="false"
              row
              @change="getMusic(selectedGenre)"
            >
              <v-radio color="orange" class="jg" label="HOT" value="5"></v-radio>
              <v-radio color="orange" class="jg" label="DANCE" value="0"></v-radio>
              <v-radio color="orange" class="jg" label="CHEERFUL" value="1"></v-radio>
              <v-radio color="orange" class="jg" label="DREAMY" value="2"></v-radio>
              <v-radio color="orange" class="jg" label="ACOUSTIC" value="3"></v-radio>
              <v-radio color="orange" class="jg" label="ELECTRO" value="4"></v-radio>
<!-- 
              <v-radio color="orange" class="jg" label="HOT" value="5"></v-radio>
              <v-radio color="orange" class="jg" label="ACOUSTIC" value="0"></v-radio>
              <v-radio color="orange" class="jg" label="CHEERFUL" value="1"></v-radio>
              <v-radio color="orange" class="jg" label="DREAMY" value="2"></v-radio>
              <v-radio color="orange" class="jg" label="BALLAD" value="3"></v-radio>
              <v-radio color="orange" class="jg" label="DANCE" value="4"></v-radio> -->
            </v-radio-group>
            <v-col class="pb-0">
              <!-- <div class="input-group mb-3">
                <input v-model="searchKeyword" @keydown.enter="onSearch()" type="text" class="form-control" placeholder="Search Music or Arists" aria-label="Recipient's username" aria-describedby="basic-addon2">
                <div class="input-group-append">
                  <button @click="onSearch()" class="btn btn-outline-secondary" type="button" style="color: white;">Search</button>
                </div>
              </div> -->
              <v-text-field
                placeholder="Search Music or Artists"
                :append-icon="mdiMusic"
                single-line
                hide-details
                class="p-0 pb-2"
                v-model="searchKeyword"
                @keydown.enter="onSearch()"
                color="white"
              />
            </v-col>
          </v-row>
          <v-container class="mb-4 pb-2 jg" grid-list-md style="height: 370px; overflow: auto;">
            <div v-if="searchMusic.length===0">
              <v-progress-circular
                indeterminate
                color="orange"
                :size="70"
                style="margin-left: 40%; margin-top: 10%;"
              ></v-progress-circular>
            </div>
            <v-row v-else style="position: relative; z-index: 0;">
              <v-overlay
                class="d-flex align-start"

                z-index=1
                :absolute="absolute"
                :value="!isLoggedIn"
                opacity="0.85"
              >
                <div style="text-align: center; margin: 150px;">
                    <p class="mb-1 jg">로그인이 필요한 서비스입니다.</p>
                    <v-btn style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</v-btn>
                </div>
              </v-overlay>
             <div class="row" style="overflow: auto;">
                <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in searchMusic" :key="idx">
                    <div @click="selectmusic(gm)" class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                      <img :src="gm.album.images[1].url" alt="" style="width: 50px; height: 50px;">
                      <div class="mr-2" style="width: 75%; color: white; text-align: left;">
                          <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                          <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                      </div>
                    </div>
                </div>
              </div>
            </v-row>
          </v-container>
          <v-divider></v-divider>
        
          <h3>Select Music</h3>
          <v-container class="pt-0 mb-4 pb-2 jg" grid-list-md style="height: 370px; overflow: auto; position: relative; z-index: 0;">
            <v-overlay
            class="d-flex align-start"

            z-index=1
            :absolute="absolute"
            :value="flag && selectedMusic.length"
            opacity="0.85"
          >
            <div class="d-flex mb-2" style=" margin: 130px;">
              <h5 class="jg">분석 중..</h5>
            </div>
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              style="margin-left: 40%;"
            ></v-progress-circular>
          </v-overlay>
            <div class="row" style="overflow: auto;">
              <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in selectedMusic" :key="idx">
                <div @click="deleteMusic(gm.id)" class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                  <img :src="gm.album.images[1].url" alt="" style="width: 50px; height: 50px;">
                  <div class="mr-2" style="width: 75%; color: white; text-align: left;">
                    <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                    <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                  </div>
                </div>
              </div>
            </div>
          </v-container>
          <v-container>
            <v-row>
              <v-btn block @click="goResult()" style="color: orange; border: 1px solid orange;">Recommend</v-btn>
              <!-- <button class="btn" @click="goResult()" style="color: orange; border: 1px solid orange;">Recommend</button> -->
            </v-row>
           <br>
          </v-container>
        </div>
        <!-- mobile end -->

        <div v-else>
          <v-row>
            <h1>Recommend</h1>
            <v-tooltip bottom color="black">
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon class="mt-3">
                  <v-icon style="font-size: 20px;" v-bind="attrs" v-on="on">
                    mdi-help-circle-outline        
                  </v-icon>
                </v-btn>
              </template>
              <span>
                <div class="m-2 jg" style="text-align: left;">
                  <p class="m-0">사용자 취향 별 분석을 통한 맞춤 음악 추천 서비스입니다.</p>
                  <p class="m-0">직접 원하는 노래를 선택해 클릭한 뒤,</p>
                  <div class="d-flex">
                    <p class="m-0">하단 아래의</p><p class="m-0 ml-1 mr-1" style="color: orange;">'RECOMMEND'</p><p class="m-0"> 버튼을 눌러주세요.</p>
                  </div>
                  <p class="m-0">직접 고른 노래를 기반으로 빅데이터 분석을 통해 추천 음악을 제공합니다.</p>
                  <!-- <p class="m-0">맞춤 노래 추천 서비스입니다.</p> -->
                </div>
              </span>
            </v-tooltip>
          </v-row>
          <v-row class="m-1">
            <v-radio-group
              v-model="selectedGenre"
              :mandatory="false"
              row
              @change="getMusic(selectedGenre)"
            >
              <v-radio color="orange" class="jg" label="HOT" value="5"></v-radio>
              <v-radio color="orange" class="jg" label="DANCE" value="0"></v-radio>
              <v-radio color="orange" class="jg" label="CHEERFUL" value="1"></v-radio>
              <v-radio color="orange" class="jg" label="DREAMY" value="2"></v-radio>
              <v-radio color="orange" class="jg" label="ACOUSTIC" value="3"></v-radio>
              <v-radio color="orange" class="jg" label="ELECTRO" value="4"></v-radio>
<!-- 
              <v-radio color="orange" class="jg" label="HOT" value="5"></v-radio>
              <v-radio color="orange" class="jg" label="ACOUSTIC" value="0"></v-radio>
              <v-radio color="orange" class="jg" label="CHEERFUL" value="1"></v-radio>
              <v-radio color="orange" class="jg" label="DREAMY" value="2"></v-radio>
              <v-radio color="orange" class="jg" label="BALLAD" value="3"></v-radio>
              <v-radio color="orange" class="jg" label="DANCE" value="4"></v-radio> -->
            </v-radio-group>
            <v-col class="pb-0">
              <!-- <div class="input-group mb-3">
                <input v-model="searchKeyword" @keydown.enter="onSearch()" type="text" class="form-control" placeholder="Search Music or Arists" aria-label="Recipient's username" aria-describedby="basic-addon2">
                <div class="input-group-append">
                  <button @click="onSearch()" class="btn btn-outline-secondary" type="button" style="color: white;">Search</button>
                </div>
              </div> -->
              <v-text-field
                placeholder="Search Music or Artists"
                :append-icon="mdiMusic"
                single-line
                hide-details
                class="p-0 pb-2"
                v-model="searchKeyword"
                @keydown.enter="onSearch()"
                color="white"
              />
            </v-col>
          </v-row>
        
        <v-container class="mb-4 pb-2 jg" grid-list-md style="height: 370px; overflow: auto;">
          <div v-if="searchMusic.length===0">
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              style="margin-left: 45%; margin-top: 10%;"
            ></v-progress-circular>
          </div>
          <v-row v-else class="" style="position: relative; z-index: 0;">
            <v-overlay
              class="d-flex align-start"

              z-index=1
              :absolute="absolute"
              :value="!isLoggedIn"
              opacity="0.85"
            >
              <div style="text-align: center; margin: 150px;">
                  <p class="mb-1 jg">로그인이 필요한 서비스입니다.</p>
                  <v-btn style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</v-btn>
              </div>
            </v-overlay>
            <!-- <v-col
              class="bg-transparent mb-2"
              v-for="music in searchMusic" :key="music.id"
            > -->
              <v-card
                style="text-align: center; cursor: pointer; width: 145px; height: 180px;"
                @click="selectmusic(music)"
                class="bg-transparent ma-2"
                v-for="(music, idx) in searchMusic" :key="idx.id"
              >
                <img v-if="music.album.images[0].url" :src="music.album.images[1].url" alt="" class="white--text align-end" style="width: 145px; height: 140px;">
                <img v-else src="../assets/default_cover.png" alt="" class="white--text align-end" style="width: 140px; height: 140px;">
                <p class="m-0" style="font-size: 13px;overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
              </v-card>
            </v-row>
            <!-- </v-col> -->
        </v-container>

        <v-divider></v-divider>
        
        <h2>Select Music</h2>
        <v-container class="mb-2" style="height: 370px; overflow: auto; position: relative; z-index: 0;" grid-list-md>
          <v-overlay
            class="d-flex align-start"

            z-index=1
            :absolute="absolute"
            :value="flag"
            opacity="0.85"
          >
            <div class="d-flex mb-2" style="text-align: center; margin: 130px;">
              <h4 class="jg" style="color: orange;">{{ $store.state.accounts.userInfo.username }}</h4>
              <h4 class="jg">님의 음악 취향을 분석 중입니다.</h4>
            </div>
            <v-progress-circular
              indeterminate
              color="orange"
              :size="70"
              style="margin-left: 45%;"
            ></v-progress-circular>
          </v-overlay>
          <v-row class="ml-2">
            <!-- <v-col
              class="bg-transparent mb-2"
              v-for="music in selectedMusic"
              :key="music.id"
              col="6"
              sm="4"
              md="3"
              lg="2"
            > -->
              <v-card
                style="text-align: center; cursor: pointer; width: 140px; height: 180px;"
                @click="deleteMusic(music.id)"
                class="bg-transparent ma-2 jg"
                v-for="(music, idx) in selectedMusic"
                :key="idx.id"
              >
                <img v-if="music.album.images[1].url" :src="music.album.images[1].url" alt="" class="white--text align-end" style="width: 140px; height: 140px;">
                <img v-else src="../assets/default_cover.png" alt="" class="white--text align-end" style="width: 140px; height: 140px;">
                <p class="m-0" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.artists[0].name }}</p>
                <p class="m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ music.name }}</p>
              </v-card>
            <!-- </v-col> -->
          </v-row>
        </v-container>
        <v-container>
          <v-row>
            <v-btn block @click="goResult()" style="color: orange; border: 1px solid orange;">Recommend</v-btn>
            <!-- <button class="btn" @click="goResult()" style="color: orange; border: 1px solid orange;">Recommend</button> -->
          </v-row>
          <br>
        </v-container>
        </div>
      </v-container>

      <v-container v-else>
        <Result :resultMusic="resultMusic" />
      </v-container>
    <!-- </v-container> -->
  </v-app>
</template>

<script>
  import { mapGetters } from 'vuex'
  import { mdiMusic } from '@mdi/js';

  import LoginModal from '../components/LoginModal.vue'

  import Result from '../components/Result.vue'
  import api from '../api'

  export default {
    name: 'RecommendTaste',

    components: {
      Result
    },

    mounted() {
      this.getMusic(this.selectedGenre)
    },

    computed: {
      ...mapGetters('accounts', ['isLoggedIn']),

      breakpoint () {
        return this.$vuetify.breakpoint
      },
    },

    data() {
      return{
        mdiMusic,
        searchKeyword: "",
        recommend: false,
        selectedMusic: [],
        selectedGenre: '5',
        searchMusic: [],
        resultMusic: [],
        absolute: true,
        flag: false,
      }
    },
    methods: {
      selectmusic(music) {
        if (!this.selectedMusic.includes(music)) {
          this.selectedMusic.push(music)
        }
      },
      deleteMusic(musicId) {
        const idx = this.selectedMusic.findIndex(item => item.id === musicId)
        if (idx > -1) this.selectedMusic.splice(idx, 1)
      },

      goResult: async function() {
        this.flag = true
        if (this.selectedMusic.length && localStorage.getItem('authorization')) {
          
          const params = {
            userid: localStorage.getItem('userid'),
            selectmusic: []
          }

          for (let music of this.selectedMusic) {
            params.selectmusic.push({ songid: music.id })
          }
                                                                                                                                                                                                                                                                                                                                     
          await api.recommendTasteMusic(params)
            .then(res => {
              this.resultMusic = [...res.data.data]
              this.recommend = true
              // console.log('resultMusic', this.resultMusic)
            })
            .catch(err => err.response.data)
        }
      },
      onSearch: async function() {
        // console.log('검색', this.searchKeyword)
        if (this.searchKeyword) {

          await api.searchMusicInfo(0, this.searchKeyword)
          .then(res => {
            this.searchMusic = [...res.data.data.track.name, ...res.data.data.track.artist]

            this.searchMusic.sort(function(a, b) {
              return a.name < b.name ? -1 : a.name > b.name ? 1 : 0
            })

            // console.log('검색 노래', this.searchMusic)
          })
          .catch(err => console.error(err.response.data))
        }
      },

      gotoLogin() {
      this.$modal.show(LoginModal, {
          modal: this.$modal},{
              // resizable: true,
              // dynamic: true,
              scrollable: true,
              // minHeight: 450
              height: 'auto',
      })
    },

      getMusic: async function(selectedGenre) {
        if (selectedGenre === "5") {
          await api.getPopularityMusic(0)
            .then(res => {
              this.searchMusic = [...res.data.data]
            })
            .catch(err => console.error(err.response.data))
        } else {
          await api.getClusterMusic(0, selectedGenre)
            .then(res => {
              this.searchMusic = [...res.data.data]
            })
            .catch(err => console.error(err.response.data))
        }
      }
    }
  }
</script>

<style scoped>
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
    font-size: 13px;
  }
</style>