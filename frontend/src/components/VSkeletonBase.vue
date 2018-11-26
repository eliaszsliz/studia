<template>
    <span :style="styles"
          v-bind="$attrs"
          v-on="$listeners"
          >{{content}}</span>
</template>

<script>
export default {
  name: 'VSkeletonBase',
  props: {
    extraStyle: {
      type: [String, Object, Array],
      default: () => {},
    },
    height: {
      type: [Number, String],
      default: 10,
    },
    dark: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
