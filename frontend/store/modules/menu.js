
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import menu from '@/api/menu';


Vue.use(VueAxios, axios);

export default {
  namespaced: true,
  state: {
    loading: true,
    submenu: false,
    mainmenu: [],
    usermenu: []

  },
  actions: {
    updateMenu ({ commit, state, dispatch }, menu) {
      commit('setMainMenu', { mainmenu: menu });
      commit('setLoading', { loading: false });
    },
  },
  mutations: {
    setLoading (state, { loading } ) {
      state.loading = loading;
    },
    setSubmenu (state, { submenu } ) {
      state.submenu = submenu;
    },
    setMainMenu (state, { mainmenu }) {
      let m = mainmenu;
      mainmenu.push(...menu.MenuStaticAppend);
      state.mainmenu = mainmenu;
      state.loading = false;
    } 
  }
};