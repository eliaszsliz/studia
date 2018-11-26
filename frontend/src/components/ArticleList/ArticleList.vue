<template>
    <v-card :class="[ $_settings.normalElevationClasses]">

        <v-layout>
            <v-flex
                xs12
                class="text-xs-right"
                >
                <v-dialog
                    v-if="isMobile"
                    :value="showDialog"
                    fullscreen
                    >

                    <v-card>
                        <v-toolbar
                          color="primary"
                          class="mb-2"
                          dark
                          >
                          <v-toolbar-title>Filtrowanie artykułów</v-toolbar-title>
                          <v-spacer></v-spacer>
                          <v-btn icon
                            @click="showDialog = false">
                            <v-icon>close</v-icon>
                          </v-btn>
                        </v-toolbar>

                        <v-card-text>
                            <article-list-filter
                                v-model="filterObject"
                                :filter-options="filterOptions"
                                ></article-list-filter>
                        </v-card-text>

                        <v-btn
                            block
                            color="accent"
                            @click="showDialog = false"
                            >
                            <v-icon>search</v-icon>
                            Wyszukaj
                        </v-btn>
                    </v-card>
                </v-dialog>

                <template v-else>
                    <article-list-filter
                        v-model="filterObject"
                        :filter-options="filterOptions"
                        ></article-list-filter>
                    <v-divider></v-divider>
                </template>
            </v-flex>
        </v-layout>

        <v-layout class="mt-3 pb-4">
            <v-flex
                xs12
                >
                <v-layout
                    :class="['py-2',  $vuetify.breakpoint.smAndUp ? 'px-3' : 'px-2' ]"
                    align-center
                    >
                    <v-flex
                        :class="['body-2 text--secondary',
                                 $vuetify.breakpoint.smAndUp ? 'ma-2' : '']"
                        tag="h2"
                        >
                        Znalezione artykuły:
                    </v-flex>

                    <v-btn
                        v-if="isMobile"
                        :class="[ $vuetify.breakpoint.smAndUp ? 'ma-2' : 'ma-1']"
                        color="primary"
                        @click.stop="showDialog = true"
                        >
                        <v-icon>filter_list</v-icon>
                        Filtruj
                    </v-btn>
                </v-layout>

                <v-divider></v-divider>

                <v-data-table
                    :items="items"
                    :custom-filter="customFilter"
                    :filter="filter"
                    :search="filterObject"
                    :no-data-text="'Nie ma żadnych artykułów. Spróbuj odświeżyć stronę.'"
                    :no-results-text="'Nie znaleziono wyników spełniających te kryteria'"
                    :rows-per-page-items="[30, 50, 100, { text: 'Wszystkie', value: -1 }]"
                    :rows-per-page-text="'Wyników na stronę:'"
                    :headers="[
                        { text: 'Numer', value: 'belongTo.date', align: 'center', width: '90px' },
                        { text: 'Tytuł', value: 'title' }]"
                    >

                    <template
                        slot="items"
                        slot-scope="props"
                        >
                        <router-link
                            :to="getArticleLink({ slug: props.item.slug })"
                            tag="tr"
                            class="cursor-pointer">

                            <td
                              class="text-xs-center"
                              style="width: 90px"
                              >
                                {{ props.item.belongTo.date }}
                            </td>

                            <td>{{ props.item.title }}</td>
                        </router-link>
                    </template>

                    <template
                        slot="pageText"
                        slot-scope="props"
                        >
                      {{ props.pageStart }} - {{ props.pageStop }}  z  {{ props.itemsLength }}
                    </template>

                    <template slot="no-data">
                        <tr v-for="(_, index) in 7"
                            :key="'noData-' + index"
                            class="cursor-pointer text-xs-left">
                            <td class="text-xs-center"
                              style="width: 90px">
                                <v-skeleton-text
                                    :width="4"
                                    height="175%"
                                ></v-skeleton-text>
                            </td>
                            <td style="vertical-align: middle">
                                <v-skeleton-text
                                :width="{ min: 30, max: 45 }"
                                height="175%"
                            ></v-skeleton-text>
                            </td>
                        </tr>
                    </template>

                 </v-data-table>
            </v-flex>
        </v-layout>
    </v-card>
</template>

<script>
import PageMixin from '../PageTitleMixin';
import ArticleListFilter from './ArticleListFilter.vue';
import VSkeletonText from '../VSkeletonText.vue';

export default {
  name: 'ArticleList',
  components: { ArticleListFilter, VSkeletonText },
  mixins: [PageMixin],
  data() {
    return {
      title: 'Przeglądanie artykułów',
      items: [],
      filterObject: {
        issues: [],
        authors: [],
        categories: [],
      },
      filterOptions: { // todo zmienic mu nazwe
        issues: [],
        authors: [],
        categories: [],
      },
      showDialog: false,
    };
  },
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
  },
  watch: {
    filterObject: {
      deep: true,
      immediate: false,
      handler() {
        this.updateRouteQuery();
      },
    },
    '$route.query': {
      immediate: false,
      handler() {
        this.updateFilterObject();
      },
    },
  },
  created() {
    this.fetchItems()
      .then(
        (items) => {
          this.items = items;
          this.filterOptions = this.getFilterOptions();
          this.updateFilterObject();
        },
        () => {
          console.log('todo error '); // todo handle it
        },
      );
  },
  methods: {
    contains(arr, propValue, key = 'id') {
      return arr.some(o => o[key] === propValue);
    },

    getObject({ type, value, key = 'id' }) {
      return this.filterOptions[type].filter(obj => obj[key] === value)[0];
    },

    getObjects({ type, values, key = 'id' }) {
      return this.filterOptions[type].filter(obj => values.includes(obj[key]));
    },

    getArticleLink(params) {
      return {
        name: 'ArticleDetail', params,
      };
    },

    fetchItems() {
      return this.$store.dispatch('fetchArticles');
    },

    updateRouteQuery() {
      const query = {};

      Object.keys(this.filterObject).forEach((key) => {
        const arrOfIDs = this.filterObject[key].map(el => el.id);
        if (arrOfIDs.length > 0) query[key] = JSON.stringify(arrOfIDs);
      });
      this.$router.replace({ query });
    },

    updateFilterObject() {
      const updatedFilterObject = {};
      Object.keys(this.$route.query).forEach((key) => {
        const arrOfIDs = JSON.parse(this.$route.query[key]);
        updatedFilterObject[key] = this.getObjects({
          type: key,
          values: arrOfIDs,
        });
      });

      this.filterObject = {
        ...{
          issues: [],
          authors: [],
          categories: [],
        },
        ...updatedFilterObject,
      };
    },

    getFilterOptions() {
      const result = {
        issues: [],
        authors: [],
        categories: [],
      };
      this.items.forEach((article) => {
        if (!this.contains(result.issues, article.belongTo.date, 'date')) {
          result.issues.push({
            ...article.belongTo,
            label: `${article.belongTo.date}`,
          });
        }

        article.authors.forEach((author) => {
          if (!this.contains(result.authors, author.id)) {
            result.authors.push({
              ...author,
              label: `${author.fullName}`,
            });
          }
        });

        article.categories.forEach((category) => {
          if (!this.contains(result.categories, category.id)) {
            result.categories.push({
              ...category,
              label: `${category.name}`,
            });
          }
        });
      });
      return result;
    },

    filter(article) {
      let result = true;

      if (this.filterObject.issues.length > 0) {
        result = this.contains(this.filterObject.issues, article.belongTo.id);
      }

      if (result && this.filterObject.authors.length > 0) {
        result = article.authors.some(authorObj => this.contains(this.filterObject.authors, authorObj.id));
      }

      if (result && this.filterObject.categories.length > 0) {
        result = article.authors.some(categoryObj => this.contains(this.filterObject.categories, categoryObj.id));
      }

      return result;
    },

    customFilter(items, search, filter) {
      return items.filter(filter);
    },

    goToArticle(params) {
      this.$router.push({ name: 'ArticleDetail', params });
    },
  },
};
</script>
