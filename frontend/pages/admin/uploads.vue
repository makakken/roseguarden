<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>
      <v-card>
        <v-card-title>
          <h3>
            Upload a file
          </h3>
        </v-card-title>
        <v-row justify="space-around">
          <v-sheet
            id="dropzone"
            ref="dropzone"
            rounded
            class="rounded-lg"
            title="Click to grap a file from your PC!"
            :color="dragover ? 'blue lighten-3' : 'blue lighten-1' "
            width="350"
            style="cursor:pointer;"
            @click="chooseFile"
            height="150"
          >
            <v-container fill-height fluid>
              <v-row align="center" justify="center">
                <input 
                  ref="file"
                  id="file"
                  type="file" 
                  multiple
                  v-on:change="handleFileSelect"
                  v-show="false" />
                <v-icon
                  dark
                  v-if="!dragover && !uploadIsRunning" 
                  size="60"            
                >mdi-upload</v-icon>
                <v-icon                 
                  dark
                  v-if="dragover && !uploadIsRunning" 
                  size="60"
                >mdi-book-plus</v-icon>
                <v-progress-circular
                  v-if="uploadIsRunning"
                  rotate="-90"
                  size="60"
                  width="10"
                  :value="uploadProgress"
                  color="white"
                >
                  {{ uploadProgress }}
                </v-progress-circular>                
              </v-row>
              <v-row align="center" justify="center">
                <div  v-if="!uploadIsRunning" class="dark white--text text-center">Drag'n drop or click <br/> to upload file!</div>
                <div  v-if="uploadIsRunning" class="dark white--text text-center">{{uploadStatus}}</div>
              </v-row>
            </v-container>
          </v-sheet>
        </v-row>
        <br>
      </v-card>    
      <br/>        
      <v-card>
        <v-card-title>
          <h3>
            Uploads
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
          :items="nodes"
          :search="search"
        ></v-data-table>
      </v-card>    
    </v-flex>
  </v-container>
</template>

<script>
  import axios from 'axios';
  import VueAxios from 'vue-axios';

  export default {
    layout: "dashboard",
    components: {
    },
    data: () => ({
      search: '',
      files: [],
      uploadProgress: 0,
      uploadStatus: "Upload ongoing",
      uploadIsRunning: false,
      dragover: false,
      headers: [
        {
          text: 'Node ID',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        { text: 'Name', value: 'calories' },
        { text: 'Type', value: 'calories' },
        { text: 'Verified', value: 'fat' },
        { text: 'Last action at', value: 'carbs' },
        { text: 'Actions', value: 'carbs' },
      ],
      nodes: []
    }),
    watch: {
      uploadProgress: function(_newVal) {
        console.log("new", _newVal)
        if (this.uploadProgress >= 100) {
          this.uploadStatus = "Upload succesful"
          setTimeout(() => {
            this.uploadIsRunning = false;
          }, 2000);
        }        
      }      
    },
    methods: {
      async runFileUpload() {
        this.uploadIsRunning = true;
        this.uploadProgress = 0;
        this.uploadStatus = "Upload ongoing";
        // axios config 
        const axios_config = {
          // progress event function
          onUploadProgress: function(progressEvent) {
            // calculate progress
            this.uploadProgress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            console.log("progress:", this.uploadProgress);
            // if progress is 100%, set the in preparation flag to show that the upload is complete but the process is not finished (response)
          }.bind(this)
        };

        // build FormData of all files
        var uploadFormData = new FormData();
        var cnt = 0;
        for (var file of this.files) {
          console.log(file);
          uploadFormData.append(cnt.toString(), file);
          cnt+=1;
        }

        console.log("send files");
        axios
          .post("/api/v1/file/upload", uploadFormData, axios_config, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(_response => {
            this.uploadProgress = 100;
          })
          .catch(error => {
            this.uploadProgress = 0;
            this.uploadStatus = "Upload failed, please try again";
            console.log("Upload failed");
          });
      },
      handleFileSelect() {
        this.files = this.$refs.file.files;
        this.runFileUpload();
      },
      handleFileDrag(files) {
        this.files = files;
        this.runFileUpload();
      },
      chooseFile() {
        console.log("click")
        this.$refs.file.click();
      },      
    },      
    mounted () {
      const dropzone = this.$el
      const fileupload = this.$el.firstElementChild    // register listeners on your dropzone / v-sheet
      if(dropzone) {
        // register all drag & drop event listeners
        dropzone.addEventListener("dragenter", e => {
          e.preventDefault();
          this.dragover = true;
        })
        dropzone.addEventListener("dragleave", e => { 
          e.preventDefault();
          this.dragover = false;
        })
        dropzone.addEventListener("dragover", e => { 
          e.preventDefault();
          this.dragover = true;
        })       
        dropzone.addEventListener("drop", function(e) { 
          e.preventDefault()
          const dragevent = e;
          if(dragevent.dataTransfer) {
            var files = [];
            for (let i = 0; i < e.dataTransfer.files.length; i++) {
              if (e.dataTransfer.files[i].size > 0) {
                if (!e.dataTransfer.items[i].webkitGetAsEntry().isDirectory) {
                  files.push(e.dataTransfer.files[i]);
                }
              }
            }
            this.dragover = false;
            this.handleFileDrag(files);
          }
        }.bind(this));  
      }
    }    
  }
</script>

<style scoped>

</style>
