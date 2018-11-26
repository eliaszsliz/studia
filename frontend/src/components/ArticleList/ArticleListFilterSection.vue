<template>
    <div>
        <div class="d-flex px-4 py-0 primary">
            <div style="flex-basis: 40px !important; flex-grow: 0 !important;">
                <v-checkbox
                        :value="getValue"
                        :indeterminate="indeterminate"
                        :label="headerText"
                        color="primary_color_light_1"
                        light
                        hide-details
                        class="my-2 ArticleListFilterTable_HeaderCheckbox"
                        @click="toggleAll"
                ></v-checkbox>
            </div>
        </div>

        <v-divider></v-divider>

        <vue-scrollbar
                v-if="$vuetify.breakpoint.mdAndUp"
                :style="{ height: '220px' }">
            <v-data-table
                :value="value"
                :items="items"
                :item-key="itemKey"
                no-data-text=""
                disable-initial-sort
                hide-actions
                hide-headers
                @input="handleChange"
                >

                <template
                    slot="items"
                    slot-scope="props"
                    >
                        <tr
                            :active="props.selected"
                            class="cursor-pointer"
                            @click="props.selected = !props.selected"
                            >

                            <td style="width: 40px; vertical-align: middle">
                                <v-checkbox
                                  :input-value="props.selected"
                                  :label="props.item.label"
                                  hide-details
                                  primary
                                ></v-checkbox>
                            </td>
                        </tr>
                </template>

                <template slot="no-data">
                    <tr v-for="(_, index) in 3"
                        :key="'noData-' + index"
                        class="cursor-pointer text-xs-left">
                        <td style="width: 40px; vertical-align: middle">
                            <v-skeleton-text
                            :width="{ min: 12, max: 20 }"
                            height="175%"
                        ></v-skeleton-text>
                        </td>
                    </tr>
                </template>
            </v-data-table>
        </vue-scrollbar>

        <v-select
          v-else
          :items="items"
          :value="value"
          :label="'Wybierz z listy'"
          item-text="label"
          return-object
          multiple
          max-height="400"
          persistent-hint
          class="mx-4"
          single-line
          @input="handleChange"
        ></v-select>
    </div>
</template>

<script>
import VueScrollbar from 'vue2-scrollbar';
import VSkeletonText from '../VSkeletonText.vue';

export default {
  name: 'ArticleListFilterSection',
  components: { VueScrollbar, VSkeletonText },
  props: {
    value: {
      type: Array,
      default: () => [],
    },
    items: {
      type: Array,
      required: true,
    },
    itemKey: {
      type: String,
      required: true,
    },
    headerText: {
      type: String,
      default: '',
    },
    sortProp: {
      type: String,
      default: 'label', // todo sortowanie powinno byc po nazwisku
    },
  },

  computed: {
    getValue() {
      return this.value.length === this.items.length;
    },
    indeterminate() {
      return this.value.length > 0 && this.items.length !== this.value.length;
    },
  },

  methods: {
    handleChange(value) {
      this.$emit('input', value);
    },
    toggleAll() {
      if (this.indeterminate === true || this.getValue) {
        this.handleChange([]);
      } else {
        this.handleChange(this.items);
      }
    },
  },
};
</script>

<style lang="stylus">
@require "../../stylus/variables.styl"

#app
    .no-messages
        .v-input__slot
            margin-bottom: 0

        .v-messages
            display none

    .ArticleListFilterTable_HeaderCheckbox
        & .v-label, & .v-icon
            color: primary_color_light_1

</style>

<!--
<v-flex xs4>
            <v-data-table
                v-model="selected.issues"
                :items="filterOptions.issues"
                item-key="id"
                hide-actions
                select-all
                class="scrollable-data-table">

                <template slot="headers"
                          slot-scope="props">
                      <tr class="dense">
                        <th>
                          <v-checkbox
                            :input-value="props.all"
                            :indeterminate="props.indeterminate"
                            primary
                            hide-details
                            @click.native="toggleAll('issues')"
                          ></v-checkbox>
                        </th>

                        <th class="px-0">
                            <v-subheader class="px-2">Numery</v-subheader>
                        </th>
                      </tr>
                </template>

                <template slot="items"
                          slot-scope="props">
                  <tr :active="props.selected"
                      class="dense"
                      @click="props.selected = !props.selected">
                      <td class="px-3"
                          style="width: 50px">
                          <v-checkbox
                            :input-value="props.selected"
                            primary
                            hide-details
                          ></v-checkbox>
                      </td>
                      <td class="px-2">
                          {{ props.item.date }}
                      </td>
                  </tr>
                </template>
            </v-data-table>
        </v-flex>
-->
