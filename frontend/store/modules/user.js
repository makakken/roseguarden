import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueCookies from 'vue-cookies';
import { mapState } from 'vuex';
import * as actionBuilder from '@/api/actionBuilder';

Vue.use(VueCookies, VueAxios, axios);
export default {
  namespaced: true,
  state: {
    jwttoken: null,
    loading: true,
    valid: false,
    firstname: "",
    lastname: "",
    email: "",
    usermenu: [
      {
        icon: 'input',
        href: '/user/login',
        title: 'Login',
        click: (e) => {
          console.log(e);
        }
      },
      {
        icon: 'create',
        href: '/user/register',
        title: 'Register',
        click: (e) => {
          console.log(e);
        }
      },
    ],
  },
  actions: {
    setUserInfo({ commit, state, dispatch }, [firstname, lastname, email]) {
      let menu = [
        {
          icon: 'face',
          href: '/user/account',
          title: 'Account',
          click: (e) => {
            console.log(e);
          }
        },
        {
          icon: 'cancel',
          href: '/dashboard',
          title: 'Logout',
          click: (e) => {
            dispatch('resetToken', null);
            // dispatch('logout', null);
          }
        }
      ];
      commit('updateUserMenu', { menu });
      commit('updateUserInfo', [firstname, lastname, email]);
      commit('setLoadingFinished');
    },
    resetUserInfo({ commit, state, dispatch }) {
      let menu = [
        {
          icon: 'input',
          href: '/user/login',
          title: 'Login',
          click: (e) => {
            console.log(e);
          }
        },
        {
          icon: 'create',
          href: '/user/register',
          title: 'Register',
          click: (e) => {
            console.log(e);
          }
        },
      ];
      commit('updateUserMenu', { menu });
      commit('resetUserInfo');
      commit('setLoadingFinished');

    },
    login({ commit, state, dispatch }, message) {
      let infoAction = [actionBuilder.newProvideUserInfoAction()];
      this.dispatch('actions/emitActionRequest', infoAction);
    },
    logout({ commit, state, dispatch }, message) {
      let actions = [actionBuilder.newProvideMenuAction(), actionBuilder.newProvideUserInfoAction()];
      this.dispatch('actions/emitActionRequest', actions);
    },
    setToken({ commit, state, dispatch }, token) {
      $cookies.set("user_jwt", token, 60 * 60);
      commit('updateToken', token)
    },
    resetToken({ commit, state, dispatch }) {
      commit('updateToken', '')
      $cookies.remove("user_jwt");
    },
  },
  mutations: {
    setLoadingFinished(state) {
      state.loading = false;
    },
    updateUserMenu(state, { menu }) {
      state.usermenu = menu;
    },
    updateToken(state, token) {
      state.jwttoken = token;
    },
    resetUserInfo(state) {
      console.log("resetUserInfo");
      state.valid = false;
      state.firstname = "";
      state.lastname = "";
      state.email = "";
    },
    updateUserInfo(state, [firstname, lastname, email]) {
      console.log("updateUserInfo");
      state.valid = true;
      state.firstname = firstname;
      state.lastname = lastname;
      state.email = email;
    }
  }
};