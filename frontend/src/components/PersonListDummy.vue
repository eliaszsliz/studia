<template>
    <list-element>

        <v-layout
                slot="header"
                class="justify-left mb-3"
                style="height: 48px"
                align-start
        >
            <v-flex offset-md4 xs12
                    column
                    style="flex-grow: 0;">
                <div class="headline">
                    <v-skeleton-text
                            :width="{ min: 12, max: 15 }"
                            dark
                            height="200%"
                    ></v-skeleton-text>
                </div>
            </v-flex>
        </v-layout>

        <v-skeleton-element slot="media"
                            width="170px"
                            height="220px"
                            class="mx-auto"
        ></v-skeleton-element>


        <div slot="content"
             class="htmlContent htmlContentSmaller"
        >

            <v-skeleton-text
                    :width="{ min: 125, max: 250}"
                    height="175%"
            ></v-skeleton-text>

        </div>

    </list-element>


</template>

<script>
  import VSkeletonText from './VSkeletonText.vue';
  import VSkeletonElement from './VSkeletonElement.vue';
  import ListElement from './ListElement.vue';

  export default {
    components: {VSkeletonText, VSkeletonElement, ListElement},
  };
</script>
