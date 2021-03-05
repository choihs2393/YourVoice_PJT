import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
      iconfont: 'mdiSvg', // default - only for display purposes
  },
  theme: {
    dark: {
      primary: '#fc5185',
      secondary: '#3a3d44',
      accent: '#43dde6',
      error: '#FF5252',
      info: '#2196F3',
      success: '#4CAF50',
      warning: '#FFC107'
    },
  },
});
