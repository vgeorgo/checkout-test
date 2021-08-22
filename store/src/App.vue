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
      <v-stepper alt-labels v-model="step" style="height: 100%">
        <v-stepper-header>
          <v-stepper-step step="1" :complete="step > 1">
            Choose
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="2" :complete="step > 2">
            Review
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="3" :complete="step > 3">
            Payment
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="4" :complete="step > 3">
            Enjoy!
          </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <Choose :categories="categories" :items="items" />
            <v-container class="d-flex flex-row-reverse">
              <v-btn color="yellow" @click="step = 2" class="ml-5" large>
                Review
              </v-btn>
              <v-btn text large> Clear cart </v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="2">
            <Checkout :items="items" />
            <v-container class="d-flex flex-row-reverse">
              <v-btn color="yellow" @click="step = 3" class="ml-5" large>
                Pay
              </v-btn>
              <v-btn text @click="step = 1" large> Back </v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="3">
            <Status />
            <v-container class="d-flex flex-row-reverse">
              <v-btn color="yellow" @click="step = 4" class="ml-5" large>
                Confirm
              </v-btn>
              <v-btn text @click="step = 2" large> Back </v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="4">
            <Status />
            <v-container class="d-flex flex-row-reverse">
              <v-btn color="yellow" @click="step = 1" large> Back </v-btn>
            </v-container>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
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
    step: 1,
    categories: [
      {
        id: 1,
        icon: "bread-slice-outline",
        image_id: "f3fbf57b118fa9",
        name: "Bakery",
      },
      {
        id: 2,
        icon: "bread-slice-outline",
        image_id: "b271afbefdc554",
        name: "Entrees",
      },
      {
        id: 3,
        icon: "bread-slice-outline",
        image_id: "eba73b2361fae3",
        name: "Drinks",
      },
    ],
    items: [
      {
        category_id: 1,
        id: 1,
        image_id: "293202f9d9f7f4",
        name: "Bagel",
        price: 2.0,
      },
      {
        category_id: 1,
        id: 2,
        image_id: "808916fd5ddf96",
        name: "Croissant",
        price: 1.0,
      },
      {
        category_id: 1,
        id: 3,
        image_id: "95d02a230fe050",
        name: "Muffin",
        price: 1.25,
      },
      {
        category_id: 1,
        id: 4,
        image_id: "23f95765b967ff",
        name: "Toast / Bread",
        price: 1,
      },
      {
        category_id: 1,
        id: 5,
        image_id: "5650be5d48a99b",
        name: "English Muffin",
        price: 2.5,
      },
      {
        category_id: 2,
        id: 6,
        image_id: "bd237a0c0d19ef",
        name: "Pasta Bar",
        price: 12.99,
      },
      {
        category_id: 2,
        id: 7,
        image_id: "3e1bd1342800f7",
        name: "Mediterranean Entree",
        price: 10.99,
      },
      {
        category_id: 2,
        id: 8,
        image_id: "72589c4c990f97",
        name: "Indian Entree",
        price: 11.95,
      },
      {
        category_id: 3,
        id: 9,
        image_id: "70c2a6247e7b58",
        name: "Small Drink",
        price: 0.75,
      },
      {
        category_id: 3,
        id: 10,
        image_id: "dba0fc03da30ca",
        name: "Medium Drink",
        price: 1.5,
      },
      {
        category_id: 3,
        id: 11,
        image_id: "ffc9bf61e441cd",
        name: "Large Drink",
        price: 2,
      },
    ],
  }),
};
</script>
