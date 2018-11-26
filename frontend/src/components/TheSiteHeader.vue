<template>
    <v-toolbar
            v-if="siteHeaderText"
            id="siteHeader"
            app
            absolute
            extension-height="64px"
            extended
            flat
            >

        <div id="siteHeaderInnerWrapper">
              <div id="siteHeaderGradientOverlay"></div>
              <div id="siteHeaderBackground"></div>
        </div>

      <v-toolbar-title
              :style="{ whiteSpace: 'normal',
                        paddingTop: '64px',
                        paddingBottom: '0px',
                        zIndex: 105 }"
              class="mx-auto">
        <h1
            id="siteHeaderText"
            :class="[
            'primary--text header-font', {
                small: siteHeaderText.length > 40,
                mobile: $vuetify.breakpoint.smAndDown
            }]">
            {{ siteHeaderText }}
        </h1>
      </v-toolbar-title>

    </v-toolbar>
</template>

<script>
export default {
  name: 'SiteHeader',
  computed: {
    siteHeaderText() {
      return this.$store.getters.displayHeader ?
        this.$store.getters.headerText :
        null;
    },
  },
  created() {},
};

</script>

<style lang="stylus">
@import "../stylus/variables.styl"

    #siteHeader
        z-index: 1
        background-color: $primary-gradient

    #siteHeaderText
        font-family: $serif-font-family
        font-size: 36px
        text-align: center
        letter-spacing: 0.1em
        cursor: default

        &::first-letter
            font-size: 42px

        &.small
            font-size: 16px

            &::first-letter
                font-size: 18px

        &.mobile
            font-size: 24px

            &::first-letter
                font-size: 30px

    #siteHeaderInnerWrapper
        position: absolute
        top: 0
        left: 0
        width: 100%
        height: 100%
        margin: 0

        $display-breakpoints.md-and-up
            left: 300px

    #siteHeaderGradientOverlay
        background: $primary-gradient
        opacity: .4
        position: absolute
        height: 100%
        width: 100%
        z-index: 102

    #siteHeaderBackground
        box-shadow: 0 -10px 10px -10px rgba(41, 111, 110, .08) inset, 0px -8px 14px -11px rgba(0, 0, 0, .12) inset, 0px -5px 10px 0px rgba(0, 0, 0, .04) inset
        background: url("../../public/header-bg.png")
        background-size: 60px
        position: absolute
        height: 100%
        width: 100%
        z-index: 101

    #siteHeaderToolbar.toolbar:before
        position: absolute
        background-color: red
        width: 100%
        height: 100%
        content: ''

</style>

