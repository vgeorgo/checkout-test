<template>
  <v-app>
    <v-app-bar app dense flat color="yellow">
      <div class="d-flex align-center">
        <v-img
          alt="Store Logo"
          class="mr-4"
          src="/images/ui/cart.png"
          width="30"
        />

        <div class="text-h4" color="black">Store</div>
      </div>
    </v-app-bar>

    <v-main>
      <v-tabs fixed-tabs background-color="yellow" v-model="tabs">
        <v-tab>Choose</v-tab>
        <v-tab>Checkout</v-tab>
        <v-tab>Staus</v-tab>
      </v-tabs>

      <v-tabs-items v-model="tabs">
        <v-tab-item key="choose" :transition="false">
          <Choose />
        </v-tab-item>
        <v-tab-item key="checkout" :transition="false">
          <Checkout />
        </v-tab-item>
        <v-tab-item key="status" :transition="false">
          <Status />
        </v-tab-item>
      </v-tabs-items>
    </v-main>
  </v-app>
</template>

<script>
import Choose from "./components/pages/Choose.vue";
import Checkout from "./components/pages/Checkout.vue";
import Status from "./components/pages/Status.vue";

export default {
  name: "App",

  components: {
    Choose,
    Checkout,
    Status,
  },

  data: () => ({
    tabs: null,
    cart: [],
  }),
};
</script>
