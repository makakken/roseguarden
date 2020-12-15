<template>
  <div v-if="user!=null"> 
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Permission groups</v-subheader>
        <v-card
          class="mx-auto"
          tile
          dense
        >
          <v-list shaped>
            <v-list-item-group
              v-model="user.rolesSelection"
              multiple
            >
              <v-list-item
                v-for="(item, i) in permissionGroups"
                :key="i"
                :value="item.id"
                active-class="blue--text text--accent-4"
              >
                <template v-slot:default="{ active, toggle }">
                  <v-list-item-content>
                    <v-list-item-title v-text="item.name"></v-list-item-title>
                    <v-list-item-subtitle v-text="item.description"/>                    
                  </v-list-item-content>
    
                  <v-list-item-action>
                    <v-icon>{{active ? "check_box" : "check_box_outline_blank"}}</v-icon>
                  </v-list-item-action>
                </template>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>     
    <v-row >
      <v-col cols="11"  class="text-right">
        <v-spacer></v-spacer>
        <v-btn color="warning" v-on:click="onCancel">Cancel</v-btn>      
        <v-btn color="success" v-on:click="onSubmit">Submit</v-btn>      
      </v-col>
    </v-row>    
    <br/>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      required: true,
      default: function() {
        return {};
      }
    },
    permissionGroups: {
      required: true,
      default: function() {
        return [];
      }
    },
  },
  data: () => ({
    doors: Array(8).fill(false),      
    days: Array(7).fill(false),
    items: [
      { 'label' : '0', 'id': 9  },
      { 'label' : '1', 'id': 8  },
      { 'label' : '2', 'id': 7  },
      { 'label' : '3', 'id': 1  },
    ],
    model: [],    
  }),
  computed: {
    accessTypeItems: function() {
      if(this.groupProps.hasOwnProperty("type")) {
        return this.groupProps.type.selection;
      } else {
        return [];
      }
    },
  },
  watch: {
    user(newValue, oldValue) {
    }
  },
  methods: {
    onSubmit() {
      this.$emit('submit')
    },
    onCancel() {
      this.$emit('cancel')      
    },  
  }, 
};
</script>
