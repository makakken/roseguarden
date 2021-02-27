<template>
  <div id="appRoot">
    <template>
      <v-app id="inspire" class="app">
        <app-drawer class="app--drawer"></app-drawer>
        <app-toolbar class="app--toolbar"></app-toolbar>
        <v-content>
          <!-- Page Header -->
          <page-header></page-header>
          <div class="page-wrapper">
            <nuxt />
          </div>
          <!-- App Footer -->
          <v-footer height="auto" class="white pa-3 app--footer">
            <span class="caption">
              <b> Roseguarden:</b>
              <a href="https://gitlab.com/roseguarden"
                >https://gitlab.com/roseguarden</a
              >, &copy; {{ new Date().getFullYear() }}, Backend: v{{
                backendVersion
              }}, Frontend: v{{ frontendVersion }}
            </span>

            <v-spacer></v-spacer>
            <span class="caption mr-1"> Made with love </span>
            <v-icon color="pink" small>favorite</v-icon>
          </v-footer>
        </v-content>
        <!-- Go to top -->
        <app-fab></app-fab>
        <!--
        <v-btn small fab dark falt fixed top="top" right="right" class="setting-fab" color="red"
               @click="openThemeSettings">
          <v-icon>settings</v-icon>
        </v-btn>
        <v-navigation-drawer
          class="setting-drawer"
          temporary
          right
          v-model="rightDrawer"
          hide-overlay
          fixed
        >
        <theme-settings></theme-settings> 
        </v-navigation-drawer> 
        -->
        <v-footer
          min-height="60px"
          class="app grey darken-2 pa-3 footerclass white--text"
        >
          <cookie-law theme="dark-lime" buttonText="I accept">
            <div slot="message">
              This site uses cookies. Only necessary cookies will be stored. For
              more information
              <router-link to="privacy">Click here</router-link>
            </div>
          </cookie-law>
          <v-row dense no-gutters justify="center">
            <v-btn
              v-for="link in footerlinks"
              color="white"
              text
              rounded
              :key="link.link"
              :to="link.link"
            >
              {{ link.label }}
            </v-btn>
            <v-spacer />

            <v-btn
              color="white"
              text
              rounded
              href="https://gitlab.com/roseguarden"
            >
              <strong
                >Powered by roseguarden - &copy; {{ new Date().getFullYear() }}
              </strong>
            </v-btn>
          </v-row>
        </v-footer>
      </v-app>
    </template>

    <v-snackbar
      :timeout="3000"
      bottom
      center
      :color="snackbar.color"
      v-model="snackbar.show"
    >
      {{ snackbar.text }}
      <v-btn dark text @click.native="snackbar.show = false" icon>
        <v-icon>close</v-icon>
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import AppDrawer from "@/components/AppDrawer";
import AppToolbar from "@/components/AppToolbar";
import AppFab from "@/components/AppFab";
import PageHeader from "@/components/PageHeader";
import ThemeSettings from "@/components/ThemeSettings";
import * as actionBuilder from "@/api/actionBuilder";
import { mapState } from "vuex";
import CookieLaw from "vue-cookie-law";

export default {
  components: {
    AppDrawer,
    AppToolbar,
    AppFab,
    PageHeader,
    ThemeSettings,
    CookieLaw,
  },
  data: () => ({
    expanded: true,
    rightDrawer: false,
    footerlinks: [
      {
        label: "About",
        link: "/about",
      },
      {
        label: "Contact",
        link: "/contact",
      },
      {
        label: "Privacy policy",
        link: "/privacy",
      },
      {
        label: "Legal notice",
        link: "/legal",
      },
    ],
    snackbar: {
      show: false,
      text: "",
      color: "error",
    },
  }),
  computed: {
    ...mapState("notifications", ["message"]),
    ...mapState("app", ["backendVersion", "frontendVersion"]),
  },
  watch: {
    message(newValue, oldValue) {
      if (newValue !== "") {
        this.snackbar.color = this.$store.state.notifications.color;
        this.snackbar.text = this.$store.state.notifications.message;
        this.snackbar.show = true;
        this.$store.commit("notifications/updateSnackbar", {
          message: "",
          color: "primary",
        });
      }
    },
  },
  methods: {
    openThemeSettings() {
      this.$vuetify.goTo(0);
      this.rightDrawer = !this.rightDrawer;
    },
  },
  mounted() {
    this.$store.dispatch("actions/startRunner").then((response) => {
      let menuAction = [actionBuilder.newProvideMenuAction()];
      this.$store.dispatch("actions/emitActionRequest", menuAction);
    });
  },
};
</script>

<style lang="stylus" scoped>
.setting-fab {
  top: 50% !important;
  right: 0;
  border-radius: 0;
}

.page-wrapper {
  min-height: calc(100vh - 64px - 50px - 81px);
  margin-bottom: 50px;
}

.app--footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.footerclass {
  background-color: #616161;
  z-index: 100;
}
</style>
