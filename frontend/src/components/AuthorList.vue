<script>
import PersonListBase from './PersonListBase.vue';

export default {
  name: 'AuthorList',
  extends: PersonListBase,
  data() {
    return {
      title: 'Autorzy',
    };
  },
  methods: {
    fetchItems() {
      return this.$store.dispatch('fetchAuthors');
    },
  },
};
</script>
