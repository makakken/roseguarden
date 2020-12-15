<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <!---
                  <img src="../static/fabba_logo.png" alt="Roseguarden logo" width="120" height="120">
                  ---->
                  <h1 class="flex my-4 primary--text">Request action</h1>
                </div>
              <v-container>
                <v-row align="center" justify="center"> 
                  <v-col cols="3" lg="3" sm="3" xs="3"  align="center" justify="center">
                    <v-progress-circular
                      v-if="loading"
                      indeterminate
                      :size="60"
                      :width="5"
                      color="primary"
                    ></v-progress-circular>                    
                  <v-icon v-else-if="error" color="red" :size="60">mdi-close-circle-outline</v-icon>
                  <v-icon v-else color="green" :size="60">mdi-checkbox-marked-circle-outline</v-icon>
                  </v-col>
                  <v-col cols="8" lg="8" sm="8" xs="8" class="text-xs-center" align="left" justify="center">
                    <span class="text-left text-xs-center title"> {{info}} </span>
                  </v-col>                  
                </v-row>
              </v-container>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>

  import { mapState } from 'vuex';  
  import * as actionBuilder from '@/api/actionBuilder';
        
  export default {
    layout: 'default',
    props: ['actionhash'], 
    data: () => ({
      loading: true,
      error: true,
      info: ""
    }),
    computed: {
      ...mapState('actionlink', ['status', 'message']),
    },
    watch: {
      status(newValue, oldValue) {
        if (newValue === "success") {
          this.error = false;          
        } else {
          this.error = true;
        }
 
        this.info = this.message;
        this.loading = false;
      }
    },    
    mounted () {
      let runActionlinkAction = [actionBuilder.newRequestActionLinkAction(this.actionhash)];
      this.$store.dispatch('actions/emitActionRequest', runActionlinkAction);
      this.info = "Request action for" + this.actionhash;
    }
  };
</script>
<style scoped lang="css">
  #login {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>
