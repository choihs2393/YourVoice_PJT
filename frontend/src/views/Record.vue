<template>
  <v-app id="inspire">
      <div class="container" style="background-color: #272727;">
          <div class="container" style="text-align: center; height: 100%;">
            <div v-if="!audioSource">
                <vue-dictaphone @stop="handleRecording($event)" mime-type="audio/webm"
                        v-slot="{ isRecording, startRecording, stopRecording }">
            
                <button class="button_rec notRec" id="recButton" v-if="!isRecording" @click="startRecording">
                    <v-icon color="white" @click="changecol">
                        mdi-microphone
                    </v-icon>
                </button>
                
                <button v-else class="button_rec notRec" id="recButton" @click="stopRecording">
                    <v-icon color="white" @click="changecol">
                    mdi-microphone
                    </v-icon>
                </button>

                <p v-if="!recopen">Press the button to record your voice</p>
                
                </vue-dictaphone>

                <div v-if="recopen" style="background-color: #272727;">
                    <Recorder style="background-color: #272727;" />
                </div>
            </div>

            <div v-else>
                <RecordPlayer :audioSource="audioSource" style="background-color: #272727;"/>
                <div class="d-flex justify-content-center mb-2">
                    <v-btn icon class="m-1 mr-4" @click="reRec">
                        <v-icon large color="red" style="font-size: 40px; margin-top: 4px;">
                            mdi-refresh
                        </v-icon>
                    </v-btn>
                    <div class="mt-3">Restart Record</div>
                </div>
                <div class="d-flex justify-content-center">
                    <v-btn icon class="m-1 mr-4" @click="selectRec">
                        <v-icon large color="green">
                            mdi-check-circle-outline
                        </v-icon>
                    </v-btn>
                    <div class="mt-2">Select Record</div>
                    <!-- <div class="mt-2" @click="thanks">옆에 초록색 버튼 누르시고 이 글씨를 눌러주세요</div> -->
                </div>
            </div>

        </div>
      </div>
  </v-app>
</template>

<script>
import Recorder from '../components/Recorder'
import RecordPlayer from '../components/RecordPlayer'
import { mapGetters } from 'vuex'

import $ from 'jquery'
import axios from 'axios'
import swal from 'sweetalert';

const SERVER_URL = "http://localhost:8000/api/"
// console.log(axios, SERVER_URL)

export default {
    components: {
        Recorder,
        RecordPlayer
    },
    // created() {
        // console.log('select rec', this.userInfo)
    // },
    data() {
        return{
            audioSource: null,
            soundfile: [],
            recopen: false,
            file: '',
            mtype: null,
            media: null,
            blobFile: null,
        }
    },
    computed: {
        ...mapGetters('accounts', ["userInfo"]),
        breakpoint () {
        return this.$vuetify.breakpoint
        },
        player() {
            return this.$refs.plyr.player
        },
    },
    mounted () {
        // console.log(this.$refs.player)
        // console.log('user', this.userInfo)
        const audio = this.$refs.player
        const constraints = {
        audio: true,
        video: false
        }
        // console.log('audio:', audio)
        navigator.mediaDevices.getUserMedia(constraints)
        .then(media => {
            this.media = media
            audio.srcObject = media
        })
    },
    methods: {
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
        handleRecording({ blob, src }) {
        this.audioSource = src;
        this.blobFile = blob;

        // console.log('blob!: ', blob)
        // console.log('src!: ', src)
        this.soundfile.push(blob)
        
        let formData = new FormData();
        formData.append('file', blob, 'recording'+new Date().getTime()+'.webm');
        // formData.append('first_name', 'ss');
        // formData.append('last_name', 's');
        formData.append('userid', 'test')
        //   axios.post( SERVER_URL + 'accounts/get_pitch/', 
        //           formData,
        //           {
        //           headers: {
        //               'Content-Type': 'multipart/form-data'
        //           }
        //         }
        //       ).then(function(){
        //     console.log('SUCCESS!!');
        //   })
        //   .catch(function(){
        //     console.log('FAILURE!!');
        //   });
        },
        reRec() {
            this.audioSource = null
            this.blobFile = null
        },
        selectRec() {
            let formData = new FormData();
            // console.log(this.blobFile)
            // console.log('select rec', this.userInfo)
            formData.append('file', this.blobFile, 'recording'+ this.userInfo.userid +new Date().getTime()+'.webm');
            
            // formData.append('first_name', 'ss');
            // formData.append('last_name', 's');
            formData.append('userid', this.userInfo.userid)
            axios.post( SERVER_URL + 'accounts/get_pitch/', 
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
        thanks() {
            this.$router.push('/thanks')
        }
    }
}
</script>

<style scoped>
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