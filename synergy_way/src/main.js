import Vue from 'vue'
import App from './App.vue'
import store from './store/index.js'

import BootstrapVue from "bootstrap-vue";
import * as VeeValidate from 'vee-validate';


import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

Vue.use(BootstrapVue)
Vue.use(VeeValidate);

new Vue({
  store,
  render: h => h(App),
}).$mount('#app');
