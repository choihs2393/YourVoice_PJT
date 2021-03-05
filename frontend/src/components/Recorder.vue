<template>
  <v-app id="inspire">
    <div v-if="breakpoint.xs" style="background-color: #272727;">
        <audio ref="player"></audio>
        <av-media :canv-width="200" type="frequ" :media="media" line-color="darkorange"/>
    </div>
    <div v-else style="background-color: #272727;">
        <audio ref="player"></audio>
        <av-media type="frequ" :media="media" line-color="darkorange"/>
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

</style>