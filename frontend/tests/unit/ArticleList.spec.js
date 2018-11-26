import Vuex from 'vuex';
import Vuetify from 'vuetify';
import { shallowMount, createLocalVue } from '@vue/test-utils';

import ArticleList from '../../src/components/ArticleList/ArticleList.vue';
import * as MOCK_DATA from './fetchArticles.mock';

const localVue = createLocalVue();
localVue.use(Vuex);
localVue.use(Vuetify);

describe('ArticleList', () => {
  let actions;
  let store;

  beforeEach(() => {
    actions = {
      fetchArticles: () => new Promise((resolve) => {
        resolve(MOCK_DATA.articles);
      }),
      setSiteHeader: () => true,
    };
    store = new Vuex.Store({
      actions,
    });
  });

  it('set items properly', () => {
    const component = shallowMount(ArticleList, { store, localVue }).vm;
    localVue.nextTick(() => {
      expect(component.items).toBe(MOCK_DATA.articles);
    });
  });

  function waitForAsyncActions(testFunction) {
    setTimeout(() => {
      localVue.nextTick(() => {
        testFunction();
      });
    }, 1);
  }

  it('set filter options issues properly', () => {
    const component = shallowMount(ArticleList, { store, localVue }).vm;

    waitForAsyncActions(() => {
      const mockedIssuesCount = MOCK_DATA.issues.length;
      expect(component.filterOptions.issues.length).toBe(mockedIssuesCount);
    });
  });

  it('set filter options authors properly', () => {
    const component = shallowMount(ArticleList, { store, localVue }).vm;

    waitForAsyncActions(() => {
      const mockedAuthorsCount = MOCK_DATA.authors.length;
      expect(component.filterOptions.authors.length).toBe(mockedAuthorsCount);
    });
  });

  it('set filter options categories properly', () => {
    const component = shallowMount(ArticleList, { store, localVue }).vm;

    waitForAsyncActions(() => {
      const mockedCategoriesCount = MOCK_DATA.categories.length;
      expect(component.filterOptions.categories.length).toBe(mockedCategoriesCount);
    });
  });

  it('set route query properly initialy ', () => {
    // const defaultMessage = 'default message';
    const mockedRoute = { query: {} };
    const component = shallowMount(ArticleList, {
      store,
      localVue,
      mocks: {
        $route: mockedRoute,
      },
    }).vm;

    localVue.nextTick(() => {
      expect(component.filterObject.issues.length).toBe(0);
      expect(component.filterObject.categories.length).toBe(0);
      expect(component.filterObject.authors.length).toBe(0);
      expect(component.$route.query).toEqual({});
    });
  });

  it('set route query when filter object change ', () => {
    // const defaultMessage = 'default message';
    const mockedRoute = { query: {} };
    const component = shallowMount(ArticleList, {
      store,
      localVue,
      mocks: {
        $route: mockedRoute,
        $router: {
          replace(o) {
            this.$route.query = o;
          },
        },
      },
    });

    waitForAsyncActions(() => {
      const selectedAuthor = MOCK_DATA.authors[1];
      component.setData({
        'filterObject.authors': [selectedAuthor],
      });

      expect(component.vm.$route.query.authors).toEqual([selectedAuthor.id]);
    });
  });

  it('set filter object properly initially ', () => {
    const selectedAuthors = [MOCK_DATA.authors[2], MOCK_DATA.authors[1]];
    const selectedIssues = [MOCK_DATA.issues[0]];
    const selectedCategories = [MOCK_DATA.categories[2]];

    const mockedRoute = {
      query: {
        authors: selectedAuthors.map(el => el.id),
        issues: selectedIssues.map(el => el.id),
        categories: selectedCategories.map(el => el.id),
      },
    };
    const component = shallowMount(ArticleList, {
      store,
      localVue,
      mocks: {
        $route: mockedRoute,
        $router: {
          replace(o) {
            this.$route.query = o;
          },
        },
      },
    }).vm;

    waitForAsyncActions(() => {
      expect(component.vm.filterObject).toEqual({
        authors: selectedAuthors,
        issues: selectedIssues,
        categories: selectedCategories,
      });
    });
  });
});
