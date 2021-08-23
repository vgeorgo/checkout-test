<template>
  <v-card class="ma-2">
    <v-img
      class="white--text align-end"
      :alt="`${item.name} Photo`"
      :src="`/images/items/${item.image_id}.jpg`"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="200px"
    >
      <v-card-title v-text="item.name"></v-card-title>
    </v-img>

    <v-card-actions>
      <v-card-text>
        Total: {{ getItemAmount(item) }} ($ {{ getItemTotal(item) }})
      </v-card-text>
      <v-spacer></v-spacer>

      <v-btn icon @click="minusItem(item)">
        <v-icon>mdi-minus</v-icon>
      </v-btn>

      <v-btn icon @click="addItem(item)">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import cartStore from "../../stores/cart";
import { formatNumber } from "../../helpers/currency";

export default {
  name: "ItemCard",

  props: {
    item: { type: Object, required: true },
  },

  components: {},

  data: () => ({}),

  computed: {
    getItemAmount: function () {
      return (item) => {
        if (!cartStore.state.items[item.id]) return 0;
        return cartStore.state.items[item.id].amount;
      };
    },
    getItemTotal: function () {
      return (item) => {
        if (!cartStore.state.items[item.id]) return formatNumber(0);
        return formatNumber(cartStore.state.items[item.id].total);
      };
    },
  },

  methods: {
    addItem: function (item) {
      cartStore.dispatch("addItem", item);
    },
    minusItem: function (item) {
      cartStore.dispatch("minusItem", item);
    },
  },
};
</script>