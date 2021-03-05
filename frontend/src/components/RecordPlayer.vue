<template>
  <v-app id="inspire">
    <div v-if="breakpoint.xs" class="mobile-rec">
      <av-waveform
        :audio-src="audioSource"
        played-line-color="#fd7e14"
        noplayed-line-color="white"
        :played-line-width="1"
        :noplayed-line-width="1"
        playtime-slider-color="white"
        :canv-width="300"
      ></av-waveform>
    </div>
    <div v-else>
      <av-waveform
        :audio-src="audioSource"
        played-line-color="#fd7e14"
        noplayed-line-color="white"
        :played-line-width="1"
        :noplayed-line-width="1"
        playtime-slider-color="white"
        :canv-width="300"
      ></av-waveform>
    </div>
  </v-app>
</template>

<script scoped>
export default {
    props: {
        audioSource: String,
    },
    computed: {
        breakpoint () {
        return this.$vuetify.breakpoint
        }
    },
}
</script>

<style>
.v-application--wrap {
    min-height: 100px !important;
}

.mobile-rec audio {
  width: 100% !important;
}

.mobile-rec canvas {
  width: 200px !important;
}
</style>