<template>

        <v-layout column
                  fill-height
                  align-end
                >

            <div class="text-justify"
                 style="flex-grow: 1; width: 100%">

                <v-skeleton-element
                        :style="{ float: 'left' }"
                        width="100px"
                        height="130px"
                        class="mr-2 my-2"
                        ></v-skeleton-element>

                    <v-skeleton-text
                            :width="{ min: 15, max: 19}"
                            height="250%"
                            dark
                        ></v-skeleton-text>

                <br>

                    <v-skeleton-text
                            :width="{ min: 150, max: 200}"
                            height="175%"
                        ></v-skeleton-text>

            </div>

            <div class="py-2 text-xs-right"
                 style="margin-bottom: auto">

                <v-skeleton-element
                        :width="'80px'"
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
