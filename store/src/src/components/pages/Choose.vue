<template>
  <v-container>
    <v-tabs vertical>
      <v-tab v-for="category in categories" :key="category.id">
        <v-icon left>{{ category.icon }}</v-icon>
        <div>{{ category.name }}</div>
      </v-tab>

      <v-tab-item
        v-for="category in categories"
        :key="`tab-${category.id}`"
        class="pa-8"
        :transition="false"
      >
        <v-container fluid>
          <v-row class="mb-5">
            <div class="text-h4" cols="12">{{ category.name }}</div>
          </v-row>
          <v-row dense>
            <v-col
              v-for="item in categoryItems[category.id]"
              :key="`${category.id}-item-${item.id}`"
              cols="12"
              md="4"
              sm="6"
              lg="3"
              xl="3"
            >
              <v-card>
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
                    Total: {{ getItemAmount(item) }} ($
                    {{ getItemTotal(item) }})
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
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs>
    <v-container class="d-flex flex-row-reverse">
      <v-btn color="yellow" @click="nextStep" class="ml-5" large>
        Review
      </v-btn>
      <v-btn text @click="clearCart" large> Clear cart </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import cartStore from "../../stores/cart";
import itemStore from "../../stores/item";
import steps from "../../constants/steps";
import { formatNumber } from "../../helpers/currency";

export default {
  name: "Choose",

  components: {},

  data: () => ({}),

  computed: {
    categories: function () {
      return itemStore.state.categories;
    },
    items: function () {
      return itemStore.state.items;
    },
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
    categoryItems: function () {
      const mapData = {};
      this.categories.forEach((c) => {
        mapData[c.id] = this.items.filter((i) => i.category_id === c.id);
      });

      return mapData;
    },
  },

  methods: {
    nextStep: function () {
      this.$emit("step", steps.REVIEW);
    },
    clearCart: function () {
      cartStore.dispatch("clear");
    },
    addItem: function (item) {
      cartStore.dispatch("addItem", item);
    },
    minusItem: function (item) {
      cartStore.dispatch("minusItem", item);
    },
  },
};
</script>