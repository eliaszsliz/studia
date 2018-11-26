<template>
    <v-navigation-drawer
            id="TheSidebar"
            :value="value"
            :class="{'primary': true, open: value }"
            v-bind="$attrs"
            :width="$_settings.sidebarWidth"
            style="display: flex; flex-direction: column"
            app
            v-on="$listeners"
    >

        <v-toolbar
                :class="['transparent',
                     {'my-1': $vuetify.breakpoint.smAndDown},
                     {'my-4': $vuetify.breakpoint.mdAndUp}
                     ]"
                flat
        >
            <v-list
                    class="transparent"
            >
                <v-list-tile>
          <span
                  id="TheSidebar_HeaderText"
                  class="d-inline-block mx-auto white--text"
          >
            Studia Pigoniana
          </span>
                </v-list-tile>
            </v-list>
        </v-toolbar>

        <vue-scrollbar :style="{
                        width: '100%',
                        maxHeight: '100%',
                        flexGrow: 1
                      }" class="transparent">

            <v-list id="TheSidebar_List"
                    :class="['transparent py-2']"
            >
                <v-list-tile :to="{ name: 'Index' }"
                             active-class="active"
                             exact>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Strona główna
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile
                        :to="{ name: 'IssueList' }"
                        active-class="active"
                        exact>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Archiwum
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-divider
                        style="visibility:hidden;"
                        class="my-2"
                ></v-divider>

                <v-list-tile
                        v-if="$store.getters.currentLinkExists"
                        :to="$store.getters.getCurrentLink"
                        active-class="active"
                        exact
                >
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Aktualne wydanie
                        </v-list-tile-title>
                    </v-list-tile-content>


                </v-list-tile>

                <v-list-tile
                        v-if="$store.getters.nextLinkExists"
                        :to="$store.getters.getNextLink"
                        active-class="active"
                        exact>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Następne wydanie
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-divider
                        v-if="$store.getters.currentLinkExists || $store.getters.nextLinkExists"
                        style="visibility:hidden;"
                        class="my-2"
                ></v-divider>

                <v-list-tile
                        :to="{ name: 'EditorList' }"
                        active-class="active"
                >
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Redakcja
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile
                        :to="{ name: 'ColleagueList' }"
                        active-class="active"
                >
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Współpracownicy
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <v-list-tile
                        :to="{ name: 'NewsList' }"
                        active-class="active"
                >
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Z pracy redakcji
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>

                <template v-if="loaded">
                    <v-list-tile
                            v-for="page in $store.getters.getFlatPages"
                            :key="page.link"
                            :to="{ name: 'AdditionalPage', params: { pageLink: page.link } }"
                            active-class="active"
                    >
                        <v-list-tile-content>
                            <v-list-tile-title>
                                {{page.name}}
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <template v-else>
                    <v-list-tile
                            v-for="i in 2"
                            :key="i"
                    >
                        <v-list-tile-content>
                            <v-list-tile-title class="pl-2">
                                <v-skeleton-text
                                        :width="15"
                                        height="175%"
                                ></v-skeleton-text>
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>
            </v-list>

        </vue-scrollbar>

        <div
                id="TheSidebar_Footer"
                class="primary text-xs-center"
        >
            <v-layout row wrap justify-center>
                <v-flex xs12 align-center wrap>
                    <v-btn
                            :to="{ name: 'AuthorList' }"
                            flat
                    >
                        Autorzy
                    </v-btn>

                    <v-btn
                            :to="{ name: 'ArticleList' }"
                            flat
                    >
                        Artykuły
                    </v-btn>
                </v-flex>
                <!-- todo w footerze tez moga byc dodatkowe linki -->
            </v-layout>
        </div>
    </v-navigation-drawer>
</template>

<script>
import VSkeletonText from '@/components/VSkeletonText.vue';
import VueScrollbar from 'vue2-scrollbar';

export default {
  components: { VSkeletonText, VueScrollbar },
  props: {
    loaded: {
      type: Boolean,
      default: false,
      required: false,
    },
    value: {
      type: Boolean,
      default: true,
      required: true,
    },
  },
};
</script>

<style lang="stylus">
    @import "../stylus/variables.styl"

    #TheSidebar
        overflow: visible
        min-height: 100% !important // todo tylko na wiekszych urzadzaniach
        max-height: 150% !important // todo tylko na wiekszych uurzadzeniach

        &.open
            &::after
                position: absolute
                left: 91%
                top: -10%
                height: 120%
                width: 13%
                background-color: inherit
                border-top-right-radius: 100%
                border-bottom-right-radius: 100%

                z-index: 5
                content: ''

    #TheSidebar_HeaderText
        font-size: 32px !important
        font-family: 'Alex Brush', sans-serif

        line-height: 48px
        letter-spacing: 0.05em

    #TheSidebar_List
        font-family: $body-font-family
        text-transform: uppercase
        color: primary_color_light_1
        overflow: auto

        & > div > a
            padding-left: 0

            &:hover
                background-color: inherit

            & > div.v-list__tile__content
                height: 44px
                display: inline-block
                overflow: visible

                & > div.v-list__tile__title
                    line-height: 44px
                    border-top-right-radius: 22px
                    border-bottom-right-radius: 22px

                    font-size: 15px
                    letter-spacing: 0.1em

                    display: inline-block
                    width: auto
                    height: 100%

                    padding-left: 24px
                    padding-right: 32px

            &.active > div.v-list__tile__content
                & > div
                    background-color: primary_color_light_1
                    color: primary_color
                    transition: box-shadow 0.4s

    #TheSidebar_Footer
        position: absolute
        width: 100%
        bottom: 0

        & .v-btn
            color: primary_color_light_1
</style>
