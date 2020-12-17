  <template>
  <v-layout row class="align-center layout px-4 pt-4 app--page-header">
    <div class="page-header-left">
      <h3 class="pr-3">{{title}}</h3>
    </div>


    </v-breadcrumbs>
    <v-spacer></v-spacer>
  </v-layout>  
</template>

<script>
import menu from '@/api/menu';
export default {
  data () {
    return {
      title: ''
    };
  },
  computed: { 
  },
  mounted () {

  }
}
</script>
