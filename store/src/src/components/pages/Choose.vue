<template>
  <v-container class="pa-0 ma-0">
    <v-tabs vertical class="d-flex justify-center">
      <v-tab v-for="category in categories" :key="category.id">
        <v-icon left>{{ category.icon }}</v-icon>
        <div>{{ category.name }}</div>
      </v-tab>

      <v-tab-item
        v-for="category in categories"
        :key="`tab-${category.id}`"
        class="pa-2 ml-6"
        :transition="false"
      >
        <v-container fluid>
          <v-row class="mb-5">
            <div class="text-h4" cols="12">{{ category.name }}</div>
          </v-row>
          <ListItems :items="categoryItems[category.id]" />
        </v-container>
      </v-tab-item>
    </v-tabs>
    <v-container class="d-flex flex-row-reverse">
      <v-btn
        color="yellow"
        @click="nextStep"
        class="ml-5"
        large
        :disabled="totalItems == 0"
      >
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

import ListItems from "../ui/ListItems.vue";

export default {
  name: "Choose",

  components: {
    ListItems,
  },

  data: () => ({}),

  computed: {
    totalItems: function () {
      return cartStore.state.totalItems;
    },
    categories: function () {
      return itemStore.state.categories;
    },
    items: function () {
      return itemStore.state.items;
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
  },
};
</script>