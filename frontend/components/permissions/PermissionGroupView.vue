<template>
  <div v-if="group!=null"> 
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Name</v-subheader>
        <v-text-field
          label="Name"
          v-model="group.name"
          hide-details
          solo
          dense
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Description</v-subheader>
        <v-text-field
          label="Note"
          v-model="group.description"
          hide-details
          solo
          dense
        ></v-text-field>
      </v-col>
    </v-row> 
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Permissions</v-subheader>
        <v-card
          class="mx-auto"
          tile
          dense
        >
          <v-list shaped>
            <v-list-item-group
              v-model="group.permissions"
              multiple
            >
              <v-list-item
                v-for="(item, i) in permissions"
                :key="i"
                :value="item.id"
                active-class="blue--text text--accent-4"
              >
                <template v-slot:default="{ active, toggle }">
                  <v-list-item-content>
                    <v-list-item-title v-text="item.name"/>
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
    <v-row dense >
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
    group: {
      required: true,
      default: function() {
        return {};
      }
    },
    permissions: {
      required: true,
      default: function() {
        return [];
      }
    },
  },
  data: () => ({
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
    group(newValue, oldValue) {
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
