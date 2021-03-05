<template>
    <v-app id="inspire">
        <div class="container">
            <div class="container" v-if="this.$vuetify.breakpoint.xs">
                <div class="d-flex">
                <h1 class="jg">🎙️노래방</h1>
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
                    <p class="mb-0">집에서도 노래방을 즐기자!</p>
                    <p class="mb-0">너목들의 노래방 서비스입니다.</p>
                        <br>
                        <div class="d-flex">
                            <p class="mb-0 mr-2"><v-icon color="red" class="mr-1">mdi-record</v-icon></p>
                            <p class="mb-0">RECORD VOICE: </p>
                            <div>
                            <p class="m-0"> Record 버튼을 눌러 노래를 불러보세요!</p>
                            <p class="m-0"> 서버에 전송된 내 목소리로</p>
                            <p class="m-0"> 다양한 추천 서비스를 받아보세요.</p>
                            </div>
                        </div>
                        <v-divider></v-divider>
                        <div class="d-flex">
                            <p class="mr-2"><v-icon small class="mr-1">mdi-playlist-music</v-icon>LIST: </p>
                            <div>
                                <p class="m-0">내가 북마크한 노래들의 목록을 확인할 수 있습니다.</p>
                            </div>
                        </div>
                        <v-divider></v-divider>
                        <div class="d-flex">
                            <p class="mr-2"><v-icon small class="mr-1">mdi-bookmark</v-icon></p>
                            <p class="mb-0">ADD TO MY LIST: </p>
                            <div>
                            <p class="m-0">북마크에 노래를 추가 해,</p>
                            <p class="m-0">나만의 예약목록을 만들어 보세요!</p>
                            </div>
                        </div>
                    </div>
                </span>
                </v-tooltip>
            </div>
                <!-- <div v-if="MR.item.duration_ms=='x'">
                    <h1>노래 선택 안했을 시 기본 소개 페이지 작업중...</h1>
                </div> -->
                <div>
                    <div style="width: 100%;">
                    <vue-plyr ref="plyr">
                        <div class="plyr__video-embed">
                            <!-- :src="`www.youtube.com${MR.item.youtube_mr}`" -->
                            <!-- :src="require(`www.youtube.com${MR.item.youtube_mr}`)" -->
                            <iframe
                            :src="`https://www.youtube.com${MR.item.youtube_mr}`"
                            allowfullscreen allowtransparency allow="autoplay">
                            </iframe>
                        </div>
                    </vue-plyr>
                </div>
                <div class="d-flex mt-2" style="height: 55px;">
                    <div>
                        <img :src="MR.item.album.images[1].url" alt="" style="width: 50px;">
                    </div>
                    <div class="ml-2">
                        <p class="mb-0">{{ MR.item.artists[0].name }}</p>
                        <p class="mb-0">{{ MR.item.name }}</p>
                    </div>
                </div>

                <div>
                    <v-card>
                        <div class="m-2">
                            <v-overlay
                                :absolute="absolute"
                                :value="!isLoggedIn"
                                opacity="0.85"
                                width="200px"
                                style="z-index: 4 !important;"
                            >
                                <div style="text-align: center;">
                                    <p class="mb-1 jg">로그인이 필요한 서비스입니다.</p>
                                    <v-btn style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</v-btn>
                                </div>
                            </v-overlay>
                            <vue-dictaphone @stop="handleRecording($event)" mime-type="audio/webm"
                                v-slot="{ isRecording, startRecording, stopRecording }">
                                <div v-if="!isRecording" @click="startRecording">
                                    <v-btn @click="startRec" width="auto" style="width: 100%; height: 48px;">
                                        <v-icon color="red" class="mr-1">
                                            mdi-record
                                        </v-icon>
                                        RECORD VOICE
                                    </v-btn>
                                </div>
                                <div v-else @click="stopRecording">
                                    <v-btn width="auto" style="width: 100%; height: 48px;">
                                        <RecordKaraoke />
                                    </v-btn>
                                </div>
                            </vue-dictaphone>
                        </div>

                        <div class="m-2">
                            <v-btn @click="showKaraokeList" width="auto" style="width: 100%;">
                                <v-icon class="mr-1">
                                    mdi-playlist-music
                                </v-icon>
                                LIST
                            </v-btn>
                        </div>
                        <div class="m-2">
                            <v-btn @click="addKaraokeList" width="auto" style="width: 100%;">
                                <v-icon class="mr-1">
                                    mdi-bookmark
                                </v-icon>
                                ADD TO MY LIST
                            </v-btn>
                        </div>
                    </v-card>
                </div>

                <v-divider></v-divider>
                    <div style="text-align: center;">
                        <p v-if="!karaokeList" class="m-0 jg">이 노래는 어떠세요?</p>
                        <p v-else class="m-0 jg">내가 부른 노래들</p>
                        <div v-if="arr.length===0">
                            <v-progress-circular
                                indeterminate
                                color="orange"
                                :size="70"
                                style="margin-top: 20%;"
                            ></v-progress-circular>
                        </div>
                        <div v-else class="container p-0" style="height: 200px; overflow: auto;">
                            <div v-if="!karaokeList">
                                <div class="mb-1 pb-0" v-for="(gm, idx) in arr" :key="idx">
                                    <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                                        <img :src="gm.album.images[1].url" alt="" @click="playMusic_(gm)" style="width: 40px; height: 40px;">
                                        <div class="mr-2" style="width: 50%; color: white; text-align: left;">
                                            <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                                            <p class="m-0 ml-2" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                                        </div>
                                        <div class="">
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
                            <div v-else>
                                <div v-if="karaokeListArr.length===0">
                                    <v-progress-circular
                                        indeterminate
                                        color="orange"
                                        :size="70"
                                        style="margin-top: 20%;"
                                    ></v-progress-circular>
                                </div>
                                <div v-else>
                                <div class="mb-1 pb-0" v-for="(list, idx) in this.karaokeListArr" :key="idx">
                                    <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                                        <img :src="list.album.images[1].url" alt="" @click="playMusic_(list)" style="width: 40px; height: 40px;">
                                        <div class="mr-2" style="width: 50%; color: white; text-align: left;">
                                            <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ list.album.artists[0].name }}</p>
                                            <p class="m-0 ml-2" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ list.name }}</p>
                                        </div>
                                        <div class="d-flex">
                                        <v-btn icon>
                                            <v-icon v-if="list.youtube_mr" @click="getMR(list)" color="#FFB74D">
                                                mdi-microphone-variant
                                            </v-icon>
                                            <v-icon v-else disabled color="#FFB74D">
                                                mdi-microphone-variant
                                            </v-icon>
                                        </v-btn>
                                        <v-btn icon>
                                            <v-icon @click="deleteList(list)">
                                                mdi-delete
                                            </v-icon>
                                        </v-btn>
                                    </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <v-overlay
                        :absolute="absolute"
                        opacity="0.85"
                        z-index=0
                        :value="overlay"
                        v-if="MR.item.duration_ms=='x'"
                        color="#171727"
                        >
                        <div class="container jg" style="text-align: center; border-radius: 1em;">
                            <h4>쉽고 간편하게 </h4>
                                
                            <h4>노래방 서비스를 이용해 보세요!</h4>
                            <h5>
                                플레이어 속
                                <v-icon x-large color="#FFB74D">mdi-microphone-variant</v-icon>
                                버튼을 눌러</h5> <h5>노래방 서비스 이용이 가능합니다.
                            </h5>
                            <v-divider></v-divider>
                            <button class="btn jg" style="background-color: orange; color: white; border: 1px solid orange;" @click="gotoHome">노래 검색하러 가기</button>
                        </div>
                        
                    </v-overlay>
                </div>
            </div>



            <div v-else>
                <div class="d-flex">
                    <h1 class="jg">🎙️노래방</h1>
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
                        <p>집에서도 노래방을 즐기자! 너목들의 노래방 서비스입니다.</p>
                        <br>
                        <div class="d-flex">
                            <p class="mr-2"><v-icon color="red" class="mr-1">mdi-record</v-icon>RECORD VOICE: </p>
                            <div>
                            <p class="m-0"> Record 버튼을 눌러 노래를 불러보세요!</p>
                            <p class="m-0"> 서버에 전송된 내 목소리로</p>
                            <p class="m-0"> 다양한 추천 서비스를 받아보세요.</p>
                            </div>
                        </div>
                        <v-divider></v-divider>
                        <div class="d-flex">
                            <p class="mr-2"><v-icon small class="mr-1">mdi-playlist-music</v-icon>LIST: </p>
                            <div>
                                <p class="m-0">내가 북마크한 노래들의 목록을 확인할 수 있습니다.</p>
                            </div>
                        </div>
                        <v-divider></v-divider>
                        <div class="d-flex">
                            <p class="mr-2"><v-icon small class="mr-1">mdi-bookmark</v-icon>ADD TO MY LIST: </p>
                            <div>
                            <p class="m-0">북마크에 노래를 추가 해,</p>
                            <p class="m-0">나만의 예약목록을 만들어 보세요!</p>
                            </div>
                        </div>
                        </div>
                    </span>
                    </v-tooltip>
                </div>
<!--                 
                <div v-if="MR.item.duration_ms=='x'">
                    <h1>노래 선택 안했을 시 기본 소개 페이지 작업중...</h1>
                </div> -->
            
                <div class="container d-flex">

                    <div style="width: 75%; text-align: center; margin: auto 0;">
                        <vue-plyr ref="plyr">
                        <div class="plyr__video-embed">
                            <iframe
                            :src="`https://www.youtube.com${MR.item.youtube_mr}`"
                            allowfullscreen allowtransparency allow="autoplay">
                            </iframe>
                        </div>
                        </vue-plyr>
                    </div>
                    <div class="ml-4" style="width: 300px;">
                        <div>
                            <div class="d-flex mb-2 mt-2">
                                <div>
                                    <img :src="MR.item.album.images[1].url" alt="" style="width: 60px;">
                                </div>
                                <div class="ml-2">
                                    <p class="mb-0" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ MR.item.artists[0].name }}</p>
                                    <p class="mb-0" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ MR.item.name }}</p>
                                </div>
                            </div>
                        </div>
                        <div>
                            <v-card>
                                <div class="m-2">
                                
                                    <v-overlay
                                        :absolute="absolute"
                                        :value="!isLoggedIn"
                                        opacity="0.85"
                                        width="200px"
                                    >
                                        <div style="text-align: center;">
                                            <p class="mb-1 jg">로그인이 필요한 서비스입니다.</p>
                                            <v-btn style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</v-btn>
                                        </div>
                                    </v-overlay>
                                    <vue-dictaphone @stop="handleRecording($event)" mime-type="audio/webm"
                                        v-slot="{ isRecording, startRecording, stopRecording }">
                                        <div v-if="!isRecording" @click="startRecording">
                                            <v-btn @click="startRec" width="auto" style="width: 100%; height: 48px;">
                                                <v-icon color="red" class="mr-1">
                                                    mdi-record
                                                </v-icon>
                                                RECORD VOICE
                                            </v-btn>
                                        </div>
                                        <div v-else @click="stopRecording" class="mt-6">
                                            <v-btn width="auto" style="width: 100%; height: 48px;">
                                                <RecordKaraoke />
                                            </v-btn>
                                        </div>
                                    </vue-dictaphone>
                                </div>
                                <div class="m-2">
                                    <v-btn @click="showKaraokeList" width="auto" style="width: 100%;">
                                        <v-icon class="mr-1">
                                            mdi-playlist-music
                                        </v-icon>
                                        LIST
                                    </v-btn>
                                </div>
                                <div class="m-2">
                                    <v-btn @click="addKaraokeList" width="auto" style="width: 100%;">
                                        <v-icon class="mr-1">
                                            mdi-bookmark
                                        </v-icon>
                                        ADD TO MY LIST
                                    </v-btn>
                                </div>
                            </v-card>
                        </div>
                        

                        <v-divider></v-divider>
                        <div style="text-align: center;">
                            <p v-if="!karaokeList" class="m-0 jg">이 노래는 어떠세요?</p>
                            <p v-else class="m-0 jg">내가 부른 노래들</p>
                            <div v-if="arr.length===0">
                                <v-progress-circular
                                    indeterminate
                                    color="orange"
                                    :size="70"
                                    style="margin-top: 20%;"
                                ></v-progress-circular>
                            </div>
                            <div v-else class="container p-3" style="height: 200px; overflow: auto;">
                                <div v-if="!karaokeList">
                                    <div class="mb-1 pb-0" v-for="(gm, idx) in arr" :key="idx">
                                        <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                                            <img :src="gm.album.images[1].url" alt="" @click="playMusic_(gm)" style="width: 40px; height: 40px;">
                                            <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                                                <p class="m-0 ml-2" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                                                <p class="m-0 ml-2" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                                            </div>
                                            <div class="d-flex">
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

                                <div v-else>
                                    <div v-if="karaokeListArr.length===0">
                                        <v-progress-circular
                                            indeterminate
                                            color="orange"
                                            :size="70"
                                            style="margin-top: 20%;"
                                        ></v-progress-circular>
                                    </div>
                                    <div v-else>
                                    <div class="mb-1 pb-0" v-for="(list, idx) in this.karaokeListArr" :key="idx">
                                        <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                                            <img :src="list.album.images[1].url" alt="" @click="playMusic_(list)" style="width: 40px; height: 40px;">
                                            <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                                                <p class="m-0 ml-2" style="font-size: 14px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ list.album.artists[0].name }}</p>
                                                <p class="m-0 ml-2" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ list.name }}</p>
                                            </div>
                                            <div class="d-flex">
                                                <v-btn icon>
                                                    <v-icon v-if="list.youtube_mr" @click="getMR(list)" color="#FFB74D">
                                                        mdi-microphone-variant
                                                    </v-icon>
                                                    <v-icon v-else disabled color="#FFB74D">
                                                        mdi-microphone-variant
                                                    </v-icon>
                                                </v-btn>
                                                <v-btn icon>
                                                    <v-icon @click="deleteList(list)">
                                                        mdi-delete
                                                    </v-icon>
                                                </v-btn>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <v-overlay
                        :absolute="absolute"
                        opacity="0.85"
                        :value="overlay"
                        v-if="MR.item.duration_ms=='x'"
                        color="#171727"
                        >
                        <div class="container jg" style="text-align: center; border-radius: 1em;">
                            <h3>
                                쉽고 간편하게 노래방 서비스를 이용해 보세요!
                            </h3>
                            <h5>
                                플레이어 속
                                <v-icon x-large color="#FFB74D">mdi-microphone-variant</v-icon>
                                버튼을 눌러 노래방 서비스 이용이 가능합니다.
                            </h5>
                            <v-divider></v-divider>
                            <button class="btn jg" style="background-color: orange; color: white; border: 1px solid orange;" @click="gotoHome">노래 검색하러 가기</button>
                        </div>
                        
                    </v-overlay>
                </div>
            </div>
        </div>
    </v-app>
</template>

<script>
import RecordKaraoke from '../components/RecordKaraoke'
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'
import swal from 'sweetalert';
import LoginModal from '../components/LoginModal.vue'
const SERVER_URL = "http://localhost:8000/api/"

export default {
    name: 'Karaoke',
    data() {
        return{
            recommend: ['1'],
            arr: [],
            karaokeListArr: [],
            page_0: 0,
            start_Rec: false,
            karaokeList: false,
            absolute: true,
            overlay: true,
        }
    },
    computed: {
        ...mapGetters('accounts', ['isLoggedIn', 'userInfo']),
        ...mapGetters('karaoke', ["MR"]),

        breakpoint () {
        return this.$vuetify.breakpoint
        },
        player() {
            return this.$refs.plyr.player
        },
    },
    created() {
        this.getTrack_Genre()
        // console.log("!#", this.MR.item.youtube_mr)
        // console.log('ususu', this.userInfo)
    },
    components: {
        RecordKaraoke
    },
    methods: {
        ...mapActions('player', ['playMusic']),
        ...mapActions('karaoke', ['playMR']),
        ...mapActions('accounts', ['getUserInfo']),
        
        gotoHome() {
            this.$router.push('/')
        },
        startRec() {
            this.start_Rec = !this.start_Rec
        },
        getTrack_Genre () {
            // console.log('MR', this.MR)
            axios.get(SERVER_URL+'music/tracks/cluster/1/' + this.MR.item.cluster + '/')
                .then(res => {
                this.arr = [...this.arr, ...res.data.data]

                for (var i = 0; i < this.arr.length ; i++) {
                    if (this.arr[i].youtube_mr === null) {
                        this.arr.splice(i, i)
                    }
                }
                
                })
                .catch(err => console.error(err))
        },

        getMR(gm) {
            this.playMR(gm)
        },

        playMusic_(item){
            // console.log('playmusic at', item)
            this.playMusic(item)
        },
        
        handleRecording({ blob, src }) {

            // console.log('blob!: ', blob)
            console.log('src!: ', src)

            let formData = new FormData();
            // console.log(this.blobFile)
            // console.log('select rec', this.userInfo)
            formData.append('file', blob, 'recording'+ this.userInfo.userid +new Date().getTime()+'.webm');
            
            formData.append('userid', this.userInfo.userid)
            axios.post( SERVER_URL + 'accounts/get_pitch/', 
                      formData,
                      {
                      headers: {
                          'Content-Type': 'multipart/form-data'
                      }
                    }
                  ).then(function(){
                // console.log('SUCCESS!!');
                swal("분석이 완료되었습니다", {
                            icon: "success",
                        })
              })
              .catch(function(){
                console.log('FAILURE!!');
              });
        
        },
        showKaraokeList: async function(){
            this.karaokeList = !this.karaokeList

            if (this.karaokeList === true) {

                await this.$store.dispatch("accounts/getUserInfo", {
                    userid: localStorage.getItem('userid')
                })
                
                this.karaokeListArr = []

                for (var i=0; i < this.userInfo.sang_songs.length; i++) {

                    axios.get(SERVER_URL + 'music/track/' + this.userInfo.sang_songs[i].songid + '/')
                        .then( res => {
                            this.karaokeListArr.push(res.data.data)
                        })
                }
            }
        },
        addKaraokeList() {
            console.log(this.MR, '!')
            console.log(this.MR.item.id, this.userInfo.userid)
            axios.post(SERVER_URL + 'accounts/add_sang_song/',
                {
                    'userid': this.userInfo.userid,
                    'sang_songs': [{'songid': this.MR.item.id}]
                }
            )
            .then(function(){
                // console.log('SUCCESS!!');
                
                swal("your request is approved", {
                            icon: "success",
                        })
            })
            .catch(function(){
                console.log('FAILURE!!');
            });
        },
        
        deleteList(song) {
            // console.log(song)

            axios.post(SERVER_URL + 'accounts/delete_sang_song/', {
                'userid': this.userInfo.userid,
                'songid': song.id
            }).then( function(){
                swal("your request is approved", {
                        icon: "success",
                    })
                console.log('SUCCESS!!');}
                ).catch(function(){
                console.log('FAILURE!!');
            })

            this.karaokeList = !this.karaokeList
            // console.log(this.karaokeList)
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
            
    },
    watch: {
        MR() {
            // console.log(this.player)
            // console.log(this.MR, '!!!')
            this.player.source = {
                type: 'video',
                sources: [
                    {
                    src: this.MR.item.youtube_mr,
                    provider: 'youtube',
                    },
                ],
            }
        },
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

.plyr--video {
    z-index: 0;
}

.v-sheet.v-card {
    z-index: 0;
}
</style>