<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            Todos
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
          :headers="headers"
          :items="todos"
          :items-per-page="15"
          :loading="isLoading"
          :search="search"
          :sort-by="['id']"
          :sort-desc="[true]"         
          class="elevation-1"        
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-spacer></v-spacer>
              <v-btn dark color="success" @click="onAddTodo()">Add</v-btn>
            </v-toolbar>
          </template> 

          <template v-slot:item.done="{ item }">
            <v-simple-checkbox :value="item.done === 'Yes'" disabled ></v-simple-checkbox>
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

          <template v-slot:item.description="props">
            <v-edit-dialog
              :return-value.sync="props.item.description"
              @save="update(props.item)"
            > {{ props.item.description }}
              <template v-slot:input>
                <v-text-field
                  v-model="props.item.description"
                  label="Edit"
                  single-line
                  counter
                ></v-text-field>
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
      loading: true,
      search: '',
      headers: [],
      todos: [],
      actions: [],
    }),
    methods: {
      updateDone (item) {
        console.log('Toggle', item);
      },
      update (item) {
        let createViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("account", "todoList", item)];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);    
        console.log('Data saved', item);
      },     
      requestViewAction(view, action, item) {

      },
      parseEntries(view) {
        if(this.viewDictionary.hasOwnProperty(view)) {
          return this.viewDictionary[view].entries;
        } else {
          return [];
        }
      },
      parseHeader(view) {
        let headers = [];
        let actionExist = false;
        if(this.viewDictionary.hasOwnProperty(view)) {
          this.viewDictionary[view].properties.forEach(function (item, index) {
            if(item.type === 'action') {
              if(actionExist === false) {
                headers.push({ text: 'Actions',  value: 'actions', tooltip: item.label, action: item.action, name: item.name });
              }
              actionExist = true;
            } else {
              headers.push({ text: item.label,  value: item.name });
            }
          });        
          return headers;
        } else {
          return [];
        }
      },      
      onAddTodo() {
        let createViewEntryAction = [actionBuilder.newCreateViewAction("account", "todoList")];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);    
      },
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['account/todoList'] !== 'ready';
      },

    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['account/todoList'] === 'ready')  {
          this.todos = this.parseEntries('account/todoList');
          this.headers = this.parseHeader('account/todoList');
        } 
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("account", "todoList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);      
    }        
  }
</script>

<style scoped>

</style>
