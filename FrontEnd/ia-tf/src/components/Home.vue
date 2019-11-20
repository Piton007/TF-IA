<template>
  <v-layout align-start>
    <v-flex>
     <v-stepper  v-model="e1">
    <v-stepper-header>
      <v-stepper-step  complete-icon="assignment_ind" :complete="e1 > 1" step="1">Registro de Usuario</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step editable  edit-icon="assessment" :complete="e1 > 2" step="2">Estadisticas</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step editable  step="3">Resultado</v-stepper-step>
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
                Disagree
              </v-btn>

              <v-btn
                color="green darken-1"
                text
                @click="terminosDialog = false"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
         </v-dialog>
      <v-card 
      class="mx-auto my-5 px-5 py-5 "
        >
        <form>
          <v-text-field
            v-model="name"
            prepend-icon="fab fa-twitter-square"
            hint="Usuario de Twitter"
            label="Username"
            data-vv-name="name"
            required
            
          ></v-text-field>
         <v-checkbox v-model="checkbox">
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

          <v-btn text color="primary" @click="e1=2">Continuar</v-btn>
          
        </form>

      </v-card>
        
      </v-stepper-content>

      <v-stepper-content  step="2">
      
        <v-card 
      class="mx-auto my-5 px-5 py-5 "
        >
       
            <GChart v-if="e1==2"
        :settings="{packages: ['bar']}"    
        :data="chartData"
        :options="chartOptions"
        :createChart="(el, google) => new google.charts.Bar(el)"
        @ready="onChartReady"
       
         />
        
     
       </v-card>
        
      </v-stepper-content>

      <v-stepper-content step="3">
       
     <v-layout>
    <v-flex xs12 sm6 offset-sm3>
              <v-card>
                <v-img
                  class="white--text"
                  height="200px"
                  src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
                >
                  <v-container fill-height fluid>
                    <v-layout fill-height align-end justify-center >
                      <v-flex  xs12 align-self-center  flexbox>
                        <v-layout justify-center >
                        <div>

                        
                        <v-avatar 
            
                        color="grey"
                        size="150"
                        
                      >
                        <v-img src="https://peru21.pe/resizer/O66CK7KA9FVHf7okINUBoIKhJ10=/940x569/smart/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/WEFZCRIDLZAAJKE5FTQBJXBLYQ.jpg"></v-img>

                      </v-avatar>
                      </div>
                        </v-layout>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-img>
                <v-card-title primary-title>
                  <div>
                    <h3 class="headline mb-0">Kangaroo Valley Safari</h3>
                    <div> {{ card_text }} </div>
                  </div>
                </v-card-title>
               
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


export default {
    components:{
      GChart
    },
  data() {
    return {
    
       card_text: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
     e1:0,
     name:"",
     terminosDialog:false,
     checkbox:0,
    chartsLib: null, 
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Year', 'Sales', 'Expenses', 'Profit'],
        ['2014', 1000, 400, 200],
        ['2015', 1170, 460, 250],
        ['2016', 660, 1120, 300],
        ['2017', 1030, 540, 350]
      ]
    };
  },
   computed: {
     chartOptions () {
      if (!this.chartsLib) {return null}
      
      return this.chartsLib.charts.Bar.convertOptions({
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017'
        },
        bars: 'vertical', // Required for Material Bar Charts.
        hAxis: { format: 'decimal' },
        
        height: 400,
        colors: ['#1b9e77', '#d95f02', '#7570b3']
      })
    }
  },
  methods: {
     onChartReady (chart, google) {
      
      this.chartsLib = google
      
    },
    openTerminosCondiciones(){
      alert("hello")
      
      
    }
  }
};
</script>
