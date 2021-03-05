<template>
  <div>
     <v-footer
        v-if="!this.$vuetify.breakpoint.xs"
        :style="!this.$vuetify.breakpoint.xs  && 'z-index: 10'"
        fixed
        color="#4E4942"
        style="opacity: 0.9;"
    >
          <div class="d-flex justify-content-between jg" style="width: 100%; height: 85px;">
              <div class="d-flex" style="">
                  <img class="ml-4" :src="MUSICDATA.item.album.images[1].url" alt="" style="width: 90px;">
                    <div class="px-3 mt-4 ml-2">
                        <div class="text-m text-white front-semibold m-0" style="width: 300px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">
                            {{ MUSICDATA.item.name }}
                        </div>
                        <p class="text-sm text-white opacity-75">
                            {{ MUSICDATA.item.album.artists[0].name }}
                        </p>
                    </div>
              </div>
              
              <!-- <div class="d-flex mt-4 ml-10 mr-10">
                    <v-item v-slot:default="{ active }">
                        <v-btn icon>
                            <v-icon>
                                {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                            </v-icon>
                        </v-btn>
                    </v-item>
              </div> -->

              <div class="mt-7 mr-2" style="width: 70%;">
                <vue-plyr ref="plyr">
                    <audio>
                        <source :src="MUSICDATA.item.preview_url" type="audio/mp3"/>
                    </audio>
                </vue-plyr>
              </div>

              <div class="d-flex mt-4 ml-10 mr-10">
                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                            icon
                            v-bind="attrs"
                            v-on="on"
                            @click="getMV(MUSICDATA.item.youtube_urls)"
                            x-large
                        >
                            <v-icon color="red">
                            mdi-youtube
                            </v-icon>
                        </v-btn>
                    </template>
                    <span>Music Video</span>
                </v-tooltip>
                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                            icon
                            v-bind="attrs"
                            v-on="on"
                            class="mr-2"
                            x-large
                        >
                            <v-icon v-if="MUSICDATA.item.youtube_mr" @click="getMR(MUSICDATA.item)" color="#FFB74D">
                                mdi-microphone-variant
                            </v-icon>
                            <v-icon v-else disabled color="#FFB74D">
                                mdi-microphone-variant
                            </v-icon>
                        </v-btn>
                    </template>
                    <span>Karaoke</span>
                </v-tooltip>
                </div>
          </div>
     </v-footer>
     
     <v-footer 
        v-else 
        fixed 
        class="player-mobile" 
        :style="this.$vuetify.breakpoint.xs  && 'z-index: 0'"
        color="#4E4942"
        style="opacity: 0.9;"
    >
         <div class="d-flex" style="margin: 0 auto; height: 60px;">
            <div>
                <img :src="MUSICDATA.item.album.images[1].url" alt="" style="width: 60px; height: 60px;">
            </div>
            <div class="ml-2">
            <div class="px-3 mr-3 jg">
                <p class="text-m text-white front-semibold m-0" style="font-size: 12px; overflow: hidden; text-overflow:ellipsis; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical;">
                    {{ MUSICDATA.item.name }}
                </p>
                <p class="text-sm text-white opacity-75 m-0" style="font-size: 12px; display: block; overflow: hidden; text-overflow:ellipsis;">
                    {{ MUSICDATA.item.album.artists[0].name }}
                </p>
            </div>
              <div style="align: right;">
                <vue-plyr ref="plyr">
                    <audio>
                        <source :src="MUSICDATA.item.preview_url" type="audio/mp3"/>
                    </audio>
                </vue-plyr>
              </div>
            </div>
         </div>
     </v-footer>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    // props: {
    //     musicdata: Object,
    // },
    computed: {
        ...mapGetters('player', ["MUSICDATA"]),
        
        player() {
            return this.$refs.plyr.player
        },
        breakpointXs () {
            return this.$vuetify.breakpoint.xs
        },
    },
    data() {
        return{
            // musicdata: this.MUSICDATA
            urls: "www.youtube.com"
        }
    },
    mounted() {

    },
    methods: {
        ...mapActions('karaoke', ['playMR']),

        getMV(youtube_urls) {
            window.open('https://'+this.urls + youtube_urls, "_blank")
        },
        
        getMR(gm) {
            // console.log(gm)
            this.playMR(gm)
            this.$router.push("/karaoke")
        },
    },
    watch: {
        MUSICDATA() {
            // console.log(this.player)
            // console.log(this.MUSICDATA, '!!!')
            this.player.source = {
                type: 'audio',
                sources: [
                    {
                    src: this.MUSICDATA.item.preview_url,
                    type: 'audio/mp3',
                    },
                ],
            };
        }
    }
}
</script>

<style>
    .plyr__controls {
        color: #ffffff !important;
        background: none !important;
        padding: 0 !important;
    }
    .player-mobile{
        transform: translateY(-56px);
    }
    .plyr--full-ui input[type=range] {
        color: darkorange !important;
    }
</style>