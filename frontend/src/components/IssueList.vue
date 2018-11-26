<template>
    <div>
      <issue-list-element
              v-for="issue in items"
              ref="itemsRef"
              :key="issue.id"
              v-bind.sync="issue"
              class="mb-4">
          </issue-list-element>

      <issue-list-dummy v-for="i in 4"
                        v-if="!loaded"
                        :key="i"
                        class="mb-4"
              ></issue-list-dummy>
    </div>
</template>

<script>
import IssueListElement from './IssueListElement.vue';
import IssueListDummy from './IssueListDummy.vue';
import PageMixin from './PageTitleMixin';
import ListMixin from './ListMixin';

export default {
  name: 'IssueList',
  components: { IssueListElement, IssueListDummy },
  mixins: [PageMixin, ListMixin],
  data() {
    return {
      title: 'Lista numerów',
    };
  },

  created() {
    Object.assign(this.$options.scrollOptions, { routerPropName: 'date', itemProp: 'date' });
  },

  methods: {
    fetchItems() {
      return this.$store.dispatch('fetchIssues');
    },
  },
};
</script>

