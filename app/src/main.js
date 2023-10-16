import { createApp } from 'vue'

import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

import './assets/main.css'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faPaperPlane } from '@fortawesome/free-solid-svg-icons'
import { faTelegram } from '@fortawesome/free-brands-svg-icons'
import { faCopy } from '@fortawesome/free-regular-svg-icons'

library.add(faPaperPlane, faCopy, faTelegram)

const vuetify = createVuetify({
  components,
  directives,
})

const pinia = createPinia()

const app = createApp(App)

let user = localStorage.getItem('user');
if (user) {
	user = JSON.parse(user)
	console.log(user.token)
    axios.defaults.headers.common['Authorization'] = `Bearer ${user.token}`
}

app.use(router)
app.use(vuetify)
app.use(pinia)
app.use(VueAxios, axios)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
