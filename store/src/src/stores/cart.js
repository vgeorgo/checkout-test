import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const defaultItem = {
  amount: 0,
  total: 0.0,
};

export default new Vuex.Store({
  state: {
    totalItems: 0.0,
    totalPrice: 0.0,
    items: {},
  },
  getters: {
    getItem: (state) => (id) => state.items[id] || { ...defaultItem },
    getItemAmount: (state, getters) => (id) => getters.getItem(id).amount,
    getItemTotal: (state, getters) => (id) => getters.getItem(id).total,
  },
  actions: {
    addItem({ commit }, item) {
      commit('addItem', item);
      commit('updateTotal');
    },
    minusItem({ commit }, item) {
      commit('minusItem', item);
      commit('updateTotal');
    },
    clear({ commit }) {
      commit('clear');
    }
  },
  mutations: {
    clear(state) {
      state.totalItems = 0.0;
      state.totalPrice = 0.0;
      state.items = {};
    },
    addItem(state, item) {
      const itemCart = state.items[item.id] || { ...defaultItem };
      itemCart.amount += 1;
      itemCart.total = itemCart.amount * item.price;

      state.items[item.id] = itemCart;
    },
    minusItem(state, item) {
      const itemCart = state.items[item.id];
      if (!itemCart) return;

      itemCart.amount -= 1;
      itemCart.total = itemCart.amount * item.price;
      if (itemCart.amount === 0) delete state.items[item.id];
    },
    updateTotal(state) {
      state.totalItems = 0;
      state.totalPrice = 0.0;

      Object.keys(state.items).map((key) => {
        state.totalItems += state.items[key].amount;
        state.totalPrice += state.items[key].total;
      });

      state.items = { ...state.items }
    }
  }
})