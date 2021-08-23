<template>
  <v-container>
    <v-form ref="form">
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="12" sm="10" md="6" lg="5" xl="4">
            <v-alert v-if="error.active" type="error">
              {{ error.message }}
            </v-alert>
            <v-card ref="form">
              <v-card-text>
                <v-row justify="center" class="mb-2">
                  <v-col cols="8" class="text-h4 px-6">Total</v-col>
                  <v-col cols="4" class="text-h4 text-right px-6"
                    >$ {{ total }}</v-col
                  >
                </v-row>
                <v-divider class="mb-5"></v-divider>
                <v-row justify="center">
                  <v-col cols="12">
                    <v-text-field
                      label="Card Number"
                      v-model="form.card_number"
                      prepend-inner-icon="mdi-credit-card"
                      :rules="rules"
                      required
                    />
                  </v-col>
                </v-row>
                <v-row justify="center">
                  <v-col cols="8">
                    <v-text-field
                      label="Expiration Date"
                      v-model="form.expiration"
                      prepend-inner-icon="mdi-calendar"
                      :rules="rules"
                      required
                    />
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      label="CV Code"
                      v-model="form.cv"
                      prepend-inner-icon="mdi-lock"
                      :rules="rules"
                      required
                    />
                  </v-col>
                </v-row>
                <v-row justify="center">
                  <v-col cols="12">
                    <v-text-field
                      label="Card Owner"
                      v-model="form.owner"
                      prepend-inner-icon="mdi-account"
                      :rules="rules"
                      required
                    />
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <v-container class="d-flex flex-row-reverse">
      <v-btn color="yellow" @click="submit" class="ml-5" large>
        Process Payment
      </v-btn>
      <v-btn text @click="backStep" large> Back </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import cartStore from "../../stores/cart";
import steps from "../../constants/steps";
import { formatNumber } from "../../helpers/currency";
import api from "../../services/api";

const emptyForm = {
  card_number: "",
  expiration: "",
  cv: "",
  owner: "",
};

const emptyError = {
  active: false,
  message: "",
};

export default {
  name: "Checkout",

  components: {},

  computed: {
    total: function () {
      return formatNumber(cartStore.state.totalPrice);
    },
  },

  data: () => ({
    form: { ...emptyForm },
    error: { ...emptyError },
    rules: [(val) => (val || "").length > 0 || "This field is required"],
  }),

  methods: {
    setError(message) {
      this.error = { active: true, message };
    },
    getPayload() {
      const items = {};
      Object.keys(cartStore.state.items).map(
        (k) => (items[k] = cartStore.state.items[k].amount)
      );

      return {
        payment: { ...this.form },
        items,
      };
    },
    async submit() {
      if (!this.$refs.form.validate()) {
        this.setError("All fields are required!");
        return false;
      }

      const response = await api.createOrder(this.getPayload());
      if (response.status == 200) {
        this.clear();
        this.nextStep();
        return;
      }

      this.setError(response.data.message);
    },
    nextStep: function () {
      this.$emit("step", steps.SUCCESS);
    },
    backStep: function () {
      this.$emit("step", steps.REVIEW);
    },
    clear: function () {
      this.form = { ...emptyForm };
      this.error = { ...emptyError };
      this.$refs.form.reset();
    },
  },
};
</script>