<!--suppress ALL -->
<template>
    <v-layout wrap>

            <v-flex xs12 sm6
                    class='pa-3'>
              <the-index-issue-element
                      v-show="loaded"
                      :item="issues.current"
                      />
              <the-index-issue-dummy
                      v-show="!loaded"
                      />
            </v-flex>

            <v-flex xs12 sm6
                    class='pa-3'>
              <the-index-issue-element
                      v-show="loaded"
                      :item="issues.next"
                      />
              <the-index-issue-dummy
                      v-show="!loaded" />
            </v-flex>

        </v-layout>
</template>

<script>
import TheIndexIssueElement from '@/components/TheIndexIssueElement.vue';
import TheIndexIssueDummy from '@/components/TheIndexIssueDummy.vue';

export default {
  name: 'TheIndexIssueSection',
  components: { TheIndexIssueElement, TheIndexIssueDummy },
  props: {
    loaded: {
      required: true,
      type: Boolean,
    },
    issues: {
      type: Object,
    },
  },
};
</script>

<style lang="stylus">
    @import "../stylus/variables.styl";

    // .TheIndexCarouselItem
    //    min-height: 200px

    .TheIndexCarouselButton
        text-transform: uppercase
        box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 1px 5px 0px rgba(0,0,0,0.12);
        width: 2px
        padding-right: 16px
        padding-left: 8px
        padding-top: 8px
        padding-bottom: 8px

        word-wrap: break-word
        overflow: visible

        &:hover, &:active
            background-color whitesmoke

        &.to-next
            padding-right: 20px
            padding-left: 10px

        &.to-current
            padding-right: 18px
            padding-left: 12px

    #app .jumbotron__wrapper
        overflow: visible

    #app .carousel
        height: auto
        overflow visible
</style>
