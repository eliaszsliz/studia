<template>

    <list-element>

        <h2 slot="header"
            class="mb-3 text-xs-center"
        >
            <v-skeleton-text
                    :width="6"
                    height="250%"
                    dark
            ></v-skeleton-text>
        </h2>

        <v-skeleton-element slot="media"
                            width="170px"
                            height="220px"
                            class="mx-auto"
        ></v-skeleton-element>

        <template slot="content">
            <div class="mb-4">
                <v-skeleton-text
                        :width="{ min: 200, max: 300}"
                        height="175%"
                ></v-skeleton-text>
            </div>

            <div>
                <div class="IssueListElement_ArticlesSubheader
                                        body-1 secondary--text pl-2">
                    <v-skeleton-text
                                :width="20"
                                height="175%"
                        ></v-skeleton-text>
                </div>

                <ul class="IssueList_Articles mt-3">
                    <li v-for="(article, index) in 6"
                        :key="index"
                        class="IssueListElement_ArticlesElement mb-2"
                    >
                        <v-skeleton-text
                                :width="{ min: 25, max: 29}"
                                height="175%"
                        ></v-skeleton-text>

                    </li>
                </ul>
            </div>
        </template>
    </list-element>

</template>

<script>
import VSkeletonText from './VSkeletonText.vue';
import VSkeletonElement from './VSkeletonElement.vue';
import ListElement from './ListElement.vue';

export default {
  components: { ListElement, VSkeletonText, VSkeletonElement },
};
</script>
