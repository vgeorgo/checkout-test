<template>
  <v-tabs vertical>
    <v-tab v-for="category in categories" :key="category.id" class="ma-4">
      <v-icon left>{{ category.icon }}</v-icon>
      <div>{{ category.name }}</div>
    </v-tab>

    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <p>
            Sed aliquam ultrices mauris. Donec posuere vulputate arcu. Morbi ac
            felis. Etiam feugiat lorem non metus. Sed a libero.
          </p>

          <p>
            Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus.
            Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc.
            Aliquam lobortis. Aliquam lobortis. Suspendisse non nisl sit amet
            velit hendrerit rutrum.
          </p>

          <p class="mb-0">
            Phasellus dolor. Fusce neque. Fusce fermentum odio nec arcu.
            Pellentesque libero tortor, tincidunt et, tincidunt eget, semper
            nec, quam. Phasellus blandit leo ut odio.
          </p>
        </v-card-text>
      </v-card>
    </v-tab-item>
    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <p>
            Morbi nec metus. Suspendisse faucibus, nunc et pellentesque egestas,
            lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Sed
            mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non
            adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt
            non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
          </p>

          <p>
            Suspendisse feugiat. Suspendisse faucibus, nunc et pellentesque
            egestas, lacus ante convallis tellus, vitae iaculis lacus elit id
            tortor. Proin viverra, ligula sit amet ultrices semper, ligula arcu
            tristique sapien, a accumsan nisi mauris ac eros. In hac habitasse
            platea dictumst. Fusce ac felis sit amet ligula pharetra
            condimentum.
          </p>

          <p>
            Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
            quis gravida magna mi a libero. Nam commodo suscipit quam. In
            consectetuer turpis ut velit. Sed cursus turpis vitae tortor.
            Aliquam eu nunc.
          </p>

          <p>
            Etiam ut purus mattis mauris sodales aliquam. Ut varius tincidunt
            libero. Aenean viverra rhoncus pede. Duis leo. Fusce fermentum odio
            nec arcu.
          </p>

          <p class="mb-0">
            Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui
            magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce
            commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis
            a, condimentum nec, nisi.
          </p>
        </v-card-text>
      </v-card>
    </v-tab-item>
    <v-tab-item>
      <v-card flat>
        <v-card-text>
          <p>
            Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam
            eget dui. Proin viverra, ligula sit amet ultrices semper, ligula
            arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna,
            posuere eget, vestibulum et, tempor auctor, justo.
          </p>

          <p class="mb-0">
            Cras sagittis. Phasellus nec sem in justo pellentesque facilisis.
            Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam
            felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at
            tortor in tellus interdum sagittis.
          </p>
        </v-card-text>
      </v-card>
    </v-tab-item>
  </v-tabs>
</template>

<script>
export default {
  name: "Choose",

  components: {},

  data: () => ({
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

  computed: {
    categoryItems: function () {
      const mapData = {};
      this.categories.forEach((c) => {
        mapData[c.id] = this.items.filter((i) => i.category_id === c.id);
      });
      console.log(mapData);
      return mapData;
    },
  },
};
</script>