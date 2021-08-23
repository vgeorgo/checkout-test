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
          <template v-for="(config, stepId) in stepsConfig">
            <v-stepper-step
              :step="stepId"
              :complete="config.complete(step)"
              :key="stepId"
            >
              {{ config.name }}
            </v-stepper-step>
            <v-divider
              v-if="stepId != steps.SUCCESS"
              :key="`divider-${stepId}`"
            ></v-divider>
          </template>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content
            v-for="(config, stepId) in stepsConfig"
            :step="stepId"
            :key="`step-content-${stepId}`"
            class="px-0 pb-0"
          >
            <component
              v-bind:is="config.component"
              v-on:step="changeStep"
            ></component>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-main>
  </v-app>
</template>

<script>
import itemStore from "./stores/item";
import steps from "./constants/steps";
import Choose from "./components/pages/Choose.vue";
import Review from "./components/pages/Review.vue";
import Checkout from "./components/pages/Checkout.vue";
import Success from "./components/pages/Success.vue";

export default {
  name: "App",

  components: {
    Choose,
    Review,
    Checkout,
    Success,
  },

  created() {
    itemStore.dispatch("loadItems");
    this.step = this.steps.CHOOSE;
  },

  computed: {
    steps: function () {
      return steps;
    },
    stepsConfig: function () {
      return {
        [this.steps.CHOOSE]: {
          name: "Choose",
          component: "Choose",
          complete: (step) => step > steps.CHOOSE,
        },
        [this.steps.REVIEW]: {
          name: "Review",
          component: "Review",
          complete: (step) => step > steps.REVIEW,
        },
        [this.steps.CHECKOUT]: {
          name: "Payment",
          component: "Checkout",
          complete: (step) => step > steps.CHECKOUT,
        },
        [this.steps.SUCCESS]: {
          name: "Enjoy!",
          component: "Success",
          complete: (step) => step > steps.CHECKOUT,
        },
      };
    },
  },

  data: () => ({
    step: null,
  }),

  methods: {
    changeStep: function (step) {
      this.step = step;
    },
  },
};
</script>
