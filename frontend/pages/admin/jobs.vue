<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>
      <v-card>
        <v-card-title>
          <h3>
            Registered jobs
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details>
          </v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="jobs"
          :search="search">        
            <template v-slot:item.actions="{ item }">
              <v-btn
                v-if="item.need_parameters === 'No'"
                class="mx-2"
                fab
                dark
                x-small
                color="primary">              
                <v-icon
                  @click="triggerJob(item)"
                >
                  mdi-play
                </v-icon>
              </v-btn>                
            </template>          
            <template v-slot:item.id="{ item }">
              <v-chip :color="Util.getColorByString(item.name)" style="width : 300px; justify-content: center;">
                {{item.id}}
              </v-chip>              
            </template>          

        </v-data-table>
      </v-card>    
    </v-flex>
    <br/>
    <v-flex lg12 sm12 xs12>
      <v-card>
        <v-card-title>
          <h3>
            Job history
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search_jobHistory"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers_jobHistory"
          :items="jobs_jobHistory"
          :search="search_jobHistory">
          <template v-slot:item.state="{ item }">
            <v-chip
              :color="getColorFromState(item.state)"
              style="min-width: 120px; justify-content: center;" 
              dark
            >
              {{ item.state }}
            </v-chip>
          </template>
          <template v-slot:item.jobid="{ item }">
            <v-chip :color="Util.getColorByString(item.name)" style="width : 300px; justify-content: center;">
              {{item.jobid}}
            </v-chip>              
          </template>                    
        </v-data-table>
      </v-card>    
    </v-flex>
  </v-container>
</template>

<script>
  import axios from 'axios';
  import * as Util from "@/util";    
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser'; 
  import * as vuetifyHelper from '@/api/vuetifyHelper.js' 
  import { createHelpers } from 'vuex-map-fields';
    
  import VueAxios from 'vue-axios';
  import { mapState } from 'vuex';
 
  // The getter and mutation types are provided to the vue module
  // they must be the same as the function names used in the store.
  const { mapFields } = createHelpers({
    getterType: 'views/getView',
    mutationType: 'views/updateView',
  });

  export default {
    layout: "dashboard",
    components: {
    },
    beforeCreate() {
      this.Util = Util;
    },
    data: () => ({
      search: '',
      files: [],
      uploadProgress: 0,
      uploadStatus: "Upload ongoing",
      uploadIsRunning: false,
      dragover: false,
      search: '',
      headers: [
        {
          text: 'Job ID',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        { text: 'Name', value: 'calories' },
        { text: 'Type', value: 'calories' },
        { text: 'Verified', value: 'fat' },
        { text: 'Last action at', value: 'carbs' },
        { text: 'Actions', value: 'actions' },
      ],
      jobs: [],
      search_jobHistory: '',
      headers_jobHistory: [],
      jobs_jobHistory: []
    }),
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['access/accessUserList'] !== 'ready';
      },
    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['jobs/jobList'] === 'ready')  {
          this.jobs = viewParser.parseEntries('jobs/jobList', this.viewDictionary);
          this.headers = viewParser.parseHeader('jobs/jobList', this.viewDictionary);
          this.headers.unshift({ text: 'Actions',  value: 'actions', sortable: false});
        }  
        if(newValue['jobs/jobHistory'] === 'ready')  {
          this.jobs_jobHistory = viewParser.parseEntries('jobs/jobHistory', this.viewDictionary);
          this.headers_jobHistory = viewParser.parseHeader('jobs/jobHistory', this.viewDictionary);
        }  
      }
    },
    methods: {
      triggerJob (item) {
        console.log(item);
        if(item.need_parameters === "No") {
          console.log("Run job without parameters")
        }
        if(item.need_parameters === "Yes") {
          console.log("Run job with parameters")
        }
        let triggerJobAction = [actionBuilder.newTriggerJobAction(item.id)];
        this.$store.dispatch('actions/emitActionRequest', triggerJobAction).then(response => {
            console.log("JobTrigger - Succesfull", response)
        }, error => {
            console.log("JobTrigger - Failed", error)
        })     

      },
      getColorFromState (state) {
        if(state.toUpperCase() === "SUCCEED") {
          return "green"
        }
        
        if(state.toUpperCase() === "TRIGGERED") {
          return "orange"
        }

        return "red"
      }
    },      
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("jobs", "jobList"),
                            actionBuilder.newGetViewAction("jobs", "jobHistory")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);           
    }    
  }
</script>

<style scoped>

</style>
