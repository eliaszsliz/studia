<template>
    <v-layout wrap>

        <v-flex
            v-for="item in items"
            :key="`item-${item.id}`"
            xs12 sm6 md4
            class="pa-3"
            >
            <the-index-news-element
                  :item="item"
                  ></the-index-news-element>
        </v-flex>

        <v-flex
          v-for="i in 3"
          v-show="!loaded"
          :key="i"
          xs12 sm6 md4
          class='pa-3'>
            <the-index-news-dummy/>
        </v-flex>
    </v-layout>
</template>

<script>
import TheIndexNewsElement from '@/components/TheIndexNewsElement.vue';
import TheIndexNewsDummy from '@/components/TheIndexNewsDummy.vue';

export default {
  name: 'TheIndexNewsSection',
  components: {
    TheIndexNewsElement, TheIndexNewsDummy,
  },
  props: {
    items: {
      type: Array,
      default: () => [],
    },
    loaded: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="stylus" scoped>
</style>
