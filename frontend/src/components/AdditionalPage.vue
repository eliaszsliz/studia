<template>

          <v-card :class="$_settings.normalElevationClasses">
              <v-card-text
                v-if="loaded"
                class="cardPadding htmlContent htmlContentSmaller"
                v-html="page.body"
                ></v-card-text>

              <v-card-text
                v-else
                class="cardPadding htmlContent"
                >

                <v-skeleton-text
                                :width="{ min: 250, max: 600}"
                                height="200%"
                        ></v-skeleton-text>
                  <br>
                  <br>

                  <v-skeleton-element
                            width="40%"
                            height="30vh"
                            class="mx-auto"
                        ></v-skeleton-element>
                  <br>

                  <v-skeleton-text
                                :width="{ min: 150, max: 600}"
                                height="200%"
                        ></v-skeleton-text>
                  <br>
                  <br>
                  <v-skeleton-text
                                :width="{ min: 200, max: 600}"
                                height="200%"
                        ></v-skeleton-text>
              </v-card-text>

          </v-card>
</template>

<script>
import PageTitleMixin from './PageTitleMixin';
import VSkeletonText from './VSkeletonText.vue';
import VSkeletonElement from './VSkeletonElement.vue';

export default {
  name: 'AdditionalPage',
  components: { VSkeletonText, VSkeletonElement },
  mixins: [PageTitleMixin],
  data() {
    return {
      page: {},
      loaded: false,
    };
  },
  watch: {
    '$route.params.pageLink': function routerPageLinkWatcher(newVal) {
      this.fetchPageBody(newVal);
    },
  },
  created() {
    this.fetchPageBody(this.$route.params.pageLink);
  },
  methods: {
    fetchPageBody(pageLink) {
      this.$store.dispatch('getFlatPage', { pageLink })
        .then((data) => {
          this.page = data;
          this.title = data.title;
          this.loaded = true;
        });
    },
  },
};

</script>

