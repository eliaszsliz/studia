<template>
    <v-bottom-nav
            id="AppBottomNav"
            :value="true"
            app
            fixed
            color="primary"
            class="hidden-md-and-up"
            >

      <v-layout>
          <v-flex
            class="text-xs-center"
            >
              <v-btn
                     :to="{ name: 'IssueList' }"
                     flat
                     class="AppBottomNav_Button "
                     >
                <span>Archiwum</span>
                <v-icon>library_books</v-icon>
              </v-btn>
          </v-flex>

          <v-flex
            v-if="showThirdButton"
            class="text-xs-center">
          </v-flex>


          <v-flex
            class="text-xs-center">

                <v-btn flat
                     class="AppBottomNav_Button"
                     @click.stop="$emit('update:sidebar', true)"
                     >
                <span>Menu</span>
                <v-icon>menu</v-icon>
              </v-btn>
          </v-flex>
      </v-layout>
  </v-bottom-nav>

</template>

<script>
export default {
  name: 'TheBottomNavigation',
  computed: {
    showThirdButton() {
      return false;
    },
  },
};
</script>

<style scoped>
</style>
