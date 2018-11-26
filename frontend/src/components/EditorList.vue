<script>
import PersonListBase from './PersonListBase.vue';

export default {
  name: 'EditorList',
  extends: PersonListBase,
  data() {
    return {
      title: 'Redakcja',
    };
  },
  methods: {
    fetchItems() {
      return this.$store.dispatch('fetchEditors');
    },
  },
};
</script>
