export default {
  data() {
    return {
      title: null,
    };
  },
  methods: {
    updateHeader() {
      this.$store.dispatch('setSiteHeader', this.title);
    },
  },
  watch: {
    title() {
      this.updateHeader();
    },
  },
  created() {
    this.updateHeader();
  },
};
