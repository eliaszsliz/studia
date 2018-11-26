<template>

    <div :style="{
           height: '48px',
           lineHeight: '48px',
           display: 'inline-block',
           marginLeft: '16px',
           marginRight: '16px'
          }"
          v-bind="$attrs"
           v-on="$listeners"
               >

          <v-tooltip
                  bottom
                  transition="fade-transition"
                  >
            <v-icon
                slot="activator"
                class="cursor-pointer"
                @click="copyLink"
                @copy="snackbar = true"
                >link</v-icon>

            <span>
                Skopiuj bezpośredni link
            </span>
        </v-tooltip>

        <slot>
            <v-snackbar
                      v-model="snackbar"
                      :timeout="2000"
                      color="success"
                      >
                  Skopiowano pomyślnie
                  <v-btn icon
                         flat
                         @click.native="snackbar = false">
                      <v-icon>close</v-icon>
                  </v-btn>
            </v-snackbar>
        </slot>
    </div>

</template>

<script>
import { HOSTNAME } from '../config';

export default {
  props: {
    link: {
      type: [String, Object],
      default: '',
    },
  },
  data() {
    return {
      snackbar: false,
    };
  },
  methods: {
    getLink() {
      return typeof this.link === 'object' ?
        this.$router.resolve(this.link).href :
        this.link;
    },
    copyLink() {
      const linkStr = HOSTNAME + this.getLink();
      this.$clipboard(linkStr);

      this.snackbar = true;
    },
  },
};
</script>
