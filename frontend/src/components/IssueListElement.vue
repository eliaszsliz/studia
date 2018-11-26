<template>
        <list-element
                @mouseover.native="showCopyLink = true"
                @mouseleave.native="showCopyLink = false"
                >

                    <h2 slot="header"
                          class="display-2 cursor-default IssueListElement_Header strong mb-3 text-xs-center"
                          >
                        {{ date }}

                        <v-copy-link
                            v-show="showCopyLink"
                            :link="{ name: 'IssueList', params: { date } }"
                            style="position: absolute; left: calc(50% + 48px); top: 24px; "
                            ></v-copy-link>
                    </h2>

                    <img  slot="media"
                          :src="coverUrl"
                          height="100%"
                          style="transition: all 700ms"
                          />

                    <template slot="content">
                        <div v-if="computedDescription"
                             class="htmlContent htmlContentSmaller mb-5"
                             v-html="computedDescription"
                             ></div>

                        <div v-if="articles.length">
                            <div class="IssueListElement_ArticlesSubheader
                                        body-1 secondary--text pl-2">
                                Artykuły z tego numeru:
                            </div>

                            <ul class="IssueList_Articles mt-3">
                                <router-link
                                        v-for="article in articles"
                                        :key="article.id"
                                        :to="getArticleLink({ slug: article.slug})"
                                        tag="li"
                                        class="subheading cursor-pointer mb-3
                                               IssueListElement_ArticlesElement"
                                        >

                                        — {{ article.title | removeDot }}
                                </router-link>
                            </ul>

                            <div class="text-xs-right caption secondary--text mx-2">
                                ({{articles.length}})
                            </div>
                        </div>
                    </template>

                    <template
                            v-if="alternativeLink"
                            slot="footer"
                            >
                        <v-btn flat
                               class="btn--link"
                               @click.native="$router.push(alternativeLink)"
                               >
                            <span>Więcej</span>
                            <v-icon>arrow_right</v-icon>
                        </v-btn>
                    </template>
        </list-element>

</template>

<script>
import ListElement from './ListElement.vue';
import VCopyLink from './VCopyLink.vue';

export default {
  name: 'IssueListElement',
  components: { ListElement, VCopyLink },
  filters: {
    removeDot(value) {
      return value[value.length - 1] === '.' ?
        value.slice(0, value.length - 1) :
        value;
    },
  },
  props: {
    date: {
      type: [String, Number],
      default: '',
    },
    description: {
      type: String,
      default: '',
    },
    shortDescription: {
      type: String,
      default: '',
    },
    articles: {
      type: Array,
      default: () => [],
    },
    coverUrl: {
      type: String,
      default: null,
    },
    alternativeLink: {
      type: String,
      required: false,
      default: null,
    },
  },
  data() {
    return {
      showCopyLink: false,
    };
  },
  computed: {
    computedDescription() {
      if (this.description.length) {
        return this.description;
      } else if (!this.description.length && !this.articles.length && this.shortDescription.length) { return `<p> ${this.shortDescription} </p>`; }

      return '';
    },
    link() {
      return this.$router.resolve({
        params: { date: this.date },
      }).href;
    },
  },
  methods: {
    getArticleLink(params) {
      return {
        name: 'ArticleDetail', params,
      };
    },
  },
};
</script>


<style lang="stylus">
    @import "../stylus/variables.styl"

    .IssueListElement_Header
        font-family: $body-font-family
        font-weight: 700 !important

    .IssueList_Articles
        font-family: $serif-font-family

    .IssueListElement_ArticlesElement
        list-style: none

        & > span
            background-image: linear-gradient(120deg, primary_color_light_1 0%, primary_color_light_2 100%)
            background-repeat: no-repeat
            background-size: 95% 0
            background-position: right 88%
            transition: background-size 0.1s ease-in

            &:hover
                background-size: calc( 100% - 16px ) 40% // 88%

    .IssueListElement_ArticlesSubheader
        vertical-align: middle
        border-left: 6px solid accent_color
        text-transform: uppercase

</style>
