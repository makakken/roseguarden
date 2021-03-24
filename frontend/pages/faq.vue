<template>
  <v-container fluid>
    <v-row dense justify="center">
      <v-col cols="12" height="100%">
        <v-card height="100%" v-for="introductionItem in introduction" :key="introduction.id">
          <v-card-title>
            <h3>
              {{introductionItem.title}}
            </h3>
            <p>
              {{introductionItem.content}}
            </p>
          </v-card-title>
          <v-card-text dense>

            <template>
              <v-expansion-panels focusable>
                <v-expansion-panel v-for="faqItem in faqList" :key="faqItem.id">
                  <v-expansion-panel-header>
                    {{faqItem.title}}
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    {{faqItem.content}}
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </template>

          </v-card-text>
        </v-card>
        <br/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import Vue from 'vue';
import { codemirror } from 'vue-codemirror';
import { mapState } from 'vuex';
import moment from 'moment';


// import { GenericNode } from '@/nodes/generic'

import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);


export default {
  layout: "dashboard",
  components: {
  },
  data() {
    return {
      introduction: null,
      faqList: null
    }
  },
  methods: {
  },
  watch: {
  },
  computed: {
  },
  created () {
  },
  mounted () {
    axios.get('https://strapi.pukoo.de/faqs')
    .then(response => {
      this.introduction = response.data[0].content;
      this.faqList = response.data[1].content;
    });
  }

}
</script>
