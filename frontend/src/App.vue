<template>
  <v-app id="inspire" class="app">
    <link src="@/assets/favicon.ico"/>
      <!-- app drawer -->
    <v-navigation-drawer
      v-model="appDrawer"
      app
      clipped
    >
      <AppDrawer />
    </v-navigation-drawer><!-- app drawer -->

    <!-- app navbar -->
    <AppNavbar
      @toggleAppDrawer="toggleAppDrawer"
    /><!-- app navbar -->

    <!-- main section -->
    <v-main style="margin-bottom: 60px">
      <v-scroll-x-transition mode="out-in"><!-- transitions -->

          <!-- router -->
          <router-view
            style=""
            :key="$route.fullPath"
          ></router-view> <!-- define key to fullpath of router makes router refresh whenever address changes -->

      </v-scroll-x-transition>
    </v-main><!-- main section -->

    <!-- bottom player -->
    <Player
      :layout="layout"
      @toggleLayout="toggleLayout"
      :tab="tab"
      @switchTab="switchTab"
    />

    <BottomNav
      :layout="layout"
      @disableLayout="disableLayout"
    />
  </v-app>
</template>

<script>
// import { mapGetters } from 'vuex'
import AppDrawer from './components/AppDrawer'
import AppNavbar from './components/AppNavbar'
import BottomNav from './components/BottomNav'
import Player from './components/Player'

export default {
  components: {
    AppNavbar,
    AppDrawer,
    BottomNav,
    Player,
  },
  data () {
    return {
      appDrawer: false,
      layout: false,
      tab: 0,
      musicdata: null,
    }
  },
  computed: {
    // ...mapGetters(["MUSICDATA"]),
  },
  created () {
    // console.log(this.MUSICDATA)
    this.$vuetify.theme.dark = true
  },
  mounted() {
    if (localStorage.getItem("authorization")) {
      this.$store.dispatch("accounts/getUserInfo", {
        userid: localStorage.getItem('userid')
      }) 
    } else {
      this.$store.commit("accounts/DELETE_TOKEN")
    }
  },

  methods: {
    // playMusic(gm) {
    //   console.log('app', gm)
    //   this.musicdata = gm
    //   console.log(this.musicdata, 'w')
    // },
    toggleAppDrawer () {
      this.appDrawer = !this.appDrawer
    },
    goBack () {
      // console.log(this.$router)
      this.$router.go(-1)
    },
    toggleLayout () {
      this.layout = !this.layout
    },
    disableLayout () {
      this.layout = false
      this.switchTab(0)
    },
    switchTab (tab) {
      this.tab = tab
    }
  }
}
</script>

<style scoped>
/* html { overflow-y: auto } */
.cursor-pointer{
  cursor: pointer;
}
.fullheight-desktop{
  margin-bottom:96px
}
.fullheight-mobile{
  padding-bottom:48px !important
}
</style>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.app{
  width: 100vw;
  min-height: 100vh;
  background: #F3F3F3;
  color: #15202B;
}
#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

<style>
table {
  background-color: #121212;
}

.row{
  display: flex !important;
  flex-wrap: wrap !important;
  flex: 1 1 auto !important;
}
</style>
