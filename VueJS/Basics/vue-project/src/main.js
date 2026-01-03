import { createApp } from 'vue'         // start vue app 
import { createPinia } from 'pinia'     // create pinia store instance, glboal state management, shares state that all comps can access to

import App from './App.vue'     // import root component 
import router from './router'   // router instance for app pages, otherwise single page only 

const app = createApp(App)      // create Vue app instance 

app.use(createPinia())          // create Pinia store instance, can use useStore() 
app.use(router)                 // register Vue router with the app 

app.mount('#app')
