<template>
    <div>
        <person-list-element
                v-for="item in items"
                ref="itemsRef"
                :key="item.slug"
                v-bind.sync="item"
                class="mb-4"
        >
        </person-list-element>

        <person-list-dummy
                v-for="i in 4"
                v-show="!loaded"
                :key="i"
                class="mb-4"
        ></person-list-dummy>
    </div>
</template>

<script>
import PersonListElement from './PersonListElement.vue';
import PersonListDummy from './PersonListDummy.vue';
import ListMixin from './ListMixin';
import PageTitleMixin from './PageTitleMixin';

export default {
  components: { PersonListElement, PersonListDummy },
  mixins: [ListMixin, PageTitleMixin],
};
</script>
