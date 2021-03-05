import axios from 'axios';

const SERVER_URL = "http://localhost:8000/api";

export default {
  login(params) {
    return axios.post(`${SERVER_URL}/accounts/login/`, params)
  },
  signup(params) {
    return axios.post(`${SERVER_URL}/accounts/signup/`, params)
  },
  idCheck(params) {
    return axios.get(`${SERVER_URL}/accounts/id_check/${params}/`)
  },  
  addSangSong(params) {
    return axios.post(`${SERVER_URL}/accounts/add_sang_song/`, params)
  },
  addRecommendSong(params) {
    return axios.post(`${SERVER_URL}/accounts/add_re_song/`, params)
  },
  addPiRecommendSong(params) {
    return axios.post(`${SERVER_URL}/accounts/add_pi_re_song/`, params)
  },
  getUserInfo(params) {
    return axios.post(`${SERVER_URL}/accounts/user_info/`, params)
  },
  getUserSangSongs(params) {
    return axios.post(`${SERVER_URL}/accounts/get_user_sang_songs/`, params)
  },
  getUserPiReSongs(params) {
    return axios.post(`${SERVER_URL}/accounts/get_user_pi_re_songs/`, params)
  },
  getUserReSongs(params) {
    return axios.post(`${SERVER_URL}/accounts/get_user_re_songs/`, params)
  },
  getToken(params) {
    return axios.post(`${SERVER_URL}/auth/token/`, params)
  },
  renewToken(params) {
    return axios.post(`${SERVER_URL}/auth/token/refresh/`, params)
  },
  searchMusicInfo(page, keyword) {
    return axios.get(`${SERVER_URL}/music/search/${page}/${keyword}/`)
  },
  getAlbum(params) {
    return axios.get(`${SERVER_URL}/music/album/${params}/`)
  },
  getArtist(params) {
    return axios.get(`${SERVER_URL}/music/artist/${params}/`)
  },
  getTrack(params) {
    return axios.get(`${SERVER_URL}/music/track/${params}/`)
  },
  getPopularityMusic(page) {
    return axios.get(`${SERVER_URL}/music/tracks/popularity/${page}/`)
  },
  getClusterMusic(page, cluster) {
    return axios.get(`${SERVER_URL}/music/tracks/cluster/${page}/${cluster}/`)
  },
  recommendTasteMusic(params) {
    return axios.post(`${SERVER_URL}/music/recommend/`, params)
  },
};
