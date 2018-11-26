/* eslint-disable */
// import '@babel/polyfill';
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Vuex from 'vuex';
import Clipboard from 'v-clipboard';

import axios from 'axios';
import VueAxios from 'vue-axios';

import {THEME_SETTINGS, CSS_SETTINGS, ROOT_API} from './config';

import store from './store/index';
import router from './router/index';

import App from './App.vue';

import './stylus/main.styl'

// copy link to list element
Vue.use(Clipboard);

import ScrollBar from 'vue2-scrollbar'
import '../node_modules/vue2-scrollbar/dist/style/vue2-scrollbar.css'


/*
import Vuetify from 'vuetify'
import VApp from 'vuetify/es5/components/VApp'
import VNavigationDrawer from 'vuetify/es5/components/VNavigationDrawer'
import VBtn from 'vuetify/es5/components/VBtn'
import VFooter from 'vuetify/es5/components/VFooter'
import VList from 'vuetify/es5/components/VList'
*/

import {
    Vuetify,
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    transitions,

    VCard,
    VSubheader,
    VDivider,

    VChip,
    VDialog,
    VMenu,
    VProgressLinear,
    VDataTable,
    VCheckbox,
    VSnackbar,
    VBottomNav,

   VSelect,

    VTooltip,
} from 'vuetify'
import { Ripple } from 'vuetify/es5/directives'
// import 'vuetify/src/stylus/app.styl'


Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    transitions,

    VCard,
    VSubheader,
    VDivider,

    VChip,
    VDialog,
    VMenu,
    VProgressLinear,
    VDataTable,
    VCheckbox,
    VSnackbar,
    VBottomNav,

    VSelect,

    VTooltip,
  },
  directives: {
    Ripple,
  },
  theme: THEME_SETTINGS,
});

Vue.config.productionTip = false;
Vue.prototype.$_settings = CSS_SETTINGS

const axiosInstance = axios.create({
  baseURL: `${ROOT_API}/api`,
  headers: { Accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', }
});

Vue.use(VueAxios, axiosInstance);
Vue.http = axiosInstance;


// Vue.prototype.$http = axios;
// Vue.http.options.root = 'http://localhost:8000/api/';

Vue.use(Vuex);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store,
});
