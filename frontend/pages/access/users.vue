<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            User access
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          ref="table"
          :headers="headers"
          :items="users"
          :items-per-page="15"
          :loading="isLoading"
          :search="search"
          :sort-by="['id']"
          :sort-desc="[true]"         
          class="elevation-1"
          eager      
        >
          <!---
          <template v-slot:item.done="{ item }">
            <v-simple-checkbox :value="item.done === 'Yes'" disabled ></v-simple-checkbox>
          </template>
          ---->

          <template v-slot:item.access_group="props">
            <v-edit-dialog
              :return-value="props.item.access_group"
              
            > <span class="font-weight-bold font-italic">
              {{  groupIndex(props.item.access_group) }}
              </span>
              <template v-slot:input>
                <v-subheader>Access type</v-subheader>
                <v-select
                  :items="selectableGroups"
                  v-bind:value="props.item.access_group"
                  item-value="id"
                  item-text="name"                  
                  label="Access type"
                  dense
                  @change="val => updateAccessGroup(val, props.item)"
                  solo
                ></v-select>
              </template>
            </v-edit-dialog>
          </template>  


          <template v-slot:item.access_budget="props">
            <v-edit-dialog
              v-if="props.item.access_budget != -1"
              :return-value="props.item.access_budget"
              @close="updateBudget(props.item)"> 
              <span class="font-weight-bold font-italic">
                {{ props.item.access_budget }}
              </span>
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.access_budget"
                  label="Budget"
                  single-line
                  type="number"
                ></v-text-field>
              </template>
            </v-edit-dialog>
            <span v-else class="font-weight-bold font-italic">
              -
            </span>
          </template>

          <template v-slot:item.actions="{ item }">
            <v-tooltip bottom v-for="action in actions" v-bind:key="action.name">
              <template v-slot:activator="{ on }">
                <v-btn  v-if="item.hasOwnProperty(action.name)" :color="action.color" v-on="on" @click="requestViewAction('todoList', action.action, item)" :disabled="!item[action.name]" fab x-small :dark="item[action.name]">
                    <v-icon>{{action.icon}}</v-icon>
                </v-btn>
              </template>
              <span>{{action.tooltip}}</span>
            </v-tooltip>            
          </template>

          <template v-slot:item.access_start_date="props" ref="b">
            <v-edit-dialog
              :return-value="props.item.access_start_date"
            > <span class="font-weight-bold font-italic">
              {{  props.item.access_start_date }}
              </span>
              <template v-slot:input>
                <v-date-picker
                  v-model="props.item.access_start_date"
                  
                  @change="val => updateAccessStartDate(val, props.item)"
                ></v-date-picker>
              </template>
            </v-edit-dialog>
          </template>  

          <template v-slot:item.access_end_date="props" ref="b">
            <v-edit-dialog
              :return-value="props.item.access_end_date"
            > <span class="font-weight-bold font-italic">
              {{  props.item.access_end_date }}
              </span>
              <template v-slot:input>
                <v-date-picker
                  v-model="props.item.access_end_date"
                  
                  @change="val => updateAccessEndDate(val, props.item)"
                ></v-date-picker>
              </template>
            </v-edit-dialog>
          </template>  

        </v-data-table>
      </v-card>  
    </v-flex>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser'; 
  import * as vuetifyHelper from '@/api/vuetifyHelper.js' 
  import { createHelpers } from 'vuex-map-fields';

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
    data: () => ({
      search: '', 
      loading: false,
      search: '',
      headers: [],
      users: [],      
      groups: [],
      actions: [],
    }),
    methods: {
      updateAccessEndDate (val, item) {
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "accessUserList", item)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);
        vuetifyHelper.cancelTableDialogs(this.$refs, "table");
        console.log("updateAccessEndDate")

      },
      updateAccessStartDate (val, item) {
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "accessUserList", item)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);
        vuetifyHelper.cancelTableDialogs(this.$refs, "table");
        console.log("updateAccessStartDate")
      },         
      updateBudget (item) {
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "accessUserList", item)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);
        console.log("update budget")

      },    
      updateAccessGroup (val, item) {
        /*let createViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("account", "todoList", item)];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);*/
        console.log("updateAccessGroup")
        item.access_group = val;
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "accessUserList", item)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);
        vuetifyHelper.cancelTableDialogs(this.$refs, "table");
      },    
      requestViewAction(view, action, item) {

      },
      groupIndex(id) {
        // console.log("groupIndex", this.groups,  this.groups.length);
        for (var i = 0; i < this.groups.length; i++) {
          // console.log(this.groups[i].name, id , this.groups[i].id );
          if(this.groups[i].id == id)
            return this.groups[i].name;
        }
        return "-";
      },        
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['access/accessUserList'] !== 'ready';
      },
      selectableGroups: function() {
        let copy = [...this.groups];
        copy.unshift({'id': -1, 'name': '-'});
        return copy
      }

    },
    watch: {
      viewStates(newValue, oldValue) {

        if(newValue['access/accessUserList'] === 'ready')  {
          this.users = viewParser.parseEntries('access/accessUserList', this.viewDictionary);
          this.headers = viewParser.parseHeader('access/accessUserList', this.viewDictionary);

        } 
        if(newValue['access/accessGroupsList'] === 'ready')  {
          this.groups = viewParser.parseEntries('access/accessGroupsList', this.viewDictionary);
          console.log("ttttt", this.groups);
        } 

      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("access", "accessUserList"),
                                  actionBuilder.newGetViewAction("access", "accessGroupsList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);      
    }        
  }
</script>

<style scoped>

</style>
