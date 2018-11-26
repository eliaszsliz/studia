<template>

    <v-card ref="cardRef"
            :class="$_settings.normalElevationClasses">

        <div class="primary_light_2 cardPadding">
                    <div>
                        <v-skeleton-text
                                :width="30"
                                height="175%"
                                dark
                        ></v-skeleton-text>
                    </div>

                    <div class="mt-1">
                        <v-skeleton-text
                                :width="10"
                                height="175%"
                        ></v-skeleton-text>
                    </div>
                </div>

                <div class="cardPadding py-0"
                     style="position: relative; top: -3px;">
                    <div
                        class="separator small"
                        ></div>
                </div>


                <v-card-text
                        class="cardPadding htmlContent htmlContentSmaller"
                        >
                    <v-skeleton-text
                                :width="{min: 200, max: 400}"
                                height="175%"
                        ></v-skeleton-text>
                </v-card-text>


                    <div class="cardPadding pt-0"
                         >
                        <v-skeleton-text
                                v-for="(chip, index) in 4"
                                :key="index"
                                :width="6"
                                class="mr-3"
                                dark
                                height="200%"
                        ></v-skeleton-text>
                    </div>

            </v-card>
</template>

<script>
import VSkeletonText from './VSkeletonText.vue';

export default {
  components: { VSkeletonText },
};
</script>
