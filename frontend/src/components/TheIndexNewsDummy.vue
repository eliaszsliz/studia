<template>

        <v-layout column
                  fill-height
                  align-end
                  >

            <div style="flex-grow: 1">
                <div>
                    <v-skeleton-text
                            :width="{ min: 24, max: 34}"
                             height="200%"
                            dark
                        ></v-skeleton-text>
                </div>

                <div class="py-1">
                    <v-skeleton-text
                            :width="8"
                            height="200%"
                        ></v-skeleton-text>
                </div>

                <div>
                    <v-skeleton-text
                            :width="{ min: 150, max: 220 }"
                            height="200%"
                        ></v-skeleton-text>
                </div>
            </div>

            <div class="mt-2">
                <v-skeleton-element
                        :width="'100px'"
                        height="25px"
                        dark />
            </div>

        </v-layout>

</template>

<script>
import VSkeletonText from './VSkeletonText.vue';
import VSkeletonElement from './VSkeletonElement.vue';

export default {
  components: { VSkeletonText, VSkeletonElement },
};
</script>
