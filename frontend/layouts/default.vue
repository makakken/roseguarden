<template>
  <div id="appRoot">
    <v-app id="inspire" class="app">
      <nuxt />
      <v-snackbar
        :timeout="4000"
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
    </v-app>
  </div>
</template>

<script>
import { mapState } from "vuex";
import * as actionBuilder from "@/api/actionBuilder";

export default {
  data: () => ({
    expanded: true,
    rightDrawer: false,
    snackbar: {
      show: false,
      text: "",
      color: "error",
    },
  }),
  computed: {
    ...mapState("notifications", ["message"]),
  },
  watch: {
    message(newValue, oldValue) {
      this.$nextTick(function () {
        if (newValue !== "") {
          this.snackbar.color = this.$store.state.notifications.color;
          this.snackbar.text = this.$store.state.notifications.message;
          this.snackbar.show = true;
          this.$store.commit("notifications/updateSnackbar", {
            message: "",
            color: "primary",
          });
        }
      });
    },
  },
  mounted() {
    this.$store.dispatch("actions/startRunner");
    /*
      .then(response => {
          let menuAction = [actionBuilder.newProvideMenuAction()];
          this.$store.dispatch('actions/emitActionRequest', menuAction);     
      })
      */
  },
};
</script>


<style lang="stylus" scoped>
>>> .error {
  background-color: #FF5252 !important;
}

>>> .info {
  background-color: #2196F3 !important;
}

>>> .success {
  background-color: #4CAF50 !important;
}

>>> .warning {
  background-color: #FFC107 !important;
}

>>> .error--text {
  color: #ff5252 !important;
  caret-color: #ff5252 !important;
}
</style>