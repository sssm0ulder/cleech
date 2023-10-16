<script setup>
import NameBlock from '../components/campaign/NameBlock.vue'
import ConditionsBlock from '../components/campaign/ConditionsBlock.vue'
import DiscriptionBlock from '../components/campaign/DiscriptionBlock.vue'
import AvatarBlock from '../components/campaign/AvatarBlock.vue'
import TimerBlock from '../components/campaign/TimerBlock.vue'

import { storeToRefs } from 'pinia';

import { useAuthStore } from '@/stores/auth.store.js';

const authStore = useAuthStore();
const { user: authUser } = storeToRefs(authStore);

</script>

<template>
  <main>
    <div v-if="authUser">
      <h3 class="block-params">Создать Клич, {{ authUser.username }}</h3>

      <div class="block-params">
        <v-card elevation="0" class="mx-auto ps-2 text-inner-offset">
         <v-card-item>
           <div>
             <div class="text-h6 mb-1 mt-3 titles">
               Название
             </div>
             <div class="text-caption mt-2 texts">Заголовок который увидят подписчики<br>Например: Xbox за подписку</div>
           </div>
         </v-card-item>
         <v-card-actions>
           <v-text-field
              variant="outlined"
              v-model="task_name"
            ></v-text-field>
         </v-card-actions>
        </v-card>
      </div>

      <div class="block-params">
        <v-card elevation="0" class="mx-auto ps-2 text-inner-offset">
         <v-card-item>
           <div>
             <div class="text-h6 mb-1 mt-3 titles">
               Условия
             </div>
             <div class="text-caption mt-2 texts">Задания для участников розыгрыша</div>

             <div class="block-card">
              <v-card style="background: #F9F9F9;" class="mx-auto ps-2 text-inner-offset">
               <v-card-item>
                 <div>
                   <div class="text-h6 mb-1 mt-2 titles">
                     Подписаться
                   </div>
                   <div class="block-card">
                      <v-card style="background: #F9F9F9;" class="mx-auto ps-2 text-inner-offset">
                       <v-card-item>
                         <div>
                           <div class="text-h6 mb-1 mt-2 titles">
                            <v-row style="margin-top: 1%">
                              <v-col
                                cols="1"
                                sm="1"
                              >
                                <v-btn
                                  class="telegram-btn ma-2"
                                  color="purple"
                                  style="
                                    min-width: 36px !important;
                                    border-radius: 30px !important;
                                    background-color: rgb(84, 169, 235) !important;
                                    padding: 0px;
                                    margin-top: -4px !important;
                                    margin-left: 0px !important;
                                  "
                                >
                                  <font-awesome-icon style="padding: 5px;" icon="fa-solid fa-paper-plane" />
                                </v-btn>
                              </v-col>
                              <v-col
                                cols="10"
                                sm="10"
                              >
                                <div style="margin-left: 1%">
                                  Подписка на Телеграм канал/группу
                                  <div class="text-caption mt-2 texts">Введите адреса каналов куда вести читателей</div>

                                </div>
                              </v-col>
                             </v-row>
                           </div>
                         </div>
                       </v-card-item>
                       <v-row>
                        <v-col
                          cols="10"
                          sm="10"
                          offset="1"
                        >
                          <div style="margin-left: 1%; margin-bottom: 5%">
                           <v-card-actions style="padding-bottom: 0px;">
                             <v-text-field
                                class="text-input-white"
                                v-model="task_chan"
                                variant="outlined"
                              ></v-text-field>
                           </v-card-actions>
                           <v-card-item style="padding-top: 0px;">
                             <div>
                               <div class="text-caption mt-2 texts">Добавьте бота <b style="color: #001AFF">@CleechProjectBot</b> в администраторы. <br>
                                Он будет проверять подписки участников</div>
                             </div>
                           </v-card-item>
                           <v-card-actions>
                            <v-btn style="background-color: #F1EFFF" variant="flat" class="btn-check-channel text-blue">
                              <p class="normal-text">Проверить</p>
                            </v-btn>
                           </v-card-actions>
                          </div>
                        </v-col>
                      </v-row>
                      </v-card>
                   </div>
                 </div>
               </v-card-item>
              </v-card>
            </div>

           </div>
         </v-card-item>
        </v-card>
      </div>

      <div class="block-params">
        <v-card elevation="0" class="mx-auto ps-2 text-inner-offset">
         <v-card-item>
           <div>
             <div class="text-h6 mb-1 mt-3 titles">
               Таймер
             </div>
             <v-switch
              v-model="isEnabledDate"
              value="true"
              color="success"
              true-value="Включено"
              false-value="Выключено"
              :label="`${isEnabledDate}`"
             />
             <div v-if="isEnabledDate == 'Включено'" class="text-caption mt-2 texts">Введите дату и время завершения конкурса. Время по МСК</div>
           </div>
         </v-card-item>
         <v-card-actions v-if="isEnabledDate == 'Включено'" style="margin-bottom: 2%">
           <VueDatePicker
            v-model="date"
            :teleport="true"
            locale="ru"
            :min-date="new Date()"
            cancelText="Сбросить"
            selectText="Выбрать"
            ></VueDatePicker>
         </v-card-actions>
        </v-card>
      </div>

      <div class="block-params">
        <v-card elevation="0" class="mx-auto ps-2 text-inner-offset">
         <v-card-item>
           <div>
             <div class="text-h6 mb-1 mt-3 titles">
               Описание розыгрыша
             </div>
             <div class="text-caption mt-2 texts">Расскажите о призах, организаторах или сроках. <br>
              Описание увидят участники розыгрыша. </div>
           </div>
         </v-card-item>
         <v-card-actions>
           <v-text-field
              v-model="task_disc"
              variant="outlined"
            ></v-text-field>
         </v-card-actions>
        </v-card>
      </div>

      <div class="mt-6 block-params d-flex justify-center mb-6">
        <v-btn
          variant=""
          style="background: #001AFF;"
          class="btn-create-task"
          color=""
          v-on:click="createTask(authUser)"
        >
          <p style="color: #FFFFFF;" class="normal-text btn-create-task-text">Создать клич</p>
        </v-btn>
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

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'App',

  components: {
    ButtonLogin,
    VueDatePicker
  },

  data () {
    return {
      'task_chan': 'https://t.me/',
      'task_disc': '',
      'task_name': '',
      'date': new Date(),
      'isEnabledDate': 'Включено',
    }
  },

  methods: {
    loginWithTelegram(data) {
      const authStore = useAuthStore();
      authStore.login(data)
    },

    createTask(user) {
      if (this.isEnabledDate == 'Включено') {
        var date = this.date;
      } else {
        var date = null;
      }

      this.axios.post('http://127.0.0.1:8000/api/task/create', {
        channel_link: this.task_chan,
        discription: this.task_disc,
        name: this.task_name,
        user: user,
        timer: date
        //avatar: ,
      })
      .then((response) => {
        if ( response.status == 201 ) {
          console.log('DONE')
          alert('DONE')
          this.$router.push('/task')
        } else if ( response.status == 200 ) {
          console.log('DONE')
          alert('Клич уже был создан с данными параметрами')
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
  .btn-check-channel {
    height: 45px;
    width: 150px;
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
  .text-input-white input {
    background-color: #fff !important;
  }
</style>
