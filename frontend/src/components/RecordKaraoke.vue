<template>
  <v-app id="inspire" style="background: transparent;">
      <div class="mt-1">
        <audio ref="player"></audio>
        <av-media :canv-width="240" :line-width="0.8" :canv-height="40" type="frequ" :media="media" line-color="darkorange"/>
      </div>
  </v-app>
</template>

<script>
export default {
    data() {
        return{
            mtype: null,
            media: null
        }
    },
    computed: {
        breakpoint () {
        return this.$vuetify.breakpoint
        }
    },
    mounted () {
        // console.log(this.$refs.player)
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
}
</script>

<style>
.v-application--wrap {
    min-height: 0px;
}
</style>