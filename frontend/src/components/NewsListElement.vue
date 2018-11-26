<template>

        <v-card ref="cardRef"
                :class="$_settings.normalElevationClasses">
                <div class="primary_light_2 cardPadding">
                    <div
                        class="NewsListElement_Title"
                        >{{item.title}}</div>

                    <div
                        class="subheading secondary--text mt-1 NewsListElement_Date"
                        v-text="item.created_at"
                        ></div>
                </div>

                <div class="cardPadding py-0"
                     style="position: relative; top: -3px;">
                    <div
                        class="separator small"
                        ></div>
                </div>


                <v-card-text
                        class="cardPadding htmlContent htmlContentSmaller"
                        v-html="item.body"
                        ></v-card-text>

                <template v-if="item.categories.length">
                    <div class="cardPadding pt-0"
                         >
                        <span class="body-1 secondary--text mr-2">
                              Kategorie
                        </span>

                        <v-chip v-for="category in item.categories"
                                :key="'cat'+category.id"
                                :category="category"
                                :class="[$route.params.categorySlug === category.slug ?
                                            $_settings.activeElevationClasses :
                                            '',
                                        'cursor-pointer primary primary_light--text' ]"
                                @click.native="$emit('update:category', category)"
                                >
                            {{ category.name }}
                        </v-chip>
                    </div>
                </template>
            </v-card>

</template>

<script>
export default {
  name: 'NewsListElement',
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
};
</script>


<style lang="stylus">
    @import "../stylus/variables.styl"

    .NewsListElement_Title
        font-family: $serif-font-family
        line-height: 1.8
        font-size: 24px


    // todo sprawdzic czy tak ma byc
    .NewsListElement_Date
        font-family: $body-font-family
</style>
