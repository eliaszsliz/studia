<template>


            <v-card v-if="loaded"
                    :class="[$_settings.normalElevationClasses]"
                    width="100%"
                    >

                <v-layout
                    column
                    class="cardPadding primary_light_2"
                    >
                    <v-flex xs12>
                        <h1 class="display-3 ArticleDetail_Title ">
                            {{ article.title }}
                        </h1>

                        <div class="separator medium my-4"></div>
                    </v-flex>

                    <v-flex v-if="article.belongTo"
                            xs12
                            class="ArticleDetail_Issue pa-0">
                        <span class="body-1 secondary--text mr-2">
                          Wydanie
                        </span>

                        <router-link :to="issueLink"
                                     tag="span"
                                     class="primary--text headline cursor-pointer strong">
                            {{ article.belongTo.date }}
                        </router-link>
                    </v-flex>

                    <v-flex v-if="article.authors.length"
                            xs12
                            class="ArticleDetail_Authors text-xs-left pa-0 mt-3">
                        <span class="body-1 secondary--text mr-2">
                            {{ article.authors.length > 1 ? 'Autorzy' : 'Autor' }}
                        </span>

                        <article-detail-author-chip
                                v-for="(author) in article.authors"
                                :key="author.slug"
                                :author="author"
                                ></article-detail-author-chip>
                    </v-flex>
                </v-layout>

                <v-card-text
                        ref="articleTextRef"
                        class="cardPadding htmlContent ArticleDetail_Text"
                        v-html="articleText"
                        >
                </v-card-text>


                    <v-layout
                        v-if="article.categories.length"
                        >
                        <v-flex xs12 class="cardPadding pt-0">
                            <span class="body-1 secondary--text">
                                  Kategorie
                            </span>

                            <v-chip v-for="category in article.categories"
                                    :key="`cat-${category.id}`"
                                    class="px-3 py-1 cursor-pointer"
                                    color="primary"
                                    text-color="white"
                                    @click="goToArticleList('categories', category.id)"
                                    v-text="category.name"
                                    >
                            </v-chip>
                        </v-flex>
                    </v-layout>
            </v-card>

            <v-card v-else
                    :class="[$_settings.normalElevationClasses]"
                    width="100%"
            >
                <v-layout
                    column
                    class="cardPadding primary_light_2"
                    >
                    <v-flex xs12>
                        <v-skeleton-text
                                :width="60"
                                :style="{ fontSize: '42px' }"
                                dark
                                height="200%"
                        ></v-skeleton-text>

                        <div class="separator medium my-4"></div>
                    </v-flex>

                    <v-flex xs12
                            class="ArticleDetail_Issue pa-0">
                        <v-skeleton-text
                                v-for="(chip, index) in 4"
                                :key="index"
                                :width="6"
                                class="mr-3"
                                dark
                                height="200%"
                        ></v-skeleton-text>
                    </v-flex>
                </v-layout>

                <v-card-text class="cardPadding">
                    <v-skeleton-text
                                :width="{ min: 250, max: 600}"
                                height="200%"
                        ></v-skeleton-text>
                    <br>
                    <br>
                    <v-skeleton-text
                                :width="{ min: 250, max: 600}"
                                height="200%"
                        ></v-skeleton-text>

                </v-card-text>


            </v-card>

</template>

<script>
import PageMixin from './PageTitleMixin';
import ArticleDetailAuthorChip from './ArticleDetailAuthorChip.vue';
import VSkeletonText from './VSkeletonText.vue';

export default {
  name: 'ArticleDetail',
  components: { ArticleDetailAuthorChip, VSkeletonText },
  mixins: [PageMixin],
  data() {
    return {
      title: null,
      loaded: false,
      article: {
        categories: [],
        authors: [],
        belong_to: null,
      },
    };
  },

  computed: {
    articleText() {
      return this.article.body;
    },
    issueLink() {
      return {
        name: 'IssueList',
        params: {
          date: this.article.belongTo.date,
        },
      };
    },
  },

  created() {
    this.fetchItem()
      .then((article) => {
        this.article = article;
        this.loaded = true;
        // this.title = article.title
      })
      .then(() => {
        // remove empty paragraphs
        function isEmpty(s) {
          return !s.trim();
        }

        // eslint-disable-next-line
        for (const p of this.$refs.articleTextRef.children) {
          if (isEmpty(p.innerText) && p.childElementCount === 0) { p.style.display = 'none'; }
        }
      });
  },

  methods: {
    fetchItem() {
      const { slug } = this.$route.params;
      return this.$store.dispatch('fetchArticle', { slug });
    },
    goToArticleList(filterType, id) {
      this.$router.push({ name: 'ArticleList', query: { [filterType]: JSON.stringify([id]) } });
    },
  },
};
</script>


<style lang="stylus">
    @import "../stylus/variables.styl"

    #ArticleDetail_InfoCard
        &::before
            content: ''
            background-color: inherit
            height: 20%
            width: 100%
            position: absolute
            bottom: 90%
            left: 0
            z-index: 6

            border-top-left-radius: 50%
            border-top-right-radius: 50%

    .ArticleDetail_Title
        font-family: $serif-font-family

    .ArticleDetail_Issue
        & > *
            vertical-align middle

    .ArticleDetail_Authors
        flex-wrap: wrap
        text-align: center

        & > *
            display: inline

    .ArticleDetail_Text p:first-of-type::first-letter,  p.big-letter::first-letter
      display: block
      float: left
      font-size: 70px
      margin-top: 8px
      color: accent_color
      line-height: 1
      margin-right: 8px
      text-shadow: 1px 0 2px rgba(0, 0, 0, 0.2)

</style>
