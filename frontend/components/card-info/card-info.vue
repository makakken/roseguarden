<template>
  <v-card class="mx-auto" max-width="344">
    <v-img
    v-if="attrImgSource"
    :width="attrWidth"
    :src="attrImgSource"
    :lazy-src="getImgSourceSmall"
    >
  </v-img>

  <v-card-title>
    <slot name="header"></slot>
  </v-card-title>

  <v-card-text>
    <slot name="content"></slot>
  </v-card-text>

  <v-divider v-if="hasSlotContentHidden"></v-divider>

  <v-card-actions>
    <v-btn block text @click="show = !show" v-if="hasSlotContentHidden">
      <span v-show="show">
        weniger Lesen
      </span>
      <span v-show="!show">
        mehr Lesen
      </span>
      <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
    </v-btn>
  </v-card-actions>

  <v-expand-transition>
    <div v-show="show">
      <v-card-text>
        <slot name="content-hidden"></slot>
      </v-card-text>
    </div>
  </v-expand-transition>
</v-card>
</template>

<script>
export default {
  name: "CardInfo",
  props: {
    attrImgSource: {
      required: true,
      default: function() {
        return "";
      }
    },
    attrWidth: {
      default: function() {
        return "350px";
      }
    }
  },
  data: () => ({
    show: false,
  }),
  computed: {
    getImgSourceSmall() {
      let smallImgSource = this.$props["attrImgSource"].split(".");

      if (smallImgSource.length > 0) {
        // follow img name convention
        // we need 2 images:
        // myImage.jpg and myImage-small.jpg
        return `${smallImgSource[0]}-small.${smallImgSource[1]}`;
      } else {
        return "";
      }
    },
    hasSlotContentHidden() {
      return !!this.$slots["content-hidden"];
    }
  }
};
</script>
