<template>
  <v-container>
    <v-card color="green" class="mb-5">
      <v-card-title>
        <span class="text-h6 font-weight-light">Enjoy!</span>
      </v-card-title>

      <v-card-text class="text-h5 font-weight-bold">
        Order successfully processed, have a nice day!
      </v-card-text>
    </v-card>
    <v-container class="d-flex flex-row-reverse">
      <v-btn color="yellow" @click="backStep" large> Back </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import cartStore from "../../stores/cart";
import steps from "../../constants/steps";

export default {
  name: "Success",

  components: {},

  data: () => ({}),

  methods: {
    backStep: function () {
      cartStore.dispatch("clear");
      this.$emit("step", steps.CHOOSE);
    },
  },
};
</script>