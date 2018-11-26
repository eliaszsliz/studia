<template>

        <list-element
                :image-first="$vuetify.breakpoint.smAndDown"
                @mouseover.native="showCopyLink = true"
                @mouseleave.native="showCopyLink = false"
                >

                <v-layout
                        slot="header"
                        :class="['justify-left', role ? 'mb-3' : '']"
                        style="height: 48px"
                        align-start
                        >
                        <v-flex offset-md4 xs12
                                column
                                style="flex-grow: 0;">
                            <div :style="role ? '' : 'line-height: 48px !important;'"
                                 class="headline"
                                 >
                                {{ fullName }}
                            </div>

                            <div v-if="role"
                                 class="subheading text--secondary"
                                 v-text="role"
                             ></div>
                        </v-flex>

                        <v-flex
                            style="margin-left: auto"
                            class="hidden-sm-and-down"
                            >
                            <v-copy-link
                                v-show="showCopyLink"
                                :link="link"
                                />
                        </v-flex>

                </v-layout>


            <v-card-media slot="media"
                          :src="avatar"
                          height="205px"
                          class="mb-5"
                          contain
                          ></v-card-media>


            <div slot="content"
                 class="htmlContent htmlContentSmaller"
                 v-html="computedDescription"
                 ></div>


            <template slot="footer">
                <v-spacer></v-spacer>
                <v-btn v-if="articles && articles.length > 0"
                       flat
                       color="primary"
                       class="pr-2"
                       @click="showArticles">
                            Artykuły autora
                            <v-icon class="ml-1">list</v-icon>
                </v-btn>
            </template>
        </list-element>

</template>

<script>
import { truncateHtml } from '@/utils';
import ListElement from './ListElement.vue';
import VCopyLink from './VCopyLink.vue';

export default {
  name: 'PersonListElement',
  components: { ListElement, VCopyLink },
  props: {
    id: Number,
    fullName: {
      type: String,
      default: '',
    },
    description: {
      type: String,
    },
    shortDescription: String,
    role: {
      type: String,
      required: false,
    },
    articles: Array,
    avatar: String,
  },
  data() {
    return {
      showCopyLink: false,
    };
  },
  computed: {
    computedDescription() {
      return this.shortDescription ?
        `<p>${this.shortDescription}</p>` :
        this.description; // truncateHtml(this.description, 600);
    },
    link() {
      return this.$router.resolve({
        params: { id: this.id },
      }).href;
    },
  },
  methods: {
    showArticles() {
      const authors = JSON.stringify([this.id]);
      this.$router.push({ name: 'ArticleList', query: { authors } });
    },
  },
};
</script>


<style lang="stylus">
    .card__text p
        text-align: justify

    .list-element-copylink
        margin-left: .5rem

</style>
