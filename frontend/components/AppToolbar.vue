<template>
  <v-app-bar fixed app color="primary">
    <v-app-bar-nav-icon @click.stop="toggleDrawer()"></v-app-bar-nav-icon>
    <v-spacer></v-spacer>
    <v-btn class="hidden-sm-and-down" icon @click="handleFullScreen()">
      <v-icon>fullscreen</v-icon>
    </v-btn>
    <v-menu
      offset-y
      origin="center center"
      :nudge-right="140"
      :nudge-bottom="10"
      transition="scale-transition"
    >
      <template v-slot:activator="{ on }">
        <v-btn icon large v-on="on">
          <v-avatar size="30px">
            <v-icon>person</v-icon>
          </v-avatar>
        </v-btn>
      </template>
      <v-list class="pa-0">
        <v-list-item
          v-for="(item, index) in userMenu"
          :to="!item.href ? { name: item.name } : null"
          :href="item.href"
          @click="item.click"
          ripple="ripple"
          :disabled="item.disabled"
          :target="item.target"
          rel="noopener"
          :key="index"
        >
          <v-list-item-action v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>
<script>
import * as Util from "@/util";
import menu from "@/api/menu";

export default {
  name: "app-toolbar",
  components: {},
  data: () => ({}),
  computed: {
    userMenu: {
      get() {
        return this.$store.state.user.usermenu;
      },
    },
    toolbarColor() {
      return this.$vuetify.options.extra.mainNav;
    },
  },
  methods: {
    toggleDrawer() {
      this.$store.commit("app/toggleDrawer");
    },
    handleFullScreen() {
      Util.toggleFullScreen();
    },
  },
};
</script>
