// import api from '../../api'

// state
const state = {
    musicdata: {"item":{
        "album":{"id":"76IRLp7YzBVLKsat6Ro9ae",
        "trackslist":[
            {"artists":[],
            "youtube_urls":"/watch?v=i23NEQEFpgQ",
            "name":"",
            "preview_url":"https://p.scdn.co/mp3-preview/dfc669bfa86bec8fe74de00b249fe1c75c748070?cid=a09fdcc51588442c985dbbe26c5b1989",}],
            "images":[{"height":640,"url":"https://i.ibb.co/vVryJmQ/default-cover.png","width":640},
            {"height":300,"url":"https://i.ibb.co/vVryJmQ/default-cover.png","width":300},
            {"height":64,"url":"https://i.ibb.co/vVryJmQ/default-cover.png","width":64}],
            "artists":[{"name":"Bigdata Music & Karaoke Player"}],
            "name":"",
            "total_tracks":1},
            "preview_url":"",
            "name":"너의 목소리가 들려",
            "artists":[],
            "youtube_urls":""}}
}
  
// getters
const getters = {
    MUSICDATA: state => state.musicdata
}
  
// mutations
const mutations = {
    addMusicData: (state, item) => {           
        state.musicdata = item
        window.console.log("ADD_EVENT", state.musicdata)
    },
}
  
// actions
const actions = {
    playMusic(store, item) {
        // console.log('vuex playmusic', item, '!')
        store.commit('addMusicData',{ item: item });
    }
}
  
export default {
namespaced: true,
state,
getters,
mutations,
actions,
};  