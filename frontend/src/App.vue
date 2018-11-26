<template>
  <v-app>
    <the-sidebar
            v-model="sidebar"
            :loaded="loaded"
            :mobile-break-point="$_settings.mobileBreakPoint"
    ></the-sidebar>

    <site-header
            v-if="$store.getters.displayHeader"
            ></site-header>


  <v-content>
    <v-container
            :style="{ padding: $vuetify.breakpoint.smAndDown ? '6px' : null}"
            fluid>
      <v-layout row wrap>
        <v-flex id="AppContent_Wrapper"
                xs12
                sm11
                class="mx-auto">

          <v-fade-transition>
            <router-view ref="currentRouteInstance"></router-view>
          </v-fade-transition>

        </v-flex>
      </v-layout>
    </v-container>
  </v-content>

  <the-bottom-navigation
          @update:sidebar="sidebar = true"
          ></the-bottom-navigation>

  <v-btn
    v-if="$vuetify.breakpoint.mdOnly"
    :style="{
        left: sidebar ? `${$_settings.sidebarWidth}px` : '0',
        transition: 'left 0.2s linear',
        zIndex: 5,
        marginTop: '36px',
    }"
    :color="sidebar ? 'accent': 'primary'"
    fab
    fixed
    class="ml-3"
    @click="sidebar = !sidebar"
    >
        <v-icon v-if="sidebar">close</v-icon>
        <v-icon v-else>menu</v-icon>
  </v-btn>

</v-app>
</template>

<script>
import SiteHeader from '@/components/TheSiteHeader.vue';
import TheBottomNavigation from '@/components/TheBottomNavigation.vue';
import TheSidebar from '@/components/TheSidebar.vue';

export default {
  name: 'App',
  components: { SiteHeader, TheSidebar, TheBottomNavigation },
  data() {
    return {
      sidebar: window.innerWidth >= this.$_settings.mobileBreakPoint,
      loaded: false,
    };
  },
  created() {
    this.$store.dispatch('fetchSiteStuff')
      .then(() => {
        this.loaded = true;
      }, (data) => {
        console.log('nieloaded')
        console.log(data)
      });
  },
};
</script>

<style lang="stylus"></style>
