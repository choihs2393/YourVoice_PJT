<template>
  <v-container
    class="pt-0 mb-8 pb-6 pb-sm-12"
  >
    <!-- mobile screen -->

    <div v-if="breakpoint.xs">
    
    <v-tabs
      show-arrows
      color="white"
      center-active
      v-model="tmp"
      background-color="#121212"
    >

      <v-tab class="jg">HOT</v-tab>
      <v-tab class="jg">CHEERFUL</v-tab>
      <v-tab class="jg">ACOUSTIC</v-tab>
      <v-tab class="jg">ELECTRO HOUSE</v-tab>
      <v-tab class="jg">DREAMY</v-tab>
      <v-tab class="jg">DANCE</v-tab>

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='arr.length === 0' 
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in arr" :key="idx">
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
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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
        <!-- <div>
      <v-btn @click="getTrack_Hot">button</v-btn>
    </div> -->
      </v-tab-item>

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='rock_track.length === 0' 
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in rock_track" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="gm.album.images[1].url" alt="" class="mb-2" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon>
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='bal_track.length === 0'
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in bal_track" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="gm.album.images[1].url" alt="" class="mb-2" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon>
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='hh_track.length === 0'
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in hh_track" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="gm.album.images[1].url" alt="" class="mb-2" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon>
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='dance_track.length === 0'
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in dance_track" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="gm.album.images[1].url" alt="" class="mb-2" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>

                    <div class="mt-2">
                      <v-btn icon>
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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

      <v-tab-item>
        <v-progress-circular
          indeterminate
          color="orange"
          :size="70"
          v-if='tmp_track.length === 0' 
          style="margin-left: 40%; margin-top: 45%;"
        ></v-progress-circular>
        <div class="row jg" v-else style="overflow: auto;">
            <div class="col-xs-12 col-sm-6 col-md-3 pb-0" v-for="(gm, idx) in tmp_track" :key="idx">
                <div class="btn d-flex justify-content-between" style="border: 1px solid grey; width: 100%;">
                    <!-- <img src="" alt="" style="width: 50px; border: 1px solid black;"> -->
                    <img :src="gm.album.images[1].url" alt="" class="mb-2" @click="playMusic_(gm)" style="width: 50px; height: 50px;">
                    <!-- <img src="../assets/logo.png" alt="" style="width: 50px; border: 1px solid black;"> -->
                    
                    <div class="mr-2" style="width: 40%; color: white; text-align: left;">
                        <p class="m-0 ml-2" style="overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.album.artists[0].name }}</p>
                        <p class="m-0 ml-2" style="font-size: 15px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
                    </div>
                    <div class="mt-2">
                      <v-btn icon>
                        <v-icon v-if="gm.preview_url" @click="playMusic_(gm)" color="white">
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

    </v-tabs><!-- mobile screen -->
    <div id="bottomSensor"></div>
    </div>

    <div v-else>

    <!-- desktop and large screen -->
    <v-row class="ma-4">
      <v-progress-circular
        indeterminate
        color="orange"
        :size="100"
        v-if="arr.length === 0"
        :width="7"
        style="margin-top: 20%; margin-left: 45%"
      ></v-progress-circular>
        <v-col
        v-else
        cols="12"
        class="pa-0 ma-0"
      >
      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">인기 차트</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(0)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
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
            class="ma-3 jg"
            @click="toggle"
            height="180"
            width="140"
          >
            <v-img lazy-src="../assets/default_cover.png" :src="gm.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
            <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.album.artists[0].name }}</p>
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      <v-divider></v-divider>

      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">밝고 경쾌한 음악</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(1)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
         <v-slide-group
        class="pa-4"
        active-class="secondary"
        show-arrows
      >
        <v-slide-item
          v-for="gm in rock_track"
          :key="gm.id"
          v-slot:default="{ active, toggle }"
        >
          <v-card
            :color="active ? undefined : 'transparent lighten-1'"
            class="ma-3 jg"
            @click="toggle"
            height="180"
            width="140"
          >
            <v-img lazy-src="../assets/default_cover.png" :src="gm.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
            <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.album.artists[0].name }}</p>
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      <v-divider></v-divider>

      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">어쿠스틱</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(2)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
         <v-slide-group
        class="pa-4"
        active-class="secondary"
        show-arrows
      >
        <v-slide-item
          v-for="gm in bal_track"
          :key="gm.id"
          v-slot:default="{ active, toggle }"
        >
          <v-card
            :color="active ? undefined : 'transparent lighten-1'"
            class="ma-3 jg"
            @click="toggle"
            height="180"
            width="140"
          >
            <v-img lazy-src="../assets/default_cover.png" :src="gm.album.images[1].url" alt="musicPic" @click="playMusic_(gm)" style="width: 140px;"></v-img>
            <p class="m-0" style="font-size: 12px; text-align: left;">{{ gm.album.artists[0].name }}</p>
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      <v-divider></v-divider>

      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">일렉트로 하우스</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(3)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
         <v-slide-group
        class="pa-4 jg"
        active-class="secondary"
        show-arrows
      >
        <v-slide-item
          v-for="gm in hh_track"
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
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      <v-divider></v-divider>

      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">몽환적인 노래</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(4)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
         <v-slide-group
        class="pa-4 jg"
        active-class="secondary"
        show-arrows
      >
        <v-slide-item
          v-for="gm in dance_track"
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
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      <v-divider></v-divider>

      <div class="d-flex mr-10 justify-content-between">
        <h3 class="jg">잔잔한 댄스</h3>
        <p class='mb-0 mt-2 mr-10' @click="GenreDetailModal(5)" style="cursor: pointer;">
          more
          <v-icon x-small>
            mdi-plus
          </v-icon>
        </p>
      </div>
         <v-slide-group
        class="pa-4 jg"
        active-class="secondary"
        show-arrows
      >
        <v-slide-item
          v-for="gm in tmp_track"
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
            <p class="m-0" style="font-size: 12px; text-align: left; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">{{ gm.name }}</p>
          
          </v-card>
        </v-slide-item>
      </v-slide-group>

      </v-col>
    </v-row><!-- desktop and large screen -->
    </div>
    <!-- <modals-container /> -->
  </v-container>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/scrollmonitor/1.2.0/scrollMonitor.js"></script>
<script>
import { mapActions } from 'vuex'
import axios from 'axios'
import GenreDetailModal from '../components/GenreDetailModal'

const SERVER_URL = "http://localhost:8000/api/"

export default {
  name: 'Home',

  created() {
    this.getTrack_Hot()
    this.getTrack_Rock()
    this.getTrack_Ballad()
    this.getTrack_Hiphop()
    this.getTrack_Dance ()
    this.getTrack_Tmp ()
  },

  data() {
    return {
      arr: [],
      rock_track: [],
      bal_track: [],
      hh_track: [],
      dance_track: [],
      tmp_track: [],
      page_t: 0,
      page_0: 0,
      page_1: 0,
      page_2: 0,
      page_3: 0,
      page_4: 0,
      urls: "www.youtube.com",
      selectmusics: [],
      tmp: null,
    }
  },

  computed: {
    breakpoint () {
    return this.$vuetify.breakpoint
    }
  },

  watch: {
    // tmp() {
    //   if (this.tmp != 0){
    //     this.rock_track = []
    //     this.bal_track = []
    //     this.hh_track = []
    //     this.dance_track = []
    //     this.tmp_track = []
        
    //     this.page_1 = 0
    //     this.page_2 = 0
    //     this.page_3 = 0
    //     this.page_4 = 0
    //     this.page_t = 0
    //   }
    // }
  },

  methods: {
    ...mapActions('player', ['playMusic']),
    ...mapActions('karaoke', ['playMR']),

    getMV(youtube_urls) {
        window.open('https://'+this.urls + youtube_urls, "_blank")
    },

    playMusic_(item){
      // console.log('playmusic at', item)
      this.playMusic(item)
    },
    
    getMR(gm) {
      // console.log(gm)
      this.playMR(gm)
      this.$router.push("/karaoke")
    },

    getTrack_Hot: function () {

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

    getTrack_Tmp: function () {

      const _page = this.page_t++
      // console.log(_page)

      axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/0/')
        .then(res => {
          this.tmp_track = [...this.tmp_track, ...res.data.data]
          // console.log(this.tmp_track)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    getTrack_Rock: function () {

      const _page = this.page_1++
      // console.log(_page)

      axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/1/')
        .then(res => {
          this.rock_track = [...this.rock_track, ...res.data.data]
          // console.log(this.rock_track)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    getTrack_Ballad: function () {

      const _page = this.page_2++
      // console.log(_page)

      axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/3/')
        .then(res => {
          this.bal_track = [...this.bal_track, ...res.data.data]
          // console.log(this.bal_track)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    getTrack_Hiphop: function () {

      const _page = this.page_3++
      // console.log(_page)

      axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/4/')
        .then(res => {
          this.hh_track = [...this.hh_track, ...res.data.data]
          // console.log(this.hh_track)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    getTrack_Dance: function () {

      const _page = this.page_4++
      // console.log(_page)

      axios.get(SERVER_URL+'music/tracks/cluster/' +  _page + '/2/')
        .then(res => {
          this.dance_track = [...this.dance_track, ...res.data.data]
          // console.log(this.dance_track)
          // console.log(_page)              
        })
        .catch(err => console.error(err))
    },

    addScrollWatcher: function () {
      const bottomSensor = document.querySelector('#bottomSensor')
      const watcher = scrollMonitor.create(bottomSensor)

      if (this.tmp == 0) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Hot()
        }, 30)
      })
      } else if (this.tmp == 1) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Rock()
        }, 30)
      })
      } else if (this.tmp == 2) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Ballad()
        }, 30)
      })
      } else if (this.tmp == 3) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Hiphop()
        }, 30)
      })
      } else if (this.tmp == 4) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Dance()
        }, 30)
      })
      } else if (this.tmp == 5) {
        watcher.enterViewport(() => {
        setTimeout(() => {
          this.getTrack_Tmp()
        }, 30)
      })
      }
    },
    
    loadUntilViewportIsFull: function () {
      const bottomSensor = document.querySelector('#bottomSensor')
      const watcher = scrollMonitor.create(bottomSensor)
      if (watcher.isFullyInViewport) {
        if (this.tmp == 0) {
          this.getTrack_Hot()
        } else if (this.tmp == 1) {
          this.getTrack_Rock()
        } else if (this.tmp == 2) {
          this.getTrack_Ballad()
        } else if (this.tmp == 3) {
          this.getTrack_Hiphop()
        } else if (this.tmp == 4) {
          this.getTrack_Dance ()
        } else if (this.tmp == 5) {
          this.getTrack_Tmp ()
        }
      }
    },
    
    GenreDetailModal(num) {
      this.$modal.show(GenreDetailModal, {
        genre: num,
        modal: this.$modal},{
            scrollable: true,
            width: "600px",
            height: "auto"
      })
    }
  },

  mounted() {
    if (this.$vuetify.breakpoint.xs) {
      this.addScrollWatcher()
    }
  },
      
  updated() {
    if (this.$vuetify.breakpoint.xs) {
      this.loadUntilViewportIsFull()
    }
  },
}
</script>

<style>
.v-window-item {
  background-color: #121212;
  color: #121212;
}
.v-progress-circular {
  margin: 1rem;
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

  @-webkit-keyframes spin {
      0% { -webkit-transform: rotate(0deg); }
      100% { -webkit-transform: rotate(360deg); }
  }

  @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
  }
</style>
