<template>
    <v-card
            :class="[$_settings.normalElevationClasses, 'cardPadding']"
             v-bind="$attrs"
             style="transition: margin 700ms, box-shadow 700ms;"
             v-on="$listeners"
             >

        <v-layout
                row
                wrap
                justify-center
                class="px-0 pt-0"
                >
            <v-flex :order-xs1="imageFirst"
                    xs12
                    class="text-xs-center text-md-left">

                <slot name="header"></slot>
            </v-flex>

            <v-flex :style="{ width: 'auto', height: showMore ? '220px' : '220px' }"
                    :class="['text-xs-center', imageFirst ? 'my-1' : 'mb-4']"
                    :order-xs0="imageFirst"
                    xs12
                    md4
                    >
                <slot name="media"></slot>
            </v-flex>

            <v-flex xs12 md8
                    order-xs3>
                <slot name="content"></slot>
            </v-flex>
        </v-layout>

        <v-layout
                row
                class=""
                >
            <v-spacer></v-spacer>
            <v-card-actions
                    >
                <slot name="footer"></slot>
            </v-card-actions>

        </v-layout>
    </v-card>

</template>

<script>
export default {
  name: 'ListElement',
  props: {
    imageFirst: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      showMore: false,
    };
  },
};
</script>


<style lang="stylus">
    @import "../stylus/variables.styl"

    .ListElement_CopyLink
        height: 48px
        line-height: 48px
        position: absolute
        left: calc(50% + 64px)

    .ListElement_HideMore
        position: absolute
        right: card_padding
</style>
