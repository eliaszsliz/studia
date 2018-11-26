export default {
  data() {
    return {
      loaded: false,
      items: [],
    };
  },
  computed: {
    indexOfItemFromRoute() {
      const options = this.$options.scrollOptions;
      const propFromRoute = this.$route[options.routerPropType][options.routerPropName];
      return this.items.findIndex(el =>
      // match issue with year from route
        propFromRoute === el[options.itemProp]);
    },
  },
  methods: {
    scrollToElement(index) {
      const options = this.$options.scrollOptions.vuetifyOptions;
      // todo ma sprawdzac czy refs sie juz pojawiły
      // todo zmienic na promise przy nastepnej wersji vuetify
      this.$vuetify.goTo(this.$refs.itemsRef[index], options);

      return new Promise((resolve) => {
        setTimeout(resolve, options.duration);
      });
    },
    $_indexOfItemFromRouteWatchHandler() { // todo rename
      const targetIndex = this.indexOfItemFromRoute;
      if (targetIndex > 0) {
        this.$nextTick(() => {
          this.items[targetIndex].showMore = true;
          this.scrollToElement(targetIndex);
        });
      } else {
        this.$vuetify.goTo(0, this.$options.scrollOptions.vuetifyOptions);
        this.$nextTick(() => {
          this.items.forEach((el) => {
            el.showMore = false;
          });
        });
      }
    },
    fillContent() {
      return new Promise((resolve) => {
        this.fetchItems()
          .then((data) => {
            this.items = data.map((el) => {
              this.$set(el, 'showMore', false);
              return el;
            });
          })
          .then(() => { this.loaded = true; })
          .then(() => { resolve(); });
      });
    },
  },
  watch: {
    indexOfItemFromRoute() {
      this.$_indexOfItemFromRouteWatchHandler();
    },
    loaded(newVal) {
      if (newVal) this.$_indexOfItemFromRouteWatchHandler();
    },
  },
  created() {
    this.fillContent();
  },
  scrollOptions: {
    routerPropType: 'params',
    routerPropName: 'id',
    item: 'item',
    itemProp: 'id',
    targetRef: 'cardRef',
    vuetifyOptions: {
      duration: 500,
      offset: -0,
      easing: 'easeOutCubic',
    },
  },
};
