import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

export default {
  namespaced: true,
  state: {
    message: "",
    status: "",
  },
  actions: {
    pushError ({ commit, state, dispatch }, message) {
      commit('updateStatus', { message: message, status: "error" });
    },
    pushSuccess ({ commit, state, dispatch }, message) {
      commit('updateStatus', { message: message, status: "success" });
    },
    pushStatus ({ commit, state, dispatch }, [status, message]) {
      commit('updateStatus', { message: message, status: status });
    }    
  },
  mutations: {
    updateStatus (state, { message, status } ) {
      state.message = message;
      state.status = status;
    }
  }
};