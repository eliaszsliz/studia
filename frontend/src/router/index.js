import Vue from 'vue';
import Router from 'vue-router';
import TheIndex from '@/components/TheIndex';
import IssueList from '@/components/IssueList';
import AdditionalPage from '@/components/AdditionalPage';

import ColleagueList from '@/components/ColleagueList';
import AuthorList from '@/components/AuthorList';
import EditorList from '@/components/EditorList';

import NewsList from '@/components/NewsList';
import ArticleDetail from '@/components/ArticleDetail';
import ArticleList from '@/components/ArticleList/ArticleList';

import Http404 from '@/components/Http404';


Vue.use(Router);

export default new Router({
  mode: 'history', // https://router.vuejs.org/en/essentials/history-mode.html
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { x: 0, y: 0 };
  },
  routes: [
    { path: '/', name: 'Index', component: TheIndex },

    { path: '/wspolpracownicy/:id?', name: 'ColleagueList', component: ColleagueList },
    { path: '/autorzy/:id?', name: 'AuthorList', component: AuthorList },
    { path: '/redaktorzy/:id?', name: 'EditorList', component: EditorList },
    { path: '/archiwum/:date?', name: 'IssueList', component: IssueList },
    { path: '/newsy/:categorySlug?', name: 'NewsList', component: NewsList }, //todo zmienic to na slug

    { path: '/artykuly/:slug', name: 'ArticleDetail', component: ArticleDetail },
    { path: '/artykuly', name: 'ArticleList', component: ArticleList },

    { path: '/dodatkowe/:pageLink', name: 'AdditionalPage', component: AdditionalPage },
    { path: '*', component: Http404 }
  ],
});
