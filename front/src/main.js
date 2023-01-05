import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vue3GoogleLogin from 'vue3-google-login'


// const app = createApp(App).use(store).use(router).mount('#app')
const app = createApp(App)

app.use(vue3GoogleLogin, {
    clientId: '380831271033-aqb513sp8g0l7u8mg5lp888m3sb6d5tk.apps.googleusercontent.com'
})
app.use(store)
app.use(router)
app.mount('#app')

