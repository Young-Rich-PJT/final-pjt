import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';



Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          options: {
            customProperties: true,
          },

          light: {
            // fonts: {
            //   family: 'BMDOHYEON',
            //   url: '../../../../assets/fonts/BMDOHYEON_ttf.ttf',
            // },
            primary: '#03A9F4',
            secondary: '#b0bec5',
            accent: '#8c9eff',
            error: '#b71c1c',
            my_color: '#ffffff',
          },
        
        },
      },
    })