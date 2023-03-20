import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import '../src/assets/css/constantes.css';

// Import the plugin here
import { domain, clientId/*, audience*/ } from './auth_config.json';
//import { Auth0Plugin } from '@/auth/index.js';
/*.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: (appState) => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname,
    );
  },
})*/

import { createAuth0 } from '@auth0/auth0-vue';

createApp(App).use(
  createAuth0({
    domain: domain,
    clientId: clientId,
    authorizationParams: {
      redirect_uri: '<MY_CALLBACK_URL>'
    }
  })
).use(store).use(router).mount('#app');
