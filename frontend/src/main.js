import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import store from "./store"
import router from './router'
import VueDictaphone from 'vue-dictaphone'
import VuePlyr from 'vue-plyr'
import axios from 'axios'
import api from './api'
import VModal from 'vue-js-modal'
import AudioVisual from 'vue-audio-visual'
import Gravatar from 'vue-gravatar';
 
Vue.component('v-gravatar', Gravatar);

Vue.use(AudioVisual)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// // Install BootstrapVue
// Vue.use(BootstrapVue)
// // Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin)


Vue.use(VModal, {dynamicDefaults: { dynamic:true, adaptive: true}})

Vue.use(VuePlyr, {
  plyr: {
    fullscreen: { enabled: false }
  },
  emit: ['ended']
})

Vue.use(VueDictaphone)
Vue.config.productionTip = false

axios.interceptors.request.use(
  function(config) {
    // 요청을 보내기 전에 수행할 일
    config.headers.Authorization = localStorage.getItem('authorization')

    return config
  },
  function(error) {
    // 오류 요청을 보내기전 수행할 일
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(
  function(response) {
    return response
  },

  function(err) {
    const errorAPI = err.config

    // if (err.response.status===401 && errorAPI.retry===undefined) {
    if (err.response.status === 406 && errorAPI.retry === undefined) {
      errorAPI.retry = true

      if (localStorage.getItem('authorization')) {
        const tokenData = {
          token: localStorage.getItem('authorization')
        }
        return api.renewToken(tokenData)
          .then(res => {
            store.account.commit("SET_TOKEN", res.headers)
            return axios(errorAPI);
          })
          .catch(err => {
            console.error(err.response.data);
            store.account.commit("DELETE_TOKEN");
          })
      } else {
        console.log('No authorization')
      }
      
    } else if (err.response.status === 401 && !!localStorage.getItem("authorization")) {
        store.account.commit("DELETE_TOKEN");
    }
    return Promise.reject(err);
  }
)

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
