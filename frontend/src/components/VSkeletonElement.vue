<script>
import SkeletonBase from './VSkeletonBase.vue';

export default {
  name: 'VSkeletonElement',
  extends: SkeletonBase,
  props: {
    width: {
      type: [Number, String],
      default: '100%',
    },
    height: {
      default: '150px',
    },
    content: {
      type: String,
      default: '',
    },
    rounded: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    computedWidth() {
      return typeof this.width === 'number' ? `${this.width}px` : this.width;
    },

    computedHeight() {
      return typeof this.height === 'number' ? `${this.height}px` : this.height;
    },

    computedBorderRadius() {
      if (this.rounded) {
        return `calc(${this.computedHeight / 2}`;
      }
      return null;
    },

    styles() {
      return Object.assign({
        cursor: 'default',
        display: 'block',
        backgroundColor: this.dark ? '#9e9e9e' : '#eee',
        color: this.dark ? '#9e9e9e' : '#eee',
        width: this.computedWidth,
        height: this.computedHeight,
        borderRadius: this.computedBorderRadius,
      }, this.extraStyle);
    },
  },
};
</script>
