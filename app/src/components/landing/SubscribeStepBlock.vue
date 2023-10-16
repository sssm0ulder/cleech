<script setup>
import { storeToRefs } from 'pinia';

import { useAuthStore } from '@/stores/auth.store.js';

const authStore = useAuthStore();
const { user: authUser } = storeToRefs(authStore);

</script>

<template>
	<div v-if="complete == 'ready'" class="block-params">
    <v-container class="bg-surface-variant inherit-color">
	    <v-row
	      class="mb-6"
	      no-gutters
	    >
	      <v-col cols="2">
	        <v-avatar variant="outlined" color="info" size="x-large">
		      {{ number }}
		    </v-avatar>
	      </v-col>
	      <v-col cols="8">
	        <div style="display: grid">
		    	<div style="display: block">
			      	<div style="padding-top: 0.7rem;" class="text-h6 mb-1 text-blue">
			          Подпишись
			        </div>
			        <p class="text-black">Подпишись на телеграм канал <b class="text-blue">@test_chan222</b></p>
				    <v-row
					  class="mb-6 mt-3"
					  no-gutters
					>
					  <v-col cols="8">
					    <v-btn v-bind:href="subscribe_link" target="_blank" width="95%" style="height: 50px; background-color: #33BDF1 !important;" color="info">
					      <font-awesome-icon style="padding: 5px;" icon="fa-solid fa-paper-plane" />
						  <p class="normal-text">Подписаться</p>
						</v-btn>
					  </v-col>
					  <v-col cols="4">
					    <v-btn v-on:click="checkSubscribe(authUser)" style="height: 50px;" variant="outlined" class="text-blue">
						  <p class="normal-text">Проверить</p>
						</v-btn>
				      </v-col>
					</v-row>
				</div>
			  </div>
	      </v-col>
	    </v-row>
	</v-container>
	</div>
	<div v-if="complete == 'done'" class="block-params">
    <v-container class="bg-surface-variant inherit-color">
	    <v-row
	      class="mb-6"
	      no-gutters
	    >
	      <v-col cols="2">
	        <v-avatar variant="outlined" color="info" size="x-large">
		      {{ number }}
		    </v-avatar>
	      </v-col>
	      <v-col cols="8">
	        <div style="display: grid">
		    	<div style="display: block">
			      	<div style="padding-top: 0.7rem;" class="text-h6 mb-1 text-blue">
			          Подпишись
			        </div>
				</div>
			  </div>
	      </v-col>
	    </v-row>
	</v-container>
	</div>
	<div v-if="complete == 'notready'" class="block-params">
    <v-container class="bg-surface-variant inherit-color">
	    <v-row
	      class="mb-6"
	      no-gutters
	    >
	      <v-col cols="2">
	        <v-avatar style="color: #9D9D9D !important;" variant="outlined" color="info" size="x-large">
		      {{ number }}
		    </v-avatar>
	      </v-col>
	      <v-col cols="8">
	        <div style="display: grid">
		    	<div style="display: block">
			      	<div style="color: #9D9D9D !important;padding-top: 0.7rem;" class="text-h6 mb-1 text-blue">
			          Подпишись
			        </div>
				</div>
			  </div>
	      </v-col>
	    </v-row>
	</v-container>
	</div>
</template>

<style scoped>
.inherit-color {
	background-color: inherit !important;
}

.normal-text {
	text-transform: none;
}

</style>

<script>
export default {
  props: ['number', 'complete'],
  name: 'App',

  data () {
    return {
    	subscribe_link: 'https://t.me/test_chan222',
    	user_id: '495363986'
    }
  },

  methods: {
    checkSubscribe(user) {
    	console.log('test')
    	console.log(user)
      	this.axios.post('http://127.0.0.1:8000/api/telegram/check', {
      		link: this.subscribe_link,
      		user_id: user.user_id,
      	})
      	.then((response) => {
      	  console.log(response)
      	  if ( response.status == 200 ) {
            console.log('DONE')
            alert('DONE')
            this.complete = 'done'
            //this.$router.push('/task')
          }
      	})
      	.catch(function (error) {
      	  if (error.response) {
      	  	if ( error.response.status == 400 ) {
          	  alert('User not subscribed')
          	}
      	  }
      	})
    }
  }
}
</script>