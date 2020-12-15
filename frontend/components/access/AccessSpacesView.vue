<template>
  <div v-if="space!=null"> 
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Name</v-subheader>
        <v-text-field
          label="Name"
          v-model="space.name"
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
          v-model="space.description"
          hide-details
          solo
          dense
        ></v-text-field>
      </v-col>
    </v-row> 
    <v-row dense>
      <v-col cols="1" />
      <v-col cols="10">
        <v-subheader>Entrance nodes</v-subheader>
        <v-card
          class="mx-auto"
          tile
          dense
        >
          <v-list shaped>
            <v-list-item-group
              v-model="space.entrance_nodes"
              multiple
            >
              <v-list-item
                v-for="(item, i) in entrance_nodes"
                :key="i"
                :value="item.id"
                active-class="blue--text text--accent-4"
              >
                <template v-slot:default="{ active, toggle }">
                  <v-list-item-content>
                    <v-list-item-title v-text="item.name"/>
                    <v-list-item-subtitle>
                      {{item.fingerprint}} <br>
                      <span v-if="item.authorized" style="color: green">Authorized</span>
                      <span v-else style="color: red">Not authorized</span>
                      <span v-if="item.active" style="color: green">, Active</span>
                      <span v-else style="color: red">, Not active</span>
                    </v-list-item-subtitle>
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
    space: {
      required: true,
      default: function() {
        return {};
      }
    },
    entrance_nodes: {
      required: true,
      default: function() {
        return [];
      }
    },
  },
  data: () => ({
  }),
  computed: {
  },
  watch: {
    space(newValue, oldValue) {
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
