<template>
  <div id="pageDashboard" >
    <v-container grid-list-xl fluid>
      <h4>
        Undefined section {{group}} / {{section}}.
      </h4>
      <i class="far fa-tired"></i>

    </v-container> 
   </div>
</template>

<script>


import { mapState } from 'vuex';

import Vue from 'vue'
  export default {
    layout: "dashboard",
    props: ['section','group'], 
    data () {
      return {
        name: 'test',
        component: null,
      }
    },
    mounted() {
      /*
      console.log(this.page);
      this.$nextTick(() => {
        // idea from https://medium.com/scrumpy/dynamic-component-templates-with-vue-js-d9236ab183bb
        // further ideas
        // use https://github.com/alexjoverm/v-runtime-template
        this.loader()
            .then(() => {
              this.component = () => this.loader()
            })
            .catch(() => {
              this.component = () => import('@/pages/test.vue')
            })
      }) 
      */
    },
    computed: {
        ...mapState('app', ['page']),
    },

  }
</script>

<style scoped>

</style>

