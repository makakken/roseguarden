import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

export default {
  namespaced: true,
  state: {
    drawer: true,
    page: 'test',
    backendVersion: 'Unknown',
    frontendVersion: JSON.parse(unescape(process.env.FRONTENDVERSION).toString()),

  },
  actions: {

  },
  mutations: {
    updateBackendVersion (state, { version }) {
      state.backendVersion = version;
    },
    toggleDrawer(state) {
      state.drawer = !state.drawer
    },
    togglePage(state) {
      if(state.page === 'pages/test.vue') {
        state.page = 'pages/test2.vue';
      } else {
        state.page = 'pages/test.vue';
      }
      console.log("toggled page", state.page  );
    },
    drawer(state, val) {
      state.drawer = val
    }
  }
};