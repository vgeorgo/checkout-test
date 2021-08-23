<template>
  <v-container>
    <v-simple-table class="mb-10">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left" style="width: 10%">Photo</th>
            <th class="text-left" style="width: 50%">Item</th>
            <th class="text-center" style="width: 20%">Amount</th>
            <th class="text-right" style="width: 20%">Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in itemRows" :key="item.id" :class="item.customClass">
            <td class="text-left">
              <v-img
                v-if="item.image_id"
                class="white--text align-end"
                :alt="`${item.name} Photo`"
                :src="`/images/items/${item.image_id}.jpg`"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                max-width="80px"
              />
            </td>
            <td class="text-left">{{ item.name }}</td>
            <td class="text-center" nowrap>
              <v-btn v-if="!item.locked" icon @click="minusItem(item)">
                <v-icon>mdi-minus</v-icon>
              </v-btn>
              {{ item.amount }}
              <v-btn v-if="!item.locked" icon @click="addItem(item)">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </td>
            <td class="text-right" nowrap>{{ item.total }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <v-container class="d-flex flex-row-reverse">
      <v-btn
        color="yellow"
        @click="nextStep"
        class="ml-5"
        large
        :disabled="totalItems == 0"
      >
        Checkout
      </v-btn>
      <v-btn text @click="backStep" large> Back </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import cartStore from "../../stores/cart";
import itemStore from "../../stores/item";
import steps from "../../constants/steps";
import { formatNumber } from "../../helpers/currency";

export default {
  name: "Review",

  computed: {
    totalItems: function () {
      return cartStore.state.totalItems;
    },
    items: function () {
      return itemStore.state.items;
    },
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
    nextStep: function () {
      this.$emit("step", steps.CHECKOUT);
    },
    backStep: function () {
      this.$emit("step", steps.CHOOSE);
    },
  },
};
</script>