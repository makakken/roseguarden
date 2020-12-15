<template>
    <v-container>
      <v-row
      >
        <v-col cols="12" lg="12" sm="12" xs="12" align="center">
          This is a test dashboard for specific actions. 
        </v-col>
        <v-col cols="3" lg="3" sm="3" xs="3"/>
        <v-col cols="6" lg="6" sm="6" xs="6">
          <v-text-field
            label="Router"
            single-line
            v-model="route"
          ></v-text-field>
        </v-col>
        <v-col cols="3" lg="3" sm="3" xs="3">
          <v-btn dark color="error" @click="onRoute()">Go</v-btn>
        </v-col>
        <v-col cols="12" lg="12" sm="12" xs="12" align="center">
          <div class="text-xs-center">          
            <v-btn dark color="primary" @click="onNotification()">Notify</v-btn>
          </div>
        </v-col>
        <v-col cols="12" lg="3" sm="3" xs="12" align="center">
          <div class="text-xs-center">          
            <v-btn  color="primary" @click="onTestLogin('roseguarden@fabba.space', 'test1234')">Login (User)</v-btn>
          </div>
        </v-col>           
        <v-col cols="12" lg="3" sm="3" xs="12" align="center">
          <div class="text-xs-center">          
            <v-btn dark color="primary" @click="onTestLogin('super@fabba.space', 'test1234')">Login (Supervisor)</v-btn>
          </div>
        </v-col>           
        <v-col cols="12" lg="3" sm="3" xs="12" align="center">
          <div class="text-xs-center">          
            <v-btn dark color="primary" @click="onTestLogin('admin@fabba.space', 'admin1234')">Login (Admin)</v-btn>
          </div>
        </v-col>           
        <v-col cols="12" lg="3" sm="3" xs="12" align="center">
          <div class="text-xs-center">          
            <v-btn dark color="primary" @click="onTestLogout()">Logout</v-btn>
          </div>
        </v-col>
        <v-col cols="3" lg="4" sm="4"/>
        <v-col cols="6" lg="4" sm="4" align="center">
          <v-text-field
            label="user-email"
            single-line
            v-model="newuser"
          ></v-text-field>
        </v-col>
        <v-col cols="12" lg="4" sm="4" align="center">
          <div class="text-xs-center">          
            <v-btn dark color="primary" @click="onTestRegistration()">Register Testuser</v-btn>
          </div>
        </v-col>

      </v-row>
    </v-container>
</template>

<script>

  import Vue from 'vue';
  import EChart from '@/components/chart/echartwrap';
  import VWidget from '@/components/VWidget';
  import Material from 'vuetify/es5/util/colors';
  import BoxChart from '@/components/widgets/chart/BoxChart';
  import { codemirror } from 'vue-codemirror';
  import { mapState } from 'vuex';

  import * as actionBuilder from '@/api/actionBuilder';

// require styles
  import 'codemirror/lib/codemirror.css';
  import 'codemirror/theme/mbo.css';

  import axios from 'axios';
  import VueAxios from 'vue-axios';

  Vue.use(VueAxios, axios);

  export default {
    layout: 'dashboard', 
    components: {
      VWidget,
      EChart,
      BoxChart,
      codemirror
    },
    data: () => ({
      route: 'abc',
      newuser: 'testuser@fabba.space',
      color: Material,
      selectedTab: 'tab-1',
      log: 'Loading log ...',
      cmOptions: {
        // codemirror options
        tabSize: 4,
        mode: 'text/javascript',
        theme: 'mbo',
        readOnly: true,
        lineNumbers: true,
        line: true,
      }
    }),
    methods: {
      onRoute() {
        this.$router.push(this.route);
      },
      onToggleRoute() {
        this.$store.commit('app/togglePage');
      },
      onScroll (e) {
      },
      onNotification() {
        console.log(this.jwttoken);
        this.$store.dispatch('notifications/pushSuccess', "Test");
      },
      onTestLogin(user, password) {
        let loginAction = [];
        loginAction = [actionBuilder.newLoginUserAction(user, password)];
        this.$store.dispatch('actions/emitActionRequest', loginAction);
        this.$store.dispatch('user/login', null);
      },
      onTestRegistration() {
          let model = {
            email: this.newuser,
            firstname: 'Auto',
            lastname: 'Generated',
            organization: 'Test',
            password: '12345678',
            password_verification: '12345678',
          };
          let registerAction = [actionBuilder.newRegisterUserAction(model, { route : false })];
          this.$store.dispatch('actions/emitActionRequest', registerAction);
      },
      onTestLogout() {
        this.$store.dispatch('user/resetToken');
        this.$store.dispatch('user/logout');
      },
    },
    computed: {
      ...mapState('user', ['jwttoken']),   
    },
    created () {
    },
    mounted () {
   
    }

  };
</script>

<style scoped>
.zindex-repair{
    z-index:1;
}


.CodeMirror {
 /* Set height, width, borders, and global font properties here */
    font-family: monospace;
    height: 600px;
}
</style>
