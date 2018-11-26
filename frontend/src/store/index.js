/* eslint-disable */
import Vue from 'vue';
import Vuex from 'vuex';
import { ROOT_API } from '../config';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    issues: [],
    header: {
      text: '',
      disabled: false,
    },
    currentLink: {
      target: { name: 'Index' },
      disabled: true,
    },
    nextLink: {
      target: { name: 'Index' },
      disabled: true,
    },

    flatPages: [],

    sidebar: false

  },
  mutations: {
    SET_CURRENT_LINK(state, obj) {
      state.currentLink.target = obj;
      state.currentLink.disabled = false;
    },
    SET_NEXT_LINK(state, obj) {
      state.nextLink.target = obj;
      state.nextLink.disabled = false;
    },
    SET_ISSUES(state, arr) {
      state.issues = arr;
    },
    SET_SITE_HEADER(state, headerStr) {
      state.header.disabled = headerStr === undefined;
      state.header.text = headerStr;
    },
    SET_FLATPAGES(state, flatPagesArray = []) {
      state.flatPages = flatPagesArray;
    },

    OPEN_SIDEBAR(state) {
      state.sidebar = true
    },

    CLOSE_SIDEBAR(state) {
      state.sidebar = false
    }

  },
  actions: {
    setSiteHeader(context, headerStr) {
      context.commit('SET_SITE_HEADER', headerStr);
    },

    fetchSiteStuff({ commit }) {
      // todo przy wchodzeniu na dodatkowe strony wysyła dwa requesty

      return new Promise((resolve) => {
        const p = Vue.http.get('site', {
          before() {
            // abort previous request, if exists
            if (this.previousRequest) {
              this.request.abort();
            }

            // set previous request on Vue instance
            // this.previousRequest = request
          },
        }, )
          .then(response => {
            return response.data},
            rejected => {
              console.log('Uuuuuuuuuuuu')
              console.log(rejected)
            })
          .then((data) => {
            commit('SET_FLATPAGES', data.flatpages);
            commit('SET_CURRENT_LINK', data.issues.current);
            commit('SET_NEXT_LINK', data.issues.next);
            return data;
          });

        resolve(p);
      });
    },

    getIssueById: ({ state }, issueId) => {
      // eslint-disable-next-line
      for (const x of state.issues) {
        if (x.id === issueId) return x;
      }
      return null;
    },

    fetchCategories() {
      return Vue.http.get('categories').then(response => response.data);
    },

    fetchIssues({ state, commit }) {
      if (state.issues.length > 0) {
        return new Promise(((resolve) => {
          resolve(state.issues);
        }));
      }

      return Vue.http.get('issues')
        .then((response) => {
          commit('SET_ISSUES', response.data);
          return response;
        })
        .then(response => response.data.map((x) => {
          x.coverUrl = ROOT_API + x.cover_url;
          x.alternativeLink = x.alternative_link;
          x.shortDescription = x.short_description;

          x.articles.forEach((article) => {
            article.belongTo = article.belong_to;
          });
          return x;
        }));
    },

    fetchArticle({}, { slug, id }) {
      return Vue.http.get(`articles/${slug}`)
        .then(res => {
          res.data.belongTo = res.data.belong_to;
          return res.data
        });
    },

    fetchAuthors() {
      return Vue.http.get('authors')
        .then(res => res.data)
        .then(items => items.map((x) => {
          x.avatar = ROOT_API + x.avatar_url;
          x.shortDescription = x.short_description;
          x.fullName = x.full_name;
          return x;
        }));
      }
    ,
    fetchEditors() {
      return Vue.http.get('editors').then(res => res.data)
        .then(items => items.map((x) => {
          x.avatar = ROOT_API + x.avatar_url;
          x.shortDescription = x.short_description;
          x.fullName = x.full_name;
          x.role = x.function;
          return x;
        }));
    },
    fetchColleagues() {
      return Vue.http.get('colleagues').then(res => res.data)
        .then(items => items.map((x) => {
          x.avatar = ROOT_API + x.avatar_url;
          x.shortDescription = x.short_description;
          x.fullName = x.full_name;
          return x;
        }));
    },

    fetchAuthor({}, authorId) {
      return Vue.http.get(`authors/${authorId}`).then((res) => {
        res.data.avatar = ROOT_API + res.data.avatar_url;
        return res.data;
      });
    },
    fetchEditor({}, editorId) {
      return Vue.http.get(`editors/${editorId}`).then(res => res.data);
    },
    fetchColleague({}, colleagueId) {
      return Vue.http.get(`colleagues/${colleagueId}`).then(res => res.data);
    },

    async fetchArticleFilterStuff({ dispatch }) {
      return {
        // todo wywalic async/await
        authors: await dispatch('fetchAuthors'),
        issues: await dispatch('fetchIssues'),
        categories: await dispatch('fetchCategories'),
      };
    },

    fetchArticles() {
      return Vue.http.get('articles')
        .then(res => res.data)
        .then(items => items.map((article) => {
          article.belongTo = article.belong_to;

          article.authors.forEach((author) => {
            author.fullName = author.full_name;
          });

          return article
        }));
    },

    fetchNews({}, { categorySlug, page } = { page: 1 }) {
      const s = categorySlug ? { category: categorySlug, page } : { page };

      if (s.page.length === 0) {
        console.log('s.page. === 0', s.page)
        s.page = 1;
      }

      return Vue.http.get(
        'news', { params: s },
        {
          // use before callback
          before() {
            // abort previous request, if exists
            if (this.previousRequest) {
              this.request.abort();
            }

            // set previous request on Vue instance
            // this.previousRequest = request
          },

        },
      )
        .then(res => ({
          items: res.data.results,
          next: res.data.next == null ? null : +page + 1,
        }));
    },

    fetchHomePage() {
      return Vue.http.get('index')
        .then(res => res.data)
        .then((data) => {
          data.issues.current.coverUrl = ROOT_API + data.issues.current.cover_url;
          data.issues.next.coverUrl = ROOT_API + data.issues.next.cover_url;
          return data;
        });
    },

    getFlatPage({ }, { pageLink }) {
      return new Promise(((resolve) => {
        // const el = state.flatPages.find(function (o) {
        //  return o.link == pageLink
        // })
        resolve(Vue.http.get(`flatpages/${pageLink}`)
          .then(response => response.data));
      }));
    },

    setSidebar({ commit }, value) {
      value ?
        commit('OPEN_SIDEBAR'):
        commit('CLOSE_SIDEBAR')
    },

    openSidebar({ dispatch }) {
      dispatch('setSidebar', true)
    },

    closeSidebar({ dispatch }) {
      dispatch('setSidebar', false)
    },

    toggleSidebar({ dispatch, state }) {
      state.sidebar ?
        dispatch('openSidebar') :
        dispatch('closeSidebar')
    },



  },
  getters: {
    currentLinkExists: state => !state.currentLink.disabled,

    nextLinkExists: state => !state.nextLink.disabled,

    getCurrentLink: (state) => {
      if (state.currentLink.target.alternative_link) {
        return { path: state.currentLink.target.alternative_link };
      }
      return { name: 'IssueList', params: { date: state.currentLink.target.date } };
    },

    getNextLink: (state) => {
      if (state.nextLink.target.alternative_link) {
        return { path: state.nextLink.target.alternative_link };
      }
      return { name: 'IssueList', params: { date: state.nextLink.target.date } };
    },

    getFlatPages: state => state.flatPages,

    displayHeader: state => !state.header.disabled,

    headerText: state => state.header.text,

    showSidebar: state => state.sidebar

  },
  modules: {

  },
});

export default store;
