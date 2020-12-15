import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

export default {
  namespaced: true,
  state: {
    message: "",
    show: false,
    color: "",
  },
  actions: {
    pushError ({ commit, state, dispatch }, message) {
      commit('updateSnackbar', { message: message, color: "error" });
    },
    pushWarning ({ commit, state, dispatch }, message) {
      commit('updateSnackbar', { message: message, color: "warning" });
    },
    pushInfo ({ commit, state, dispatch }, message) {
      commit('updateSnackbar', { message: message, color: "info" });
    },
    pushSuccess ({ commit, state, dispatch }, message) {
      commit('updateSnackbar', { message: message, color: "success" });
    },
    pushNotification ({ commit, state, dispatch }, [message, color]) {
      commit('updateSnackbar', { message: message, color: color });
    }
  },
  mutations: {
    updateSnackbar (state, { message, color } ) {
      state.message = message;
      state.color = color;
      state.show = true;  
    }
  }
};