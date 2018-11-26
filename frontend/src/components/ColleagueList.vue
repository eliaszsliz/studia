<script>
import PersonListBase from './PersonListBase.vue';

export default {
  name: 'ColleagueList',
  extends: PersonListBase,
  data() {
    return {
      title: 'Współpracownicy',
    };
  },
  methods: {
    fetchItems() {
      return this.$store.dispatch('fetchColleagues');
    },
  },
};
</script>
