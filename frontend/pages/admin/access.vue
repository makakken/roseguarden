<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            Groups (space access)
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="users"
          :search="search"
        ></v-data-table>
      </v-card>    
    </v-flex>
    <v-flex lg12 sm12 xs12>
      <br>
    </v-flex>
    <v-flex lg12 sm12 xs12>
      <v-card>
        <v-card-title>
          <h3>
            Users access
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="users"
          :search="search"
        ></v-data-table>
      </v-card>    
    </v-flex>
  </v-container>
</template>

<script>
  export default {
    layout: "dashboard",
    components: {
    },
    data: () => ({
      search: '',
      headers: [
        {
          text: 'Name',
          align: 'left',
          sortable: false,
          value: 'name',
        },
      ],
      users: []
    }),
  }
</script>

<style scoped>

</style>
