<template>
  <v-app id="inspire">
    <div v-if="!recommend">
    <div v-if="breakpoint.xs" class="container" style="height: 100%; z-index: 0;">
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
              <p class="m-0">사용자 음성 분석을 통한</p>
              <p class="m-0">맞춤 노래 추천 서비스입니다.</p>
              <br>
              <div class="d-flex">
                <p class="mr-2"><v-icon color="red" class="mr-1">mdi-record</v-icon>RECORD VOICE: </p>
                <div>
                  <p class="m-0"> Record 버튼을 눌러 노래를 부른 뒤, 마음에 드는 파일을 선택해 제출해 주세요.</p>
                  <p class="m-0"> 최소 5초, 최대 20초의 녹음시간을 권장합니다.</p>
                </div>
              </div>
              <v-divider></v-divider>
              <div class="d-flex">
                <p class="mr-2"><v-icon small class="mr-1">mdi-file</v-icon>UPLOAD VOICE FILE: </p>
                <div>
                  <p class="m-0">직접 녹음한 음성 파일을 제출해 업로드 해 주세요.</p>
                  <p class="m-0">분석 가능한 음성 파일 형식은 .wav 이며, 300kb 이하의 음성 파일 제출을 권장합니다.</p>
                </div>
              </div>
            </div>
          </span>
        </v-tooltip>
      </div>

      <div class="container">
        <div class="mb-2">
          <v-expansion-panels>
              <v-expansion-panel>
                <v-expansion-panel-header expand-icon="" color="#272727">
                  <div style="text-align: center;">
                    <v-icon color="red" class="mr-1">
                      mdi-record
                    </v-icon>
                    RECORD VOICE
                  </div>
                </v-expansion-panel-header>
                <v-expansion-panel-content v-if="isLoggedIn" color="#272727">
                  <Record />
                </v-expansion-panel-content>
                <v-expansion-panel-content color="#272727" v-else>
                  <div style="text-align: center;">
                    <h5 class="jg">로그인이 필요한 기능입니다.</h5>
                    <br>
                    <button class="btn" style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</button>
                  </div>
                </v-expansion-panel-content>
              </v-expansion-panel>
          </v-expansion-panels>
        </div>
        <div class="mb-2">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header expand-icon="" color="#272727">
                <div style="text-align: center;">
                  <v-icon class="mr-1">
                    mdi-file
                  </v-icon>
                  UPLOAD VOICE FILE
                </div>
              </v-expansion-panel-header>
              <v-expansion-panel-content v-if="isLoggedIn" color="#272727">
                <div class="form-group" style="color: black;">
                  <!-- <v-file-input 
                    ref='file'
                    label=".WAV 파일만 가능합니다." 
                    accept=".wav, .WAV" 
                    v-on:change="handleFileUpload()"
                    show-size 
                    counter 
                    multiple>
                  </v-file-input> -->
                  <input v-on:change="handleFileUpload()" type="file" ref="file" class="form-control-file justify-content-center" id="exampleFormControlFile1" style="width: 30%; display: block; margin : 0 auto;">
                </div>
                <div class="d-flex justify-content-center">
                  <button class="btn" style="color: orange; border: 1px solid orange;" @click="fileupload">Submit</button>
                </div>
              </v-expansion-panel-content>
              <v-expansion-panel-content color="#272727" v-else>
                  <div style="text-align: center;">
                    <h5 class="jg">로그인이 필요한 기능입니다.</h5>
                    <br>
                    <button class="btn" style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</button>
                  </div>
                </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
      </div>

      <v-divider></v-divider>

      <div class="container" v-if="!isLoggedIn || !userInfo.pi_re_songs.length">
        <h5>New & Hot</h5>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='arr.length === 0' 
          style="margin-left: 40%;"
        ></v-progress-circular>
        <div class="row" v-else style="overflow: auto; height: 250px;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in arr" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <img :src="gm.album.images[1].url" alt="" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <div class="mr-1 mt-2" style="width: 35%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon @click="playMusic_(gm)">
                        <v-icon color="white">
                          mdi-play
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMV(gm.youtube_urls)">
                        <v-icon color="red">
                          mdi-youtube
                        </v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon color="#FFB74D">
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
            <h5 class="jg" style="color: orange;">{{ userInfo.username }}</h5>
            <h5 class="jg">님 추천 노래</h5>
          </div>
          <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='recommendVoice.length === 0' 
          style="margin-left: 40%;"
        ></v-progress-circular>
        <div class="row" v-else style="overflow: auto; height: 250px;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in recommendVoice" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <img :src="gm.album.images[1].url" alt="" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <div class="mr-1 mt-2" style="width: 35%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 13px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon @click="playMusic_(gm)">
                        <v-icon color="white">
                          mdi-play
                        </v-icon>
                      </v-btn>
                      <v-btn icon @click="getMV(gm.youtube_urls)">
                        <v-icon color="red">
                          mdi-youtube
                        </v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon color="#FFB74D">
                          mdi-microphone-variant
                        </v-icon>
                      </v-btn>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>



    <!-- Desktop-->

    <div v-else class="container justify-content-center">
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
              <p>사용자 음성 분석을 통한 맞춤 노래 추천 서비스입니다.</p>
              <br>
              <div class="d-flex">
                <p class="mr-2"><v-icon color="red" class="mr-1">mdi-record</v-icon>RECORD VOICE: </p>
                <div>
                  <p class="m-0"> Record 버튼을 눌러 노래를 부른 뒤,</p>
                  <p class="m-0"> 마음에 드는 파일을 선택해 제출해 주세요.</p>
                  <p class="m-0"> 최소 5초, 최대 20초의 녹음시간을 권장합니다.</p>
                </div>
              </div>
              <v-divider></v-divider>
              <div class="d-flex">
                <p class="mr-2"><v-icon small class="mr-1">mdi-file</v-icon>UPLOAD VOICE FILE: </p>
                <div>
                  <p class="m-0">직접 녹음한 음성 파일을 제출해 업로드 해 주세요.</p>
                  <p class="m-0">분석 가능한 음성 파일 형식은 .wav 이며,</p>
                  <p class="m-0">300kb 이하의 음성 파일 제출을 권장합니다.</p>
                </div>
              </div>
            </div>
          </span>
        </v-tooltip>
      </div>

      <div class="container">
        <div class="mb-2">
          <v-expansion-panels>
              <v-expansion-panel>
                <v-expansion-panel-header expand-icon="" color="#272727">
                  <div style="text-align: center;">
                    <v-icon color="red" class="mr-1">
                      mdi-record
                    </v-icon>
                    RECORD VOICE
                  </div>
                </v-expansion-panel-header>
                <v-expansion-panel-content color="#272727" v-if="isLoggedIn">
                  <Record />
                </v-expansion-panel-content>
                <v-expansion-panel-content color="#272727" v-else>
                  <div style="text-align: center;">
                    <h5 class="jg">로그인이 필요한 기능입니다.</h5>
                    <br>
                    <button class="btn" style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</button>
                  </div>
                </v-expansion-panel-content>
              </v-expansion-panel>
          </v-expansion-panels>
        </div>
        <div class="mb-2">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header expand-icon="" color="#272727">
                <div style="text-align: center;">
                  <v-icon class="mr-1">
                    mdi-file
                  </v-icon>
                  UPLOAD VOICE FILE
                </div>
              </v-expansion-panel-header>
              <v-expansion-panel-content color="#272727" v-if="isLoggedIn">
                <div class="form-group" style="color: black;">
                  <!-- <v-file-input 
                    ref="file"
                    type="file"
                    label=".WAV 파일만 가능합니다." 
                    accept=".wav, .WAV" 
                    @change="handleFileUpload()" 
                    show-size 
                    counter 
                    multiple>
                  </v-file-input> -->
                  <input v-on:change="handleFileUpload()" type="file" ref="file" class="form-control-file justify-content-center" id="exampleFormControlFile1" style="width: 30%; display: block; margin : 0 auto;">
                </div>
                <div class="d-flex justify-content-center">
                  <button class="btn" style="color: orange; border: 1px solid orange;" @click="fileupload">Submit</button>
                </div>
              </v-expansion-panel-content>
              <v-expansion-panel-content color="#272727" v-else>
                  <div style="text-align: center;">
                    <h5 class="jg">로그인이 필요한 기능입니다.</h5>
                    <br>
                    <button class="btn" style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</button>
                  </div>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
      </div>

      <v-divider></v-divider>
        <div class="container" v-if="!isLoggedIn || !userInfo.pi_re_songs.length">
          <h3>New & Hot</h3>
          <v-progress-circular
            indeterminate
            color="orange"
            :size="100"
            v-if="!arr.length"
            :width="7"
            style="margin-top: 5%; margin-left: 45%"
          ></v-progress-circular>
          <div v-else class="d-flex mr-10 justify-content-between">
            <v-slide-group
              class="pa-4"
              active-class="secondary"
              show-arrows
            >
              <v-slide-item
                v-for="gm in arr"
                :key="gm.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  :color="active ? undefined : 'transparent lighten-1'"
                  class="ma-3"
                  @click="toggle"
                  height="180"
                  width="140"
                >
                  <v-img lazy-src="../assets/default_cover.png" :src="gm.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
                  <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.album.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.name }}</p>
                
                </v-card>
              </v-slide-item>
            </v-slide-group>
            </div>
        </div>
        <div v-else>
          <div class="d-flex">
            <h3 class="jg" style="color: orange;">{{ userInfo.username }}</h3>
            <h3 class="jg">님을 위한 맞춤 추천 노래입니다.</h3>
          </div>
          <v-progress-circular
                indeterminate
                color="orange"
                :size="100"
                v-if="recommendVoice.length === 0"
                :width="7"
                style="margin-top: 5%; margin-left: 45%"
          ></v-progress-circular>

          <div v-else class="d-flex mr-10 justify-content-between">
              
            </div>
              <v-slide-group
              class="pa-4"
              active-class="secondary"
              show-arrows
            >
              <v-slide-item
                v-for="gm in recommendVoice"
                :key="gm.id"
                v-slot:default="{ active, toggle }"
              >
                <v-card
                  :color="active ? undefined : 'transparent lighten-1'"
                  class="ma-3"
                  @click="toggle"
                  height="180"
                  width="140"
                >
                  <v-img lazy-src="../assets/default_cover.png" :src="gm.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
                  <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.album.artists[0].name }}</p>
                  <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.name }}</p>
                
                </v-card>
              </v-slide-item>
            </v-slide-group>
        </div>
      </div>
    </div>
    <div v-else>
      <h1>결과화면</h1>
    </div>
  </v-app>
</template>

<script>
import Record from '../views/Record'
import { mapGetters, mapActions } from 'vuex'
import api from '../api'
import $ from 'jquery'
import axios from 'axios'
import swal from 'sweetalert';
import LoginModal from '../components/LoginModal.vue'

const SERVER_URL = "http://localhost:8000/api/"

export default {
  data() {
    return{
      RecDT: false,
      audioSource: null,
      soundfile: [],
      recopen: false,
      file: '',
      arr: [],
      page_0: 0,
      recommend: false,
      recommendVoice: [],
      // rules: [
      // value => !value || value.size < 7000000 || 'File size should be less than 7 MB!',
      // ],
      categories: ["이 노래 어떠세요?", "NEW & HOT"],

    }
  },
  components: {
    Record
  },
  mounted() {
    this.getTrack_Hot()
    if (localStorage.getItem('authorization')) {
      this.getUserPiReSongs()
    }
  },
  computed: {
        ...mapGetters('accounts', ['isLoggedIn']),
        ...mapGetters('accounts', ["userInfo"]),

        breakpoint () {
        return this.$vuetify.breakpoint
        }
  },
  methods: {
    ...mapActions('player', ['playMusic']),

    gotoRecord() {
      this.$router.push('/recommend_voice/record')
    },
    gotoUpload() {
      this.$router.push('/recommend_voice/upload')
    },
    getMV(youtube_urls) {
        window.open('https://'+this.urls + youtube_urls, "_blank")
    },

    playMusic_(item){
        // console.log('playmusic at', item)
        this.playMusic(item)
      },
    getTrack_Hot () {

      const _page = this.page_0++
      // console.log('hot', _page)

      axios.get(SERVER_URL+'music/tracks/popularity/' +  _page + '/')
        .then(res => {
          this.arr = [...this.arr, ...res.data.data]
          // console.log(this.arr)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    handleFileUpload(){
      this.file = this.$refs.file.files[0];
      // console.log('handlefileupload', this.$refs.file)
    },
    fileupload() {
      let formData = new FormData();
      // console.log('handlefileupload', this.$refs.file)
      formData.append('file', this.file);    
      formData.append('userid', this.userInfo.userid)
      // console.log('fileupload', this.file)
      axios.post( SERVER_URL + 'accounts/get_pitch_file/',
              formData,
              {
              headers: {
                  'Content-Type': 'multipart/form-data'
              }
            }
          ).then(
            swal("your request is approved", {
                icon: "success",
              })
              .then(()=>{
              this.$router.push('/recommend_voice/result')  
            })
      )
      .catch(function(){
        console.log('FAILURE!!');
      });
       
    },
    changecol() {
      // console.log('!')
      if($('#recButton').hasClass('notRec')){
        $('#recButton').removeClass("notRec");
        $('#recButton').addClass("Rec");
        this.recopen = true
      }
      else{
        // console.log('!!')
        $('#recButton').removeClass("Rec");
        $('#recButton').addClass("notRec");
        this.recopen = false
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

    getUserPiReSongs: async function() {
      const params = {
        userid: localStorage.getItem('userid'),
        page: 0
      }
        await api.getUserPiReSongs(params)
          .then(res => {
            // console.log('결과', res.data.data)
            // this.sangMusic = res.data.data.sang_songs
            // this.recommendTaste = res.data.data.re_songs
            this.recommendVoice = res.data.data

            // if (this.sangMusic || this.recommendTaste || this.recommendVoice) {
              // this.loading = false
            // }
          })
          .catch(err => console.error(err.response.data))
    },
  }
}
</script>


<style scoped>
.v-progress-circular {
  margin: 1rem;
}
  
.button_rec {
	width: 35px;
	height: 35px;
	font-size: 0;
	background-color: red;
	border: 0;
	border-radius: 35px;
	margin: 18px;
	outline: none;
}

.notRec{
	background-color: darkred;
}

.Rec{
	animation-name: pulse;
	animation-duration: 1.5s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
}

/* 
button{background: 0 none; border: 0 none;}
.buttons{position: relative; text-align: center; margin-top: 300px;}
.buttons button{overflow: hidden; position: relative; display: inline-block; vertical-align: top; width: 200px; height: 100px; line-height: 100px; border: 1px solid #225ea7; transition: all 0.5s;}
.buttons button:hover{color: #fff;}
.buttons button:before{content: ""; z-index: -1; position: absolute; background-color: #225ea7 !important; transition: all 1s;}

.buttons.buttons2 .button6:before{left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(45deg); width: 200%; height: 0;}
.buttons.buttons2 .button6:hover:before{height: 300%;} */

</style>

<style lang="scss">
@keyframes pulse{
	0%{
		box-shadow: 0px 0px 5px 0px rgba(173,0,0,.3);
	}
	65%{
		box-shadow: 0px 0px 5px 13px rgba(173,0,0,.3);
	}
	90%{
		box-shadow: 0px 0px 5px 13px rgba(173,0,0,0);
	}
}
</style>