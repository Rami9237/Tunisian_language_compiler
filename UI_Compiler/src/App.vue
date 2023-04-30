<template>
  <v-app>
    <v-main>
    <Nav />
      <v-img src="@/assets/blob.svg" class="abs-fix"/>
      <div class="d-flex justify-center align-items-center min-h-100-vh flex-column">
        <h1>Type in your <span class="green-dark">code !</span> </h1>
        <v-container>
          <v-row>
            <Transition  name="slide-fade-right" appear>
            <v-col :cols="12" :md="5">
              <div class="textarea-cont" >
                <h2 class="green-dark">Input</h2>
                <v-textarea  v-model="text1" label="Tunisian Code" variant="outlined" color="green darken-2" :no-resize="true"></v-textarea>
              </div>    
            </v-col>
            </Transition>
            <v-col :cols="12" :md="2" class="d-flex align-items-center">
              <v-btn block rounded="xl" size="x-large" color="green darken-2" @click="compile_input">Convert <v-icon icon="mdi-arrow-right"></v-icon></v-btn>
            </v-col>
            <Transition name="slide-fade-left" appear>
            <v-col :cols="12" :md="5">
              <div class="textarea-cont">
                <h2 class="green-dark">Output</h2>
                <v-textarea v-model="text2" label="Python Code" color="green darken-2" variant="outlined" :no-resize="true"></v-textarea>

              </div>

            </v-col>
          </Transition>
          </v-row>
          <div v-if="showOP">
                Output:
              <v-hover v-slot="{ isHovering }" v-if="!error">
                <v-card :elevation="isHovering ? 24 : 6" class="mx-auto pa-6" v-for="substring,key in substrings" :key="key">
                  <v-chip class="ma-2" color='green' text-color="white">{{ key }}</v-chip>
                  {{substring}}    
                </v-card>
              </v-hover>
              <v-hover v-slot="{ isHovering }" v-else>
                <v-card :elevation="isHovering ? 24 : 6" class="mx-auto pa-6">
                  <v-chip class="ma-2" color='red' text-color="white">{{ 0 }}</v-chip>
                  {{error}}    
                </v-card>
              </v-hover>
              </div>
        </v-container>
    </div>
    </v-main>
  
  </v-app>
</template>

<script>
import Nav from './components/Nav.vue'
import axios from 'axios'
export default {
  name: 'App',

  components: {
    Nav,
  },

  data: () => ({
    text1 : "",
    text2 : "",
    show : false,
    showOP : false,
    output : "",
    substrings : "",
    error : null,
  }),
  mounted(){
    this.show = true;
  },
  methods:{
    compile_input() {
    if (this.text1 === "") {
      console.log("Please enter text to be executed first");
    } else {
      const path = 'http://127.0.0.1:5000/read_input';
      const data = { code: this.text1 }; // Construct the data to be sent to the server
      axios.post(path, data) // Send the HTTP POST request to the server
        .then((res) => {
          if(res.data.err == ""){
            this.error = null;
            this.text2 = res.data.code; // Set the response data to the 'text2' data property
            this.output = res.data.result;
            this.substrings = this.output.split('\n');
            this.substrings = this.substrings.filter(substring => substring != "")
          }
          else{
            this.error = res.data.err;
            
          }
          this.showOP = true;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }
  }
}

</script>
<style scoped>
.min-h-100-vh{
  min-height: 92vh;
}
.align-items-center{
  align-items: center;
}
.green-dark{
  color: #4CAF50 !important;
}

.abs-fix{
  right : -100px;
  top : -100px;
  position : absolute;
  height:460px;
  width:500px;
}
.textarea-cont{
  border-radius : 10px;
  border: 1px solid green;
  padding: 10px;
}
@media (max-width: 960px) {
  .abs-fix{
    height:220px;
    width:300px;
    right : -120px;
  top : -50px;
  position : absolute;
  }

}
.slide-fade-right-enter-from{
  opacity : 0;
  transform:translateX(-30px);
}
.slide-fade-right-enter-active{
  transition :  1s;
}
.slide-fade-left-enter-from{
  opacity : 0;
  transform:translateX(30px);
}
.slide-fade-left-enter-active{
  transition :  1s;
}
@font-face {
    font-family:"MKPRO";
    src: url("../Fonts/FontFont_FF.Mark.Pro.Light.ttf");
}
*{
  font-family: "MKPRO";
}
</style>