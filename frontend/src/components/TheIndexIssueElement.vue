<template>
        <v-layout
                  column
                  fill-height
                  align-end
                >

            <div class="text-justify"
                 style="flex-grow: 1">
                <router-link
                        :to="moreLink">
                    <img
                     :src="item.coverUrl"
                     :alt="item.date"
                     height="130px"
                     class="mr-3 mb-2 mt-3 cursor-pointer"
                     style="float: left; height: 130px; min-width: 80px"
                     />
                </router-link>

              <router-link
                      :to="moreLink"
                      class="title cursor-pointer TheIndexElement_Title d-inline-block mb-1"
                      tag="h3"
                      >
                  {{ title }} -
                  <span class="secondary--text">
                      {{ item.date }}
                  </span>
              </router-link>

              <p class="mb-0 TheIndexElement_Text">
                  {{ computedDescription }}
              </p>
            </div>

            <div class="py-2 text-xs-right"
                 style="margin-bottom: auto">
                 <v-btn
                   :to="moreLink"
                   flat
                   class="mr-0 btn--link"
                   >
                   <span>Więcej</span>
                   <v-icon>arrow_right</v-icon>
                </v-btn>
            </div>
        </v-layout>

</template>


<script>
export default {
  name: 'TheIndexIssueElement',
  props: {
    item: Object,
  },
  computed: {
    computedDescription() {
      return this.item.short_description || '';
    },
    title() {
      return this.item.current ? 'Aktualny numer' : 'Następny numer';
    },
    moreLink() {
      return { name: 'IssueList', params: { issueYear: this.item.date } };
    },
  },
};
</script>
