<template>
  <v-container fluid fill-height>
    <v-row lg12 sm12 xs12>      
      <v-col cols="12" md="3">
        <v-card min-height="650px">
          <v-card-title>
            <h3>
              Access groups
            </h3>
            <v-spacer></v-spacer>
              <v-btn dark small color="success" @click="onAddGroup()">Add</v-btn>
          </v-card-title>
          
          <div v-if="isLoading" class="text--center">
            <v-progress-circular
              :size="70"
              :width="7"
              style="margin-top: 42%; margin-left: 42%;"
              color="primary"
              indeterminate
            ></v-progress-circular>
          </div>
          <v-list v-else dense single-line style="height: 100%" class="overflow-y-auto">
            <v-list-item-group
              v-model="selected"
              mandatory
              active-class="blue--text"
            >
              <template v-for="(item, index) in groups">
                <v-list-item :key="item.id" @click="selectGroup(item)">
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
        <v-card height="650px"  class="overflow-y-auto">
          <v-card-title>
            <h3>
              {{groupName}}
            </h3>
            <v-spacer></v-spacer>
            <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveGroup()">Delete</v-btn>

          </v-card-title>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <AccessGroupView  :groupProps="groupsProps" :spaces="spaces"
                                      :group="selectedGroup" cancel v-on:submit="submitChange" v-on:cancel="cancelChange"/>            
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
            <v-toolbar-title>{{groupName}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveGroup()">Delete</v-btn>
            <v-toolbar-items>
            </v-toolbar-items>
          </v-toolbar>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <AccessGroupView :groupProps="groupsProps" :spaces="spaces" :group="selectedGroup"  v-on:cancel="cancelChange" v-on:submit="submitChange" />            
          </v-container>
        </v-card>
    </v-dialog>  

    <v-dialog
        v-model="newGroupDialog"
        hide-overlay
        transition="dialog-bottom-transition"
        width="90%"
      >
        <v-card>
            <v-toolbar dense dark color="primary">
              <v-toolbar-title>New group</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
              </v-toolbar-items>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                v-model="newGroupName"
                label="Group name"
                single-line
                style="padding-left: 15px; padding-right: 15px"
                hide-details
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="error" @click="newGroupDialog = false" >Cancel</v-btn>
              <v-btn color="primary" @click="requestNewGroup">Ok</v-btn>
            </v-card-actions>
          </v-card>
      </v-dialog>        
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser';

  import AccessGroupView from "@/components/access/AccessGroupView";

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
    components: { AccessGroupView },
    data: () => ({
      mobileDialog: false,
      newGroupDialog: false,
      newGroupName: "",
      loading: true,
      isMobile: false,
      groupName: "Please select a group",
      validSelection: false,
      actions: [],
      selected: null,
      selectedGroup: null,
      groups: [],
      spaces: [],
      groupsProps: [],
      accessTypeItems: [],
    }),
    methods: {
      selectGroup(item) {
        this.validSelection = true;
        this.selectedGroup = {...item};
        this.groupName = item.name;
        if(this.isMobile === true) {
          this.mobileDialog = true;
        }        
      },
      onResize () {
        this.isMobile = window.innerWidth < 950;
      },
      onRemoveGroup() {
        let removeViewEntryAction = [actionBuilder.newRemoveDataViewEntryAction("access", "accessGroupsList", this.selectedGroup)];
        this.$store.dispatch('actions/emitActionRequest', removeViewEntryAction);  
        this.groupName = "Please select a group";
      },
      requestNewGroup() {
        let createViewEntryAction = [actionBuilder.newCreateViewAction("access", "accessGroupsList", {'name' : this.newGroupName})];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);  
        this.newGroupDialog = false;
      },      
      onAddGroup() {
        this.newGroupDialog = true;
        this.newGroupName = "New group";
      },
      submitChange() {
        console.log("submitChange", this.selectedGroup);
        let createViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("access", "accessGroupsList", this.selectedGroup)];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);  

      },
      cancelChange() {
        console.log("cancelChange", this.selected);
        this.mobileDialog = false; 
        this.selectedGroup = {...this.groups[this.selected]};
      }
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['access/accessGroupsList'] !== 'ready';
      },
    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['access/accessGroupsList'] === 'ready')  {
          this.groups = viewParser.parseEntries('access/accessGroupsList', this.viewDictionary);
          this.groupsProps = viewParser.parseProperties('access/accessGroupsList', this.viewDictionary);

          if(this.selected !== null) {
            this.selectGroup(this.groups[this.selected]);
          }

        }
        if(newValue['access/spacesList'] === 'ready')  {
          this.spaces = viewParser.parseEntries('access/spacesList', this.viewDictionary);
        }
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("access", "accessGroupsList"), 
                            actionBuilder.newGetViewAction("access", "spacesList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
      this.onResize()
      window.addEventListener('resize', this.onResize, { passive: true })         
    }        
  }
</script>

<style scoped>


</style>
