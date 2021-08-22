<template>
  <v-container>
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