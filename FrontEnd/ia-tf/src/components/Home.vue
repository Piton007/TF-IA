<template>
  <v-layout align-start>
    <v-flex>
     <v-stepper  v-model="e1">
    <v-stepper-header>
      <v-stepper-step editable  edit-icon="assignment_ind" :complete="e1 > 1" step="1">Registro de Usuario</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step editable  edit-icon="face" :complete="e1 > 2" step="2">Resultados</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step editable  step="3">Estadisticas</v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
         

      <v-dialog
          v-model="terminosDialog"
         max-width="600px"
          >
          <v-card>
            <v-card-title class="headline">Terminos y Condiciones de uso</v-card-title>

            <v-card-text>
              Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color="green darken-1"
                text
                @click="terminosDialog = false"
              >
                Cancelar
              </v-btn>

              <v-btn
                color="green darken-1"
                text
                @click="terminosDialog = false"
              >
                Acepto
              </v-btn>
            </v-card-actions>
          </v-card>
         </v-dialog>
      <v-card 
      
      class="mx-auto my-5 px-5 py-5 "
      
        >
        <v-form 
        ref="form"
        
        
        >
          <v-text-field
            :rules="[v => !!v || 'Inserte un usuario']"
            v-model="name"
            prepend-icon="fab fa-twitter-square"
            hint="Usuario de Twitter"
            label="Username"
           
            required
            
          ></v-text-field>
         <v-checkbox required v-model="checkbox"
         :rules="[v => !!v || 'Acepte Terminos y Condiciones']"
         >
            <template v-slot:label>
              <div>
                Acepto los 
                <a
                      href="#"
                      
                      @click.stop="terminosDialog = true"
                      
                    >
                      Terminos y Condiciones
                    </a>
              </div>
            </template>
            </v-checkbox>

          <v-btn text color="success" @click="IniciarPrueba">Analizar</v-btn>
          
        </v-form>

      </v-card>
        <v-alert dismissible v-if="valid && !error " type="success">
            Usuario Valido
          </v-alert>
          <v-alert  v-if="!valid && error " type="error">
            Usuario Invalido
          </v-alert>
      </v-stepper-content>

      <v-stepper-content  step="3">
        <v-layout justify-center v-if='chartData.length<=1'>
                    <v-progress-circular
                    :indeterminate="contentUser"
                    size="200"
                    color="light-blue"
                  >Waiting for Data</v-progress-circular>
                  </v-layout>
        <v-card v-if='e1==3 && chartData.length>1'
      class="mx-auto my-5 px-5 py-5 "
        >
       
            <GChart 
        :settings="{packages: ['bar']}"    
        :data="chartData"
        :options="chartOptions"
        :createChart="(el, google) => new google.charts.Bar(el)"
        @ready="onChartReady"
       
         />
         
     
       </v-card>
       

      </v-stepper-content>

      <v-stepper-content step="2">
       
     <v-layout>
    <v-flex xs12 sm6 offset-sm3>
                <v-layout justify-center v-if='user==""'>
                    <v-progress-circular
                    :indeterminate="contentUser"
                    size="200"
                    color="light-blue"
                  >Waiting for Data</v-progress-circular>
                  </v-layout>
             <v-card v-if='user!=""'
                class="mx-auto"
                max-width="350"
                outlined
              >
              <v-img  :src="user.profile_banner_url" >
               <v-list-item three-line>
                  <v-list-item-content>
                    <div ><v-btn :href="user.twitterUrl" target="_blank" text icon color="primary">
                        <v-icon>fab fa-twitter</v-icon>
                      </v-btn></div>
                    <v-list-item-title  class="font-weight-black headline mb-1">{{user.name}}</v-list-item-title>
                    <v-list-item-subtitle class="font-weight-black"> <span class="username"> @{{user.screen_name}}</span></v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-avatar
                    
                    size="80"
                    color="grey"
                  >

                  <v-img :src="user.profile_image_url"></v-img>
                  </v-list-item-avatar>
                </v-list-item>
              </v-img>
                

                <v-card-actions>
                  <v-layout align-center justify-center>
                  <div class="text-center">
                      <v-alert
                        v-model="alert"
                        border="left"
                        close-text="Close Alert"
                        :color="resultado"
                        dark
                        dismissible
                      >
                        Aenean imperdiet. Quisque id odio. Cras dapibus. Pellentesque ut neque. Cras dapibus.

                        Vivamus consectetuer hendrerit lacus. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur blandit mollis lacus. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo.
                      </v-alert>
                      <div class="text-center">
                        <v-btn
                          v-if="!alert"
                          color="blue-grey darken-4"
                          
                          text
                          @click="alert = true"
                        >
                          Resultados
                        </v-btn>
                      </div>
                    </div>
                 </v-layout>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
  
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>

    </v-flex>
  </v-layout>
</template>
<script>
import { GChart } from 'vue-google-charts'
import axios from "axios";

export default {
    components:{
      GChart
    },
  data() {
    return {
      alert:false,
      error:false,
      user:"",
       card_text: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
     e1:0,
     valid:false,
     contentUser:true,
     contentStadistics:true,
     name:"",
     resultados:false,
     terminosDialog:false,
     checkbox:0,
    chartsLib: null, 
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Months', 'Polarity', 'Subjectivity']
      ]
    };
  },
   computed: {
     chartOptions () {
      if (!this.chartsLib) {return null}
      
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Estadisticas del usuario '+this.user.name,
          subtitle: 'Resultados del ultimo año'
        },
        bars: 'vertical', // Required for Material Bar Charts.
        hAxis: { format: 'decimal' },
        
        height: 400,
        colors: [ '#d95f02', '#7570b3']
      })
    }
  },
  methods: {
     onChartReady (chart, google) {
      
      this.chartsLib = google
      
    },
    openTerminosCondiciones(){
      alert("hello")
      
      
    },
    IniciarPrueba(){
      this.validarUser()
      //this.fetchStadistics()
    },
    validarUser()
    {
      
      if (this.$refs.form.validate()) {
        let me = this;
      axios
        .post("users",{
          UserName:this.name,
          LimitsTweets:200}
        )
        .then(function(response) {
         me.error=false
         me.valid=true
          me.user=response.data
          me.valid=true
        })
        .catch(function(error) {
          me.error=true
          me.valid=false
        });
      }
      
    },
    fetchStadistics(){
      let me = this;
      axios
        .get("stadistics")
        .then(function(response) {
          for (let mes of Object.keys(response.data) ) me.chartData.push([mes, response.data[mes]["polaridad"] , response.data[mes]["subjectividad"]])
              
        })
        .catch(function(error) {
          alert(error);
        });
    }
    
  }
};
</script>
<style scoped>
  .username{
    color:#299FE3;
  }
</style>