<template>
    <v-layout
            wrap
            >
        <v-flex
            xs12 md4
            style="border-right: 1px solid rgba(0,0,0,0.12);"
            >

            <article-list-filter-section
                v-model="value.issues"
                :items="filterOptions.issues"
                item-key="id"
                header-text="Numery"
                ></article-list-filter-section>
        </v-flex>

        <v-flex xs12 md4
                style="border-right: 1px solid rgba(0,0,0,0.12);"
                >
             <article-list-filter-section
                v-model="value.authors"
                :items="filterOptions.authors"
                item-key="id"
                header-text="Autorzy"
                ></article-list-filter-section>
        </v-flex>

        <v-flex xs12 md4>
             <article-list-filter-section
                v-model="value.categories"
                :items="filterOptions.categories"
                item-key="id"
                header-text="Kategorie"
                ></article-list-filter-section>
        </v-flex>
    </v-layout>
</template>

<script>
import ArticleListFilterSection from './ArticleListFilterSection.vue';


export default {
  name: 'ArticleListFilter',
  components: { ArticleListFilterSection },
  props: {
    value: {
      type: Object,
      default: () => ({
        issues: [],
        authors: [],
        categories: [],
      }),
    },
    filterOptions: {
      type: Object,
      required: true,
    },
  },
};
</script>

