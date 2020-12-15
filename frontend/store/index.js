import Vue from 'vue'
import Vuex from 'vuex';
import actionsStore from './modules/actions'
import userStore from './modules/user'
import actionlinkStore from './modules/actionlink'
import notificationsStore from './modules/notifications'
import appStore from './modules/app'
import menuStore from './modules/menu'
import viewStore from './modules/views'


Vue.use(Vuex);


const createStore = () => {
  return new Vuex.Store({
    namespaced: true,
    modules: {
      notifications: notificationsStore,
      app: appStore,
      user: userStore,
      menu: menuStore,
      actionlink: actionlinkStore,
      actions: actionsStore,
      views: viewStore,
    },
  });
};


/*

export const state = () => ({
  drawer: true
})

export const mutations = {
  toggleDrawer(state) {
    state.drawer = !state.drawer
  },
  drawer(state, val) {
    state.drawer = val
  }
}
*/


export default createStore

