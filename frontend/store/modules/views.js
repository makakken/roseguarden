import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import { strict } from 'assert';

Vue.use(VueAxios, axios);

export default {
  namespaced: true,
  state: {
    viewDictionary: {},
    viewStates: {},
    viewAnnouncementCounter: {},
  },
  actions: {
    loadView ({ commit, state, dispatch }, [viewname, viewdata]) {
      commit('loadView', [viewname, viewdata]);
      if(state.viewAnnouncementCounter[viewname] === 0) {
        commit('updateViewState', [viewname, 'ready']);
      }
    },
    announceLoadView ({ commit, state, dispatch }, [viewname]) {
      commit('incrementLoadViewAnnouncement', [viewname]);
      commit('updateViewState', [viewname, 'loading']);
    }
  },
  getters: {
    // modified getField(path) from the mapField-package
    // return a lambda function to update nodes when needed by vue,
    getView(state, path) {
      // getField modified 
      return function (path) {
        try {
          // split the path e.g. "config.acquisition.adc1Gain" to a list and
          // try to go through the list by the token starting with state.dataTree 
          // result is the lasting node value
          // split use regex-expressions here, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
          let result = path.split(/[.[\]]+/).reduce(function (prev, key) {
            return prev[key];
          }, state.viewDictionary);
          return result._value;  
        } catch (e) {
          // if failure 
          console.log("getting view ",  path, " failed");
          return "";
        }
      }; 
    },
  },    
  mutations: {
    updateViewState(state, [viewname, viewstate]) {
      let newviewState = {};
      newviewState[viewname] = viewstate;
      state.viewStates[viewname] = viewstate;
      state.viewStates = {...state.viewStates};
      console.log("updateViewState ",viewname , "successful with: ", viewstate, state.viewStates);
    },
    loadView(state, [viewname, viewdata]) {
      let newview = {};
      newview[viewname] = viewdata
      state.viewDictionary = {...state.viewDictionary, ...newview};
      state.viewAnnouncementCounter[viewname] -=1;
      console.log("loadView successful with", state.viewDictionary);
    },
    incrementLoadViewAnnouncement(state, [viewname]) {
      if(!state.viewAnnouncementCounter.hasOwnProperty(viewname)) {
        state.viewAnnouncementCounter[viewname] = 0;
      }

      state.viewAnnouncementCounter[viewname] += 1;
      console.log('increment counter', viewname, state.viewAnnouncementCounter[viewname]);
    },
    updateView(state, node) {
      // modified updateField(state.user, node) from the mapField-package
      // split the path e.g. "config.acquisition.adc1Gain" to a list and
      // try to go through the list by the token starting with state.dataTree 
      // result is the lasting node value
      // split use regex-expressions here, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
      try {
        let result = node.path.split(/[.[\]]+/).reduce(function (prev, key, index, array) {
          if (array.length === index + 1) {
            if (typeof prev[key]._value === typeof node.value) {
              prev[key]._value = node.value;
            } else {
              throw new TypeError('updateView type invalid error from : ' + (typeof prev[key]._value) + ' to ' + (typeof node.value), "updateView", 0);
            }
          }
          return prev[key];        
        }, state.viewDictionary);
      } catch (e) {
        console.log("updating view ",  path, " failed");
      }
    },      
  }
};