<template>


        <v-layout column
                  fill-height
                  align-end
                  >

            <div style="flex-grow: 1">
                <div
                    class="title cursor-pointer TheIndexElement_Title"
                    @click="$router.push(moreLink)"
                    v-text="item.title"
                    ></div>

                <div class="secondary--text body-1 py-1">
                    {{ year }}
                </div>

                <div
                     class="text-justify TheIndexElement_Text"
                     v-html="truncatedItemBody"
                     ></div>
            </div>

            <div>
                <v-btn
                   :to="moreLink"
                   class="mr-0 btn--link"
                   flat
                   >
                    <span>Czytaj dalej</span>
                    <v-icon>arrow_right</v-icon>
                </v-btn>
            </div>

        </v-layout>

</template>

<script>
import { truncateHtml } from '@/utils';

export default {
  name: 'TheIndexNewsElement',
  props: {
    item: Object,
  },
  computed: {
    truncatedItemBody() {
      return this.item.body ? truncateHtml(this.item.body, 400) : '';
    },
    year() {
      const d = this.item.created_at.split('-');
      return `${d[2]} ${this.months[+d[1]]} ${d[0]}`;
    },
    moreLink() {
      return { name: 'NewsList', params: { id: this.item.id } };
    },
  },
  created() {
    this.months = new Array(12);
    this.months[0] = 'stycznia ';
    this.months[1] = 'lutego ';
    this.months[2] = 'marca ';
    this.months[3] = 'kwietnia ';
    this.months[4] = 'maja ';
    this.months[5] = 'czerwca ';
    this.months[6] = 'lipca ';
    this.months[7] = 'sierpnia ';
    this.months[8] = 'września ';
    this.months[9] = 'października ';
    this.months[10] = 'listopada ';
    this.months[11] = 'grudnia ';
  },
};
</script>
