import api from '../../api'
import swal from 'sweetalert';


// state
const state = {
  authorization: localStorage.getItem('authorization'),
  // refreshToken: localStorage.getItem("refresh-token"),

  // user info
  userInfo: {
    userid: "",
    username: "",
    password: "",
    sang_songs: [],
    re_songs: [],
    pi_re_songs:[],
    last_login: null,
    is_superuser: null,
    joindate: "",
    pitch: null,
    groups: [],
    user_permissions: [],
  },
}

// getters
const getters = {
  isLoggedIn: state => !!state.authorization,
  userInfo: state => state.userInfo
}

// mutations
const mutations = {
  SET_TOKEN(state, info) {
    if (info) {
      state.authorization = info.token
      localStorage.setItem('authorization', 'jwt ' + state.authorization)
      localStorage.setItem('userid', info.userid)
    }
  },
  DELETE_TOKEN(state) {
    state.authorization = null
    state.userInfo = {
      userid: "",
      username: "",
      password: "",
      sang_songs: [],
      re_songs: [],
      pi_re_songs:[],
      last_login: null,
      is_superuser: null,
      joindate: "",
      pitch: null,
      groups: [],
      user_permissions: [],
    },
    localStorage.removeItem('authorization')
    localStorage.removeItem('userid')
  },
  SET_INIT_USER_INFO(state, info) {
    state.userInfo = info;
    // console.log('회원정보!!!', info)
  },
}

// actions
const actions = {
  async signup({ dispatch }, params) {
    await api.signup(params)
    .then(() => {
      dispatch('login', params)
    })
    .catch(err => console.error(err.response.data))
  },

  async login({ dispatch }, params) {
    await api.login(params)
    .then(() => {
      dispatch('getToken', params)
      // this.$emit('close')
    })
    .catch(err => {
      if (err.response.status === 401) {
        // alert('아이디와 비밀번호가 맞지 않습니다.')
        swal('Warning', '아이디와 비밀번호가 맞지 않습니다.', 'warning')
      } else {
        console.error(err.response.data)
      }
    })
  },

  async getToken({ commit, dispatch }, params) {
    await api.getToken(params)
    .then(async res => {
      const info = {
        token: res.data.token,
        userid: params.userid,
      }
      await commit('SET_TOKEN', info)
      dispatch('getUserInfo', info)
    })
    .catch(err => console.error(err.response.data))
  },

  async idCheck(context, params) {
    await api.idCheck(params)
    .then(() => {
      // if (res.data.message) {
        // alert('사용가능한 아이디 입니다.')
        swal("your request is approved", {
          icon: "success",
        });
      // } else {
        // alert('이미 있는 아이디입니다.')
      // }
    })
    .catch(err => {
      if (err.response.status === 400) {
        // alert('이미 있는 아이디입니다.')
        swal('Warning', '이미 있는 아이디입니다.', 'warning')
      } else {
        console.error(err.response.data)
      }
    })
  },

  // async addSangSong(context, params) {
  //   await api.addSangSong(params)
  // },

  // 취향 추천 노래 추가
  async addRecommendSong({ dispatch }, params) {
    await api.addRecommendSong(params)
      .then(() => {
        const info = {
          token: localStorage.getItem('authorization'),
          userid: localStorage.getItem('userid'),
        }
        dispatch('getUserInfo', info)
      })
      .catch(err => console.error(err.response.data))
  },

  async addPiRecommendSong({ dispatch }, params) {
    await api.addPiRecommendSong(params)
      .then(() => {
        const info = {
          token: localStorage.getItem('authorization'),
          userid: localStorage.getItem('userid'),
        }
        dispatch('getUserInfo', info)
      })
      .catch(err => console.error(err.response.data))
  },

  // 초기 회원정보 세팅
  async getUserInfo({ commit }, params) {
    await api.getUserInfo(params)
      .then(res => {
        commit("SET_INIT_USER_INFO", res.data.data);
      })
      .catch(err => console.error(err.response.data));
  },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};  