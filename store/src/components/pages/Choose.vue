<template>
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
            cols="4"
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
          </v-col>
        </v-row>
      </v-container>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import cartStore from "../../stores/cart";
import { formatNumber } from "../../helpers/currency";

export default {
  name: "Choose",

  props: {
    categories: { type: Array, required: true },
    items: { type: Array, required: true },
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
    categoryItems: function () {
      const mapData = {};
      this.categories.forEach((c) => {
        mapData[c.id] = this.items.filter((i) => i.category_id === c.id);
      });

      return mapData;
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