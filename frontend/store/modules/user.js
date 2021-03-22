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
    loggedin: false,
    username: "Guest",
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
    changeLoginStatus({ commit, state, dispatch }, loggedin) {
      commit('updateLoginStatus', { loggedin });
    },
    login({ commit, state, dispatch }, message) {
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
    },
    logout({ commit, state, dispatch }, message) {
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
      ]
      commit('updateUserMenu', { menu });
      let menuAction = [actionBuilder.newProvideMenuAction()];
      this.dispatch('actions/emitActionRequest', menuAction);

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
    updateLoginStatus(state, { loggedin }) {
      state.loggedin = loggedin;
    },
    updateUserMenu(state, { menu }) {
      console.log("change menu");
      state.usermenu = menu;
    },
    updateToken(state, token) {
      console.log("change token", token);
      state.jwttoken = token;
    }
  }
};