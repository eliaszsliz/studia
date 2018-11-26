<script>
import SkeletonBase from './VSkeletonBase.vue';

export default {
  name: 'VSkeletonText',
  extends: SkeletonBase,
  props: {
    symbol: {
      type: [String, Number],
      default: 'X',
    },
    width: {
      type: [Number, Object, Array],
      default() {
        return {
          min: 10,
          max: 30,
        };
      },
    },
  },
  computed: {
    computedHeight() {
      return typeof this.height === 'number' ? `${this.height}px` : this.height;
    },
    getContentLength() {
      if (Array.isArray(this.width)) {
        return Math.floor(Math.random() * (this.width[1] - this.width[0] + 1)) + this.width[0];
      }

      switch (typeof this.width) {
        case 'number':
          return this.width;
        case 'object':
          return Math.floor(Math.random() * (this.width.max - this.width.min + 1)) + this.width.min;
        default:
          return this.width;
      }
    },
    content() {
      let result = '';
      for (let i = 0; i < this.getContentLength; i += 1) result += `${this.symbol} `;
      return result;
    },
    styles() {
      return Object.assign({
        display: 'inline',
        userSelect: 'none',
        cursor: 'default',
        backgroundColor: this.dark ? 'rgba(158, 158, 158, .85)' : 'rgba(238, 238, 238, .85)',
        color: 'transparent',
        lineHeight: this.computedHeight,
      }, this.extraStyle);
    },
  },
};
</script>
