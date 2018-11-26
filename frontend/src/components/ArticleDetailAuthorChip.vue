<template>

        <v-menu v-model="showDialog"
                :content-class="'ArticleDetailAuthorChip_Card'"
                :close-on-content-click="false"
                :max-width="450"
                :nudge-left="50"
                offset-x
                transition="scale-transition"
                >
            <v-chip slot="activator"
                    class="px-3 py-1"
                    color="primary"
                    text-color="white"
                    @click.native="showDialog = true, fetchItem()"
                    v-text="author.full_name"
            ></v-chip>

            <v-card>
                <v-list>
                    <v-list-tile avatar>
                        <v-list-tile-avatar
                                tile
                                color="grey"
                                class="ma-0">
                          <img :src="author.avatar">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                          <v-list-tile-title>
                              {{ author.fullName }}
                          </v-list-tile-title>

                          <v-list-tile-sub-title>
                              {{ author.function }}
                          </v-list-tile-sub-title>
                        </v-list-tile-content>

                        <v-list-tile-action>
                          <v-btn
                            icon
                            @click="showDialog = false"
                            >
                              <v-icon>close</v-icon>
                          </v-btn>
                        </v-list-tile-action>
                  </v-list-tile>
                </v-list>

                <template v-if="loaded">
                    <v-card-text class="py-1">
                        <div class="text-justify"
                             v-html="description"
                             ></div>
                    </v-card-text>

                    <v-card-actions right>
                        <v-spacer></v-spacer>
                        <v-btn v-if="author.articles.length > 0"
                               :to="{ name: 'ArticleList', query: { authors: JSON.stringify([author.id]) } }"
                               flat
                               color="primary">
                            <v-icon class="mr-1">list</v-icon> Artykuły autora
                        </v-btn>
                        <v-btn v-if="author.computedDescription"
                               :to="{ name: 'AuthorList', params: { id: author.id } }"
                               flat
                               @click="goToMore">
                             <v-icon class="mr-1">person</v-icon> Więcej
                        </v-btn>
                    </v-card-actions>
                </template>

                <template v-else>
                    <v-progress-linear
                        v-model="loadingVal"
                        class="my-0"
                        height="3"
                        ></v-progress-linear>
                    <v-card-title>
                       <div>
                           <v-skeleton-text
                               :width="120"
                                height="175%"
                          ></v-skeleton-text>
                       </div>
                    </v-card-title>
                </template>
            </v-card>
        </v-menu>

</template>

<script>
import VSkeletonText from '@/components/VSkeletonText.vue';

export default {
  name: 'ArticleDetailAuthorChip',
  components: { VSkeletonText },
  props: {
    author: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      showDialog: false,
      loaded: false,
      loadingVal: 0,
      loadingInterval: {},
    };
  },
  computed: {
    computedDescription() {
      function closeTags(html) {
        const div = document.createElement('div');
        div.innerHTML = html;
        return (div.innerHTML);
      }

      const len = this.author.computedDescription.length;
      if (len > 400) {
        return closeTags(`${this.author.computedDescription.substring(0, 400)}...`);
      }
      return this.author.computedDescription;
    },
  },
  methods: {
    fetchItem() {
      if (!this.loaded) {
        this.loadingInterval = setInterval(() => {
          this.loadingVal += 5;

          if (this.loadingVal > 100) {
            clearInterval(this.loadingInterval);
          }
        }, 8);
      }

      this.$store.dispatch('fetchAuthor', this.author.id)
        .then((res) => {
          this.author = res;
          this.loaded = true;
        });
    },
  },
};
</script>
