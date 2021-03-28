<template>
  <v-navigation-drawer
    id="appDrawer"
    :mini-variant.sync="mini"
    fixed
    :dark="$vuetify.theme.dark"
    app
    disable-route-watcher
    v-model="drawer"
    width="260"
  >
    <v-toolbar color="primary">
      <img src="../static/konglo_logo.png" height="36" alt="" />
      <v-toolbar-title href="/" class="ml-0 pl-3">
        <v-btn to="/" text
          ><span class="hidden-sm-and-down">roseguarden</span>
        </v-btn>
      </v-toolbar-title>
    </v-toolbar>
    <vue-perfect-scrollbar
      v-bind:class="['drawer-menu--scroll', submenu ? 'submenustyle' : '']"
      :settings="scrollSettings"
    >
      <div v-if="loading" class="text-xs-center">
        <v-progress-circular
          :size="70"
          :width="7"
          style="margin-top: 50%"
          color="primary"
          indeterminate
        ></v-progress-circular>
      </div>
      <v-list v-else dense expand>
        <v-list-item v-if="submenu" :to="item.href">
          <v-list-item-action>
            <v-btn style="min-width: 40px" item dark small color="#616161">
              <v-icon dark style="margin: 4px">reply</v-icon>
            </v-btn>
          </v-list-item-action>
          <v-list-item-content @click="click()">
            <v-list-item-title style="font-size: 1.5em">{{
              submenuname
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <template v-for="(item, i) in mainmenu">
          <!--group with subitems-->
          <v-list-group
            v-if="item.items"
            :key="item.name"
            :group="item.group"
            :prepend-icon="item.icon"
            no-action="no-action"
          >
            <v-list-item slot="activator" ripple="ripple">
              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <template v-for="(subItem, i) in item.items">
              <!--sub group-->
              <v-list-group
                v-if="subItem.items"
                :key="subItem.name"
                :group="subItem.group"
                sub-group="sub-group"
              >
                <v-list-item slot="activator" ripple="ripple">
                  <v-list-item-content>
                    <v-list-item-title>{{ subItem.title }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item
                  v-for="(grand, i) in subItem.children"
                  :to="item.href"
                  :key="i"
                  @click="click(item)"
                  ripple="ripple"
                >
                  <v-list-item-content>
                    <v-list-item-title>{{ grand.title }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-group>
              <!--child item-->
              <v-list-item
                v-else
                :key="i"
                :to="item.href"
                @click="click(item)"
                :disabled="subItem.disabled"
                :target="subItem.target"
                ripple="ripple"
              >
                <v-list-item-content>
                  <v-list-item-title
                    ><span>{{ subItem.title }}</span></v-list-item-title
                  >
                </v-list-item-content>
                <v-list-item-action v-if="subItem.action">
                  <v-icon :class="[subItem.actionClass || 'success--text']">{{
                    subItem.action
                  }}</v-icon>
                </v-list-item-action>
              </v-list-item>
            </template>
          </v-list-group>
          <v-subheader v-else-if="item.header" :key="i">{{
            item.header
          }}</v-subheader>
          <v-divider v-else-if="item.divider" :key="i"></v-divider>
          <v-list-item
            v-else-if="item.external === true"
            :href="item.href"
            :key="item.name"
            target="_blank"
          >
            <v-list-item-action v-if="item.icon">
              <v-icon>{{ item.icon }} </v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }} </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action v-if="item.subAction">
              <v-icon class="success--text">{{ item.subAction }}</v-icon>
            </v-list-item-action>
          </v-list-item>
          <!--top-level link-->
          <v-list-item
            v-else
            :to="item.href"
            @click="click(item)"
            ripple="ripple"
            :disabled="item.disabled"
            :target="item.target"
            rel="noopener"
            :key="item.name"
          >
            <v-list-item-action v-if="item.icon">
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }} </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action v-if="item.subAction">
              <v-icon class="success--text">{{ item.subAction }}</v-icon>
            </v-list-item-action>
          </v-list-item>
        </template>
      </v-list>
    </vue-perfect-scrollbar>
  </v-navigation-drawer>
</template>
<script>
import VuePerfectScrollbar from "vue-perfect-scrollbar";
import { mapState } from "vuex";

export default {
  name: "app-drawer",
  components: {
    VuePerfectScrollbar,
  },
  props: {
    expanded: {
      type: Boolean,
      default: true,
    },
  },
  data: () => ({
    mini: false,
    submenuname: "User",
    scrollSettings: {
      maxScrollbarLength: 160,
    },
  }),
  computed: {
    ...mapState("menu", ["loading"]),
    ...mapState("menu", ["submenu"]),
    ...mapState("menu", ["mainmenu"]),
    drawer: {
      get() {
        return this.$store.state.app.drawer;
      },
      set(val) {
        this.$store.commit("app/drawer", val);
      },
    },
    computeGroupActive() {
      return true;
    },
    sideToolbarColor() {
      return this.$vuetify.options.extra.sideNav;
    },
  },
  methods: {
    click(item) {
      console.log("click", item);
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
        case "sm":
          this.$store.commit("app/drawer", false);
          break;
      }
      /*
        if(item.href) {
          if(item.external) {
            window.location = item.href;
          } else {
            this.$router.push(item.href)
          }
        }*/
    },
    genChildTarget(item, subItem) {
      if (subItem.href) return;
      if (subItem.component) {
        return {
          name: subItem.component,
        };
      }
      return { name: `${item.group}/${subItem.name}` };
    },
  },
  mounted() {},
};
</script>


<style lang="stylus" scoped>
.submenustyle {
  background-color: #e5e5e5;
}

#appDrawer {
  overflow: hidden;

  .drawer-menu--scroll {
    height: calc(100% - 124px);
  }
}

.a.normal:link {
  color: black;
}

.a.normal:visited {
  color: black;
}

.a.normal:hover {
  color: black;
}
</style>
