import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import music from './modules/music'
import player from './modules/player'
import karaoke from './modules/karaoke'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    accounts,
    music,
    player,
    karaoke,
  }
});