<template>
  <v-list dense shaped>
    <v-list-item-group v-model="item" color="orange">

    <!-- user avatar and info -->
    <v-list-item disabled>
      <v-list-item-avatar v-if="!isLoggedIn" size=72 class="mx-auto">
        <img src="../assets/p1.png" class="mt-4 ml-1" style="width: 110px; height: 90px;">
      </v-list-item-avatar>
      <v-list-item-avatar v-else size=72 class="mt-10 mx-auto">
        <!-- <img v-if="isLoggedIn" src="../assets/logo.png" alt=""> -->
        <v-gravatar @click="gotoMypage" :email="userInfo.userid" />
      </v-list-item-avatar>
    </v-list-item>
    <div v-if="!isLoggedIn" class="m-2" style="text-align: center; color: white;">
      <p class="jg m-0">지금 로그인해</p>
      <p class="jg">다양한 서비스를 경험해보세요!</p>
      <button class="btn" style="color: orange; border: 1px solid orange;" @click="gotoLogin">Login</button>
    </div>
    <div v-else>
      <v-list-item disabled>
        <v-list-item-content>
          <v-list-item-title class="text-center jg" style="font-size: 16px;">{{ $store.state.accounts.userInfo.username }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <br>
    </div>
    
    <v-divider></v-divider>

    <!-- navigation items -->
    <v-list-item to="/">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title class="jg">Home</v-list-item-title>
        </v-list-item>
      <v-list-item link to="/artists">
          <v-list-item-icon>
            <v-icon>mdi-account-music</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title class="jg">Artists</v-list-item-title>
        </v-list-item>

        <v-list-group
          :prepend-icon="mdiThumbUp"
          color="orange"
          value="true"
        >
          <template v-slot:activator>
            <v-list-item-title class="jg">Recommend</v-list-item-title>
          </template>
  
          <v-list-item
            no-action
            sub-group
            color="orange"
            to="/recommend_voice"
          >
              <v-list-item-content>
                <v-list-item-title class="jg">내 목소리로 추천받기</v-list-item-title>
              </v-list-item-content>

          </v-list-item>
  
          <v-list-item
            sub-group
            no-action
            color="orange"
            to="/recommend_taste"
          >
              <v-list-item-content>
                <v-list-item-title class="jg">내 취향으로 추천받기</v-list-item-title>
              </v-list-item-content>
          </v-list-item>
        </v-list-group>
        <v-list-item to="/karaoke">
          <v-list-item-icon>
            <v-icon>mdi-microphone-variant</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title class="jg">노래방</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="isLoggedIn" to="/mypage">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title class="jg">My Page</v-list-item-title>
        </v-list-item>
        <!-- <v-list-item v-if="!isLoggedIn" to="/login">
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item> -->
        <v-list-item v-if="isLoggedIn" @click="onLogout">
          <v-list-item-icon>
            <v-icon>mdi-logout</v-icon>
          </v-list-item-icon>
  
          <v-list-item-title class="jg">Logout</v-list-item-title>
        </v-list-item>
    <v-divider></v-divider>
    <v-spacer></v-spacer>
    </v-list-item-group>
  </v-list>
</template>

<script>
import LoginModal from '../components/LoginModal.vue'

import { mdiMusic, mdiThumbUp} from '@mdi/js';
import { mapGetters, mapMutations } from 'vuex'

export default {
  data () {
    return {
      item: 2,
      mdiMusic,
      mdiThumbUp,
      items: [
        { icon: mdiMusic, text: 'Home', url: '/' },
        { icon: mdiMusic, text: 'Select Music', url: '/music' },
        { icon: mdiMusic, text: 'Recommend Music', url: '/record' },
        { icon: mdiMusic, text: 'Mypage', url: '/mypage' },
        { icon: mdiMusic, text: 'Karaoke', url: '/karaoke' },
        { icon: mdiMusic, text: 'Logout', url: '/logout' },
      ],
      admins: [
      ['Management', 'people_outline'],
      ['Settings', 'settings'],
    ],
    cruds: [
      ['Create', 'add'],
      ['Read', 'insert_drive_file'],
      ['Update', 'update'],
      ['Delete', 'delete'],
    ],
    }
  },
  components: {
    // LoginModal
  },
  computed: {
    ...mapGetters('accounts', ['isLoggedIn', 'userInfo'])
  },
  methods: {
    ...mapMutations('accounts', ['DELETE_TOKEN']),

    onLogout: async function() {
      await this.DELETE_TOKEN()
      this.$router.push('/')
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

    gotoMypage() {
      this.$router.push('/mypage')
    }
  }
}
</script>

<style scoped>

</style>
