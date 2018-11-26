<template>
  <v-layout column>
    <v-flex :class="[$_settings.normalElevationClasses]"
            xs12
            >

      <v-card flat
              class="pb-3"
              >
          <the-index-issue-section
            :loaded="loaded"
            :issues="issues"
            />
      </v-card>
    </v-flex>

    <v-flex xs12>
      <v-layout>
        <v-flex
                class="text-xs-center mx-auto">
          <v-btn :to="{name: 'IssueList'}"
                 class="cursor-pointer TheIndex_MoreButton"
                 style="top: -50%">
            Przeglądaj wszystkie wydania
          </v-btn>
        </v-flex>
      </v-layout>
    </v-flex>

    <v-flex :class="[$_settings.normalElevationClasses]"
            xs12
            >
      <v-card flat
              class="pb-3"
              >
        <the-index-news-section
            :loaded="loaded"
            :items="newsList"
        ></the-index-news-section>
      </v-card>
    </v-flex>

    <v-flex xs12>
      <v-layout>
        <v-flex
                class="text-xs-center  mx-auto">
          <v-btn :to="{name: 'NewsList'}"
                 class="cursor-pointer TheIndex_MoreButton"
                 style="top: -50%"
                >
            Wszystkie newsy
          </v-btn>
        </v-flex>
      </v-layout>
    </v-flex>

  </v-layout>
</template>

<script>
import PageTitleMixin from '@/components/PageTitleMixin'; // todo zrobic folder mixins

import TheIndexIssueSection from '@/components/TheIndexIssueSection.vue';
import TheIndexNewsSection from '@/components/TheIndexNewsSection.vue';

export default {
  name: 'TheIndex',
  components: {
    TheIndexIssueSection, TheIndexNewsSection,
  },
  mixins: [PageTitleMixin],
  data() {
    return {
      newsList: [],
      issues: {
        current: {},
        next: {},
      },
      loaded: false,
    };
  },

  created() {
    this.fetchItems()
      .then((data) => {
        this.newsList = data.news;
        this.issues.current = data.issues.current;
        this.issues.next = data.issues.next;
        this.loaded = true;
      });
  },
  methods: {
    fetchItems() {
      return this.$store.dispatch('fetchHomePage');
    },
  },
};
</script>


<style lang="stylus">
@import "../stylus/variables.styl"

#app
    .TheIndexElement_Title
        font-family: $serif-font-family
        font-size: 21px !important
        line-height: 1.5 !important

    .TheIndexElement_Text
        font-family: $serif-font-family
        font-size: 15.3px
        line-height: 1.5
        letter-spacing: 0.03em

    .TheIndex_MoreButton.v-btn
      background: $primary-gradient
      background-color: primary_color
      color: primary_color_light_1

</style>
