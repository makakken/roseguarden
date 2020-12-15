<template>
<v-dialog scrollable v-model="showDialog" transition="false" max-width="600px">
  <v-container fluid>  
    <v-card color="white">
        <v-card-title class="primary white--text">
          Authorize node
        </v-card-title>
        <v-card-text dense>
            <v-row dense align="center">
              <v-col cols="12">
                <v-subheader light>Footprint</v-subheader>
                <h3 light align="center">
                  {{identificationValue.fingerprint}}
                </h3>
              </v-col>
            </v-row>
            <v-row dense align="center">
              <v-col cols="6">
                <v-subheader light>Workspace</v-subheader>
                <h3 light align="center">
                  {{identificationValue.workspace}}
                </h3>
              </v-col>
              <v-col cols="6">
                <v-subheader light>Class</v-subheader>
                <h3 light align="center">
                  {{identificationValue.classid}}
                </h3>
              </v-col>
            </v-row>            
            <v-row dense align="center">
              <v-col cols="12">
                <v-subheader light> Identification</v-subheader>
                <Editor ref="editor" readOnly lineNumbers v-model="identificationValue.identification" height="400px"></Editor>
              </v-col>
            </v-row>
            <v-row align="center">
              <v-col cols="12" align="center">
                <v-subheader light> Authentification secret</v-subheader>
                <v-text-field
                  v-model="authorizationPassword"
                  solo
                  hide-details
                  :append-icon="hide ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (hide = !hide)"
                  :type="hide ? 'password' : 'text'"                  
                  label="Authentification secret"
                  placeholder="enter the node specific authentification secret"
                ></v-text-field>
              </v-col>
            </v-row>            
            <v-row dense align="center">
              <v-col cols="12">
                <v-alert v-model="alert" dismissible :type="alertType" dense>
                  {{errorText}} 
                </v-alert>
              </v-col>
            </v-row>
        </v-card-text>
      <v-card-actions dense class="ma-1">
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="cancel" >Cancel</v-btn>
        <v-btn color="primary" @click="authorize" >Authorize</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</v-dialog>
</template>

<script>


import Editor from '@/components/widgets/Editor'
import * as actionBuilder from '@/api/actionBuilder';

export default {
  props: {
     value: {
       default: ""
     },
     show: {
        default: false
     },     
     identification: {
       default: {}
     },
     node: {
       default: {}
     }     
  },
  data: () => ({
    identity: "{}\n",
    alert: true,
    hide: true,
    alertType: "warning",
    authorizationPassword: "",
    errorText: "Please check the nodes identity"
  }),  
  components: {
    Editor,
  },
  computed: {
    identificationValue: function() {
      let i = {};
      if(this.identification.hasOwnProperty('fingerprint')) {
        i.fingerprint = this.identification.fingerprint;
      } else {
        i.fingerprint = "";
      }

      if(this.identification.hasOwnProperty('classid')) {
        i.classid = this.identification.classid;
      } else {
        i.classid = "";
      }      

      if(this.identification.hasOwnProperty('workspace')) {
        i.workspace = this.identification.workspace;
      } else {
        i.workspace = "";
      }      

      if(this.identification.hasOwnProperty('identification')) {
        i.identification = this.identification.identification;
      } else {
        i.identification = "";
      }        
      return i;
    },
    showDialog: {
      get () {    
        return this.show
      },
      set (value) {
        this.$emit('update:show', false)         
      }      
    },
  },  
  methods: {
    checkInput() {
      return true;
    },
    cancel () {
        this.identity = this.value;
        this.$emit('update:show', false)
    },
    authorize () {
      let request_data =  {}
      request_data.id =  this.node.id
      request_data.authentification =  this.authorizationPassword

      let getIdentificationAction = [actionBuilder.newExecuteDataViewActionAction('nodes', "nodeList", "requestAuthorization", request_data)];
      this.$store.dispatch('actions/emitActionRequest', getIdentificationAction).then(response => {
        console.log("mmmmmmm", response);
        if(response.succeed == true) {
          this.$emit('update:show', false)
        } else {
          this.errorText = response.message;
          this.alertType = "error";
          this.alert = true;
        }
      }, error => {
        this.dispatch('notifications/pushNotification', [error, "error"]);
      })     
    }    
  },
  watch: {
    show(newValue) {
      let setTimeoutObject = setTimeout(() => {
        this.alertType = "warning";
        this.errorText = "Please check the nodes identity";
        this.alert = true;
        this.authorizationPassword = "";

      }, 1000);      

    }
  },
  mounted () {
    this.identity = this.value;
  }  
}
</script>
