<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      src="https://decidesoluciones.es/wp-content/uploads/2019/04/Inteligencia-Artificial-en-positivo-soluciones-en-positivo-cambiar-mundo-IA-innovacion-1200x545_c-1090x545.jpg"
    >
      
      <div class="hidden-sm-and-down font-weight-light headline" >Depredetector</div>
      

      
    </v-app-bar>

    <v-content>
      <Home/>
    </v-content>
    
  </v-app>
</template>

<script>
import Home from './components/Home'

export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
  
};
</script>
