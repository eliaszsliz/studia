<template>
    <div class="text-xs-center my-5">

        <h1 class="display-4 grey--text text--lighten-3">
            404
        </h1>

        <h1 class="display-2 grey--text text--lighten-1">
            Strona której szukasz
        </h1>

        <h1 class="display-3 grey--text text--lighten">
            nie istnieje lub została usunięta
        </h1>



        <v-btn :to="{ name: 'Index' }" class="mt-5">
            wróć na stronę główną
        </v-btn>
    </div>
</template>

<script>
export default {
  name: 'Http404',
};
</script>

<style lang="stylus" scoped>
@import "../stylus/variables.styl"

#app
    .v-btn
      background: $primary-gradient
      background-color: primary_color
      color: primary_color_light_1
</style>

