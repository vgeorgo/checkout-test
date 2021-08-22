import Vue from 'vue'
import Vuex from 'vuex'

import api from '../services/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    categories: [],
    items: [],
  },
  actions: {
    loadItems({ commit }) {
      commit('loadItems');
    },
  },
  mutations: {
    loadItems(state) {
      api.getItems().then(function (response) {
        state.categories = response.data.categories;
        state.items = response.data.items;
      });
    },
  }
})