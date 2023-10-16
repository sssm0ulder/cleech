<template>
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
</template>

<style scoped>
	@import '@/assets/custom.css';

.inherit-color {
	background-color: inherit !important;
}

.normal-text {
	text-transform: none;
}
</style>

<script>
import { ButtonLogin } from 'televue'

//user.first_name + user.last_name + user.id + user.username
export default {
  name: 'App',

  components: {
    ButtonLogin
  },

  data () {
    return {}
  },

  methods: {
    loginWithTelegram(user) {
    	console.log(user)
      	this.axios.post('http://127.0.0.1:8000/api/telegram/auth', {
      		first_name: user.first_name,
      		last_name: user.last_name,
      		username: user.username.toString(),
      		user_id: user.id.toString(),
      	})
      	.then((response) => {
      	  console.log(response.data)
      	})
    }
  }
}
</script>
