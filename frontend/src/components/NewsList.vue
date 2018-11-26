<template>
    <v-layout
            column
    >

        <v-flex xs12>
            <news-list-element
                    v-for="item in items"
                    :key="item.id"
                    :item="item"
                    :show-more.sync="item.showMore"
                    class="mb-4"
                    @update:category="changeFilter"
            ></news-list-element>
        </v-flex>

        <v-flex xs12>
            <news-list-dummy
                        v-for="i in 2"
                        v-if="loading"
                        :key="i"
                        class="mb-4"
                ></news-list-dummy>


        </v-flex>

        <v-flex v-if="nextPage" xs12>
            <v-btn
                    flat
                    block
                    primary
            @click="loadMore">
                <v-icon class="mx-2">expand_more</v-icon>
                Wczytaj więcej
                <v-icon class="mx-2">expand_more</v-icon>
            </v-btn>
        </v-flex>

        <v-flex v-show="loading"
                xs12>
            <span class="secondary--text">
              Wszystkich wyników: {{ items.length }}
            </span>
        </v-flex>
    </v-layout>

</template>

<script>

import PageTitleMixin from './PageTitleMixin';
import NewsListElement from './NewsListElement.vue';
import NewsListDummy from './NewsListDummy.vue';

const ITEMS_PER_PAGE = 2;

export default {
  name: 'NewsList',
  components: { NewsListElement, NewsListDummy },
  mixins: [PageTitleMixin],
  data() {
    return {
      items: [],
      bottom: false,
      title: 'Z pracy redakcji',
      nextPage: 1,
      loading: false,
    };
  },
  computed: {
    categorySlugParam() { // todo dorobic get i set
      return this.$route.params.categorySlug;
    },
  },
  mounted() {
    console.log('mounted XD');
    this.loadMore();
    window.addEventListener('scroll', () => {
      this.handleScroll();
    });
  },
  methods: {
    bottomVisible() {
      const scrollY = window.scrollY;
      const visible = document.documentElement.clientHeight;
      const pageHeight = document.documentElement.scrollHeight;
      const bottomOfPage = visible + scrollY >= pageHeight;
      return bottomOfPage || pageHeight < visible;
    },

    shouldLoadMore() {
      return this.bottomVisible() && this.nextPage && !this.loading;
    },

    handleScroll() {
      if (this.shouldLoadMore()) {
        this.loadMore();
      }
    },

    loadMore() {
      this.loading = true;

      return this.fetchItems({ page: this.nextPage })
        .then((data) => {
          this.items = this.items.concat(data.items);
          this.nextPage = data.next;
          this.loading = false;
        });
    },


    changeFilter(category = null) {
      if (this.$route.params.categorySlug === category.slug || !category) {
        this.$router.push({ name: this.$route.name });
        this.title = 'Z pracy redakcji';
        this.nextPage = 1;
      } else {
        this.$router.push({ params: { categorySlug: category.slug } });
        this.title = `Z pracy redakcji - ${category.name}`;
        this.nextPage = 1;
      }
      this.items = [];
    },
    fetchItems({ page } = { page: 1 }) {
      return this.$store.dispatch('fetchNews', {
        categorySlug: this.categorySlugParam,
        page,
      });
    },
    manualLoad() {
      this.distance = 100;
      this.$nextTick(() => {
        this.$refs.infiniteLoading.attemptLoad();
      });
    },
  },
};
</script>
