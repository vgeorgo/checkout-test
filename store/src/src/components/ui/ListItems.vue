<template>
  <v-row dense>
    <v-col
      v-for="item in items"
      :key="`${item.category_id}-item-${item.id}`"
      cols="12"
      md="4"
      sm="6"
      lg="3"
      xl="3"
    >
      <ItemCard :item="item" />
    </v-col>
  </v-row>
</template>

<script>
import ItemCard from "./ItemCard.vue";

export default {
  name: "ListItems",

  props: {
    items: { type: Array, required: true },
  },

  components: {
    ItemCard,
  },

  data: () => ({}),
};
</script>