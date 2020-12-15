<template>
  <v-container fluid fill-height>
    <v-row lg12 sm12 xs12>      
      <v-col cols="12" md="3">
        <v-card min-height="100%">
          <v-card-title>
            <h3>
              Spaces
            </h3>
            <v-spacer></v-spacer>
              <v-btn dark small color="success" @click="onAddSpace()">Add</v-btn>
          </v-card-title>
          
          <v-list dense single-line style="height: 100%" min-height="600px" class="overflow-y-auto">
            <v-list-item-group
              v-model="selected"
              mandatory
              active-class="blue--text"
            >
              <template v-for="(item, index) in spaces">
                <v-list-item :key="item.id" @click="selectSpace(item)">
                  <template v-slot:default="{ active, toggle }">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.name"></v-list-item-title>
                    </v-list-item-content>

                    <v-list-item-action>

                    </v-list-item-action>
                  </template>
                </v-list-item>


              </template>
            </v-list-item-group>
          </v-list>
        </v-card>  
      </v-col>

      <v-col v-if="!isMobile" cols="12" md="9">
        <v-card min-height="100%">
          <v-card-title>
            <h3>
              {{spaceName}}
            </h3>
            <v-spacer></v-spacer>
              <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveSpace()">Delete</v-btn>

          </v-card-title>
          <v-container lg12 sm12 xs12 style="height: 100%" class="overflow-y-auto">
            <AccessSpacesView :entrance_nodes="nodes" :space="selectedSpace"  v-on:cancel="cancelChange" v-on:submit="submitChange"/>            
          </v-container>
        </v-card>  
      </v-col>
    </v-row>


    <v-dialog
        v-model="mobileDialog"
        fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card width="100%">
          <v-toolbar dark color="primary">
            <v-btn icon dark @click="cancelChange()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>{{spaceName}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveSpace()">Delete</v-btn>
            <v-toolbar-items>
            </v-toolbar-items>
          </v-toolbar>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <AccessSpacesView :entrance_nodes="nodes" :space="selectedSpace" v-on:cancel="cancelChange" v-on:submit="submitChange" />            
          </v-container>
        </v-card>
    </v-dialog>  


    <v-dialog
        v-model="newSpaceDialog"
        hide-overlay
        transition="dialog-bottom-transition"
        width="90%"
      >
        <v-card>
            <v-toolbar dense dark color="primary">
              <v-toolbar-title>New space</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
              </v-toolbar-items>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                v-model="newSpaceName"
                label="Space name"
                single-line
                style="padding-left: 15px; padding-right: 15px"
                hide-details
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="error" @click="newSpaceDialog = false" >Cancel</v-btn>
              <v-btn color="primary" @click="requestNewSpace">Ok</v-btn>
            </v-card-actions>
          </v-card>
      </v-dialog>            
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser';
  import { createHelpers } from 'vuex-map-fields';

  import AccessSpacesView from "@/components/access/AccessSpacesView";

  import { mapState } from 'vuex';
 
  // The getter and mutation types are provided to the vue module
  // they must be the same as the function names used in the store.
  const { mapFields } = createHelpers({
    getterType: 'views/getView',
    mutationType: 'views/updateView',
  });

  export default {
    layout: "dashboard",
    components: { AccessSpacesView },
    data: () => ({
      newSpaceDialog: false,
      mobileDialog: false,
      loading: true,
      isMobile: false,
      spaceName: "Please select a space",
      validSelection: false,
      spaces: [],
      nodes: [],
      newSpaceName: "New space",
      validSelection: false,
      selected: null,
      selectedSpace: null,
    }),
    methods: {
      selectSpace(item) {
        this.validSelection = true;
        this.selectedSpace = {...item};
        this.spaceName = item.name;
        if(this.isMobile === true) {
          this.mobileDialog = true;
        }        
      },
      onResize () {
        this.isMobile = window.innerWidth < 950;
      },
      onRemoveSpace() {
        let removeViewEntryAction = [actionBuilder.newRemoveDataViewEntryAction("access", "spacesList", this.selectedSpace)];
        this.$store.dispatch('actions/emitActionRequest', removeViewEntryAction); 
        this.spaceName = "Please select a group";
      },
      submitChange() {
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "spacesList", this.selectedSpace)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);  
      },       
      cancelChange() {
        this.mobileDialog = false; 
        this.selectedSpace = {...this.spaces[this.selected]};
      },          
      onAddSpace() {
        this.newSpaceDialog = true;
        this.newSpaceName = "New space";
      },
      requestNewSpace() {
        let createViewEntryAction = [actionBuilder.newCreateViewAction("access", "spacesList", {'name' : this.newSpaceName})];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);  
        this.newSpaceDialog = false;
      },           
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['access/spacesList'] !== 'ready';
      },

    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['access/spacesList'] === 'ready')  {
          this.spaces = viewParser.parseEntries('access/spacesList', this.viewDictionary);
        } 
        if(newValue['nodes/nodeList'] === 'ready')  {
          this.nodes = viewParser.parseEntries('nodes/nodeList', this.viewDictionary);
        } 
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("access", "spacesList"), 
                            actionBuilder.newGetViewAction("nodes", "nodeList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
      this.onResize()
      window.addEventListener('resize', this.onResize, { passive: true })         
    }        
  }
</script>

<style scoped>


</style>
