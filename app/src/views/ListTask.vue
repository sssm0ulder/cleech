<script setup>
import { storeToRefs } from 'pinia';

import { useAuthStore } from '@/stores/auth.store.js';

const authStore = useAuthStore();
const { user: authUser } = storeToRefs(authStore);

</script>

<template>
  <main>
    <div v-if="authUser">
      <h3 class="block-params">Мои Клич Кампании, {{ authUser.username }}</h3>

      <div class="block-params">
        <v-card elevation="0" class="mx-auto ps-2 text-inner-offset">
         <v-card-item>
           <div>
             <div class="text-h6 mb-1 mt-3 titles">
               Xbox за подписку
             </div>
             <div class="text-caption mt-2 texts">Участников: 0</div>
             <div class="text-caption mt-2 texts">Закончится через: 5 дней, 5 часов, 5 минут</div>
             <v-row class="mt-3 ml-1 mb-1">
              <font-awesome-icon style="color: rgb(84, 169, 235) !important" icon="fa-brands fa-telegram" />
               <div class="text-caption ml-2 texts">t.me/namechannel</div>
             </v-row>
           </div>
         </v-card-item>
         <v-card-actions class="mb-2">
          <v-btn style="background-color: #F1EFFF" variant="flat" class="btn-check-channel text-blue">
            <p class="normal-text">Редактировать</p>
          </v-btn>
          <v-btn style="background-color: #F1EFFF" variant="flat" class="btn-check-channel text-blue">
            <p class="normal-text">Остановить</p>
          </v-btn>
          <v-btn style="background-color: #F1EFFF" variant="flat" class="btn-check-channel text-blue">
            <p class="normal-text">Удалить</p>
          </v-btn>
         </v-card-actions>
        </v-card>
      </div>
    </div>

    <div v-else>
      <div class="block-params">
        <v-card class="mx-auto ps-2">
           <v-card-item>
             <div>
               <div class="text-h6 mb-1 mt-2 titles">
                 Авторизуйся
               </div>
               <div class="text-caption mt-2 texts">Войди через соц.сети, чтобы создавать свои кампании</div>
             </div>
           </v-card-item>
           <v-card-actions>
            <ButtonLogin 
              mode="callback" 
              size="large"
              bot-username="CleechProjectBot" 
              @callback="loginWithTelegram" 
            />
           </v-card-actions>
          </v-card>
        </div>
    </div>
  </main>
</template>

<script>
import { ButtonLogin } from 'televue'

export default {
  name: 'App',

  components: {
    ButtonLogin
  },

  data () {
    return {
      data: null
    }
  },

  async mounted() {
    if (!this.data) {
      this.data = await this.getTasks()
    }
  },

  methods: {
    loginWithTelegram(data) {
      const authStore = useAuthStore();
      authStore.login(data)
    },

    getTasks() {
      this.axios.get('http://127.0.0.1:8000/api/task/list', {
        user: this.authUser
      })
      .then((response) => {
        if ( response.status == 200 ) {
          console.log('DONE')
        }
      })
    }
  }
}
</script>

<style>
  .block-params {
    margin-top: 29px;
    border-radius: 7px;
    max-width: 80%;
    margin-left: 10%;
    margin-right: 10%;
  }
  .block-card {
    margin-top: 29px;
    margin-bottom: 29px;
    border-radius: 7px;
    max-width: 95%;
    margin-left: 2.5%;
    margin-right: 2.5%;
  }
  .field-offset {
    max-width: 95%;
    margin-left: 2.5%;
    margin-right: 3%;
  }
  .text-inner-offset {
    padding-left: 2.5% !important;
    padding-right: 1% !important;
  }
  .normal-text {
    text-transform: none;
  }
  .btn-create-task {
    height: 45px;
    width: 214px;
    border-radius: 10px;
  }
  .btn-create-task-text {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 12px;
    line-height: 136.52%;

    text-align: center;

    color: #FFFFFF;
  }
</style>
