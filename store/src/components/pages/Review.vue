<template>
  <v-simple-table class="mb-10">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left" style="width: 50%">Item</th>
          <th class="text-center" style="width: 20%">Amount</th>
          <th class="text-right" style="width: 30%">Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in itemRows" :key="item.id">
          <td class="text-left" :class="item.customClass">{{ item.name }}</td>
          <td class="text-center" :class="item.customClass">
            <v-btn v-if="!item.locked" icon @click="minusItem(item)">
              <v-icon>mdi-minus</v-icon>
            </v-btn>
            {{ item.amount }}
            <v-btn v-if="!item.locked" icon @click="addItem(item)">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </td>
          <td class="text-right" :class="item.customClass">{{ item.total }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import cartStore from "../../stores/cart";
import { formatNumber } from "../../helpers/currency";

export default {
  name: "Review",

  props: {
    items: { type: Array, required: true },
  },

  computed: {
    itemMap: function () {
      const items = {};
      this.items.map((i) => (items[i.id] = i));
      return items;
    },
    itemRows: function () {
      const cartItems = Object.keys(cartStore.state.items).map((key) => {
        const values = cartStore.state.items[key];

        return Object.assign({}, this.itemMap[key], {
          amount: values.amount,
          total: `$ ${formatNumber(values.total)}`,
        });
      });

      cartItems.push({
        name: "Total",
        amount: cartStore.state.totalItems,
        total: `$ ${formatNumber(cartStore.state.totalPrice)}`,
        locked: true,
        customClass: "font-weight-black",
      });

      return cartItems;
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