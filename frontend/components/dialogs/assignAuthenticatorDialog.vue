<template>
<v-dialog scrollable v-model="showDialog" transition="false" max-width="600px">
  <v-container fluid>  
    <v-card color="white">
        <v-card-title class="primary white--text">
          Assign authenticator
        </v-card-title>
        <v-card-text dense>
            <v-row align="center">
              <v-col cols="12" align="center">
                <v-subheader light> Authenticator code</v-subheader>
                <v-text-field
                  v-model="authenticatorCode"
                  solo
                  hide-details
                  :append-icon="passwordHidden ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="() => (passwordHidden = !passwordHidden)"
                  :type="passwordHidden ? 'password' : 'text'"                  
                  label="Authenticator code"
                  placeholder="00:00:00:00:00:00"
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
        <v-btn color="primary" @click="assign" >Assign</v-btn>
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
     userId: {
        default: ""
     },     
     show: {
        default: false
     },     
  },
  data: () => ({
    alert: false,
    passwordHidden: true,
    alertType: "error",
    authenticatorCode: "",
    errorText: "Please check the nodes identity"
  }),  
  components: {
    Editor,
  },
  computed: {
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
    cancel () {
        this.$emit('update:show', false)
    },
    assign () {
      let action = [actionBuilder.newAssignUserAuthenticatorAction('users', this.userId, this.authenticatorCode)];
      this.$store.dispatch('actions/emitActionRequest', action).then(response => {
        if(response.succeed == true) {
          this.$emit('update:show', false)
          let getViewAction = [actionBuilder.newGetViewAction("users", "authenticatorList"),
                                actionBuilder.newGetViewAction("users", "userAuthenticatorList")];
          this.$store.dispatch('actions/emitActionRequest', getViewAction);

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
      this.alert = false;
      this.authenticatorCode = "";
    }
  },
  mounted () {
      this.alert = false;
      this.authenticatorCode = "";
  }  
}
</script>
