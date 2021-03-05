<template>
    <!-- navbar -->
  <v-app-bar
    app
    dense
    color="#FF8F00"
    clipped-left
    class="px-xs-0 px-sm-5 navbar"
  >
    <!-- left section -->
    <v-app-bar-nav-icon @click.stop="toggleAppDrawer" />
    <div class="d-flex align-center cursor-pointer" @click="goToHomePage">
      <div icon class="mr-2 d-none d-sm-flex" style="cursor: pointer; margin-top: 10px">
        <img src="../assets/lo3.png" style="width: 150px;">
      </div>
      <p class="headline ma-auto"></p>
    </div>
    <v-spacer /><!-- left section -->

    <!-- right section -->
    <v-text-field
      placeholder="Search Music or Artists"
      :append-icon="mdiMusic"
      single-line
      hide-details
      class="mr-5 d-none d-sm-flex"
      v-model="search"
      @keydown.enter="searchInput"
      color="white"
    />
    <v-spacer class="d-flex d-sm-none"></v-spacer>
    <v-text-field
      style="max-width: 30vw"
      v-if="searchOpen"
      autofocus
      placeholder="Search..."
      single-line
      color="white"
      hide-details
      class="mr-1 d-flex d-sm-none"
      v-model="search"
      @keydown.enter="searchInput"
    />
    <v-icon
      class="d-flex d-sm-none mr-0"
      @click="toggleSearchInput"
    >
      {{mdiMusic}}
    </v-icon>
    <!-- right section -->

  </v-app-bar>
</template>

<script>
import { mdiMusic } from '@mdi/js';

export default {
  created() {
    this.$emit('toggleAppDrawer')
  },

  data () {
    return {
      search: '',
      searchOpen: false,
      mdiMusic
    }
  },

  methods: {
    toggleAppDrawer () {
      this.$emit('toggleAppDrawer')
    },
    goToHomePage () {
      this.$router.push('/')
    },
    goToSearchPage () {
      this.searchOpen = false
      // this.$router.push('/search/' + this.search)
      if (this.search) {
        this.$router.push({name: 'Search', query: {keyword: this.search}})
      }
    },
    toggleSearchInput () {
      this.searchOpen = !this.searchOpen
    },
    searchInput () {
      this.goToSearchPage()
      // this.$store.commit('music/SET_SEARCH_KEYWORD', this.search)
      this.search = ''
      this.searchOpen = false
    },
    toggleDarkTheme () {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    }
  },
}
</script>

<style scoped>
.navbar {
  opacity: 0.9;
}

</style>

<style lang="scss">
.v-toolbar--dense .v-toolbar__content, .v-toolbar--dense .v-toolbar__extension {
  padding-bottom: 15px !important;
}
</style>
