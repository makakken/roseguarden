<template>
    <codemirror  ref="editor" :value="value" :options="cmOptions"  @input="onChange" class="zindex-repair"></codemirror>
</template>


<script>
  import { codemirror } from 'vue-codemirror';
  import 'codemirror/lib/codemirror.css';
  import 'codemirror/theme/material.css';
  import 'codemirror/addon/display/autorefresh.js';
  import CodeMirror from "codemirror";


  export default {
    components: {
      codemirror,
    },      
    props: {
      value: {
        type: String,
        default: ""
      },
      height: {
        type: String,
        default: '400px'
      },
      readOnly: {
        type: Boolean,
        default: false
      },
      lineNumbers: {
        type: Boolean,
        default: false
      }      
    },
    data: function() {
      return {
        cmOptions: {
            // codemirror options
            tabSize: 4,
            mode: 'text/html',
            theme: 'material',
            readOnly: this.readOnly,
            lineNumbers: this.lineNumbers,
            line: false,
            lineWrapping: false,
            gutters: ["CodeMirror-linenumbers"],
            autoRefresh: true
        }
      }
    },
    computed: {
      codemirror() {
        return this.$refs.editor.codemirror 
      },
    },    
    methods: {
        onChange(newCode) {
            this.$emit('input', newCode)
        },
        refresh() {
          this.codemirror.focus();
          this.codemirror.setCursor(this.codemirror.lineCount(), 0);
          this.codemirror.setSize("auto",this.height);
          this.codemirror.refresh();
        }
    },
    mounted () {
      this.codemirror.focus();
      this.codemirror.setCursor(this.codemirror.lineCount(), 0);
      this.codemirror.setSize("auto",this.height);

    }    
  }
</script>

<style scoped>


.buttons-margin {
  margin: 4px;

}

.CodeMirror {
 /* Set height, width, borders, and global font properties here */
  font-family: "monospace";
}

.CodeMirror pre {
    white-space: pre-wrap;
    word-break: break-all;
    word-wrap: break-word;
}
</style>
