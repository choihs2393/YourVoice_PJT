// import api from '../../api'

// state
const state = {
    mrdata: {
        "item": {
            "youtube_mr": "/watch?v=G9wdCWnLHus",
            "artists": [{"id": "3Nrfpe0tUJi4K4DXYWgMUX","name": "BTS"}],
            "album": { 
                "artists" : [{"id": "3Nrfpe0tUJi4K4DXYWgMUX", "name": "BTS"}],
                "images": [{"url": "https://i.scdn.co/image/ab67616d0000b2735469e11760fad283eaa07414"},
                            {"url": "https://i.scdn.co/image/ab67616d0000b2735469e11760fad283eaa07414"}],
                "name": "Dynamite"
            },
            "id": "2J4P46vCFm1rPkNkp9pZWX",
            "name": "Dynamite",
            "cluster": "1",
            "duration_ms": "x"
        }
    }

    // mrdata: null
}
  
// getters
const getters = {
    MR: state => state.mrdata
}
  
// mutations
const mutations = {
    addMR: (state, item) => {           
        state.mrdata = item
        // window.console.log("ADD_EVENT", state.mrdata)
    },
}
  
// actions
const actions = {
    playMR(store, item) {
        store.commit('addMR',{ item: item });
    }
}
  
export default {
namespaced: true,
state,
getters,
mutations,
actions,
};  