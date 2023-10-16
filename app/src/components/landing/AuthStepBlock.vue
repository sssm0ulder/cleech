<template>
	<div class="block-params">
    <v-container class="bg-surface-variant inherit-color">
	    <v-row
	      class="mb-6"
	      no-gutters
	    >
	      <v-col cols="2">
	        <v-avatar variant="outlined" color="info" size="x-large">
		      1
		    </v-avatar>
	      </v-col>
	      <v-col cols="8">
	        <div style="display: grid">
		    	<div style="display: block">
			      	<div class="text-h6 mb-1 text-blue">
			          Авторизуйся
			        </div>
			        <p class="text-black">Войди через соц сети, чтобы принять участие в конкурсе <b>Ford Boyard Collection</b></p>
			          <v-container class="bg-surface-variant inherit-color">
				        <v-row
					      class="mb-6"
					      no-gutters
					    >
					      <v-col cols="6">
					      	<ButtonLogin 
							  mode="callback" 
							  size="large"
							  bot-username="CleechProjectBot" 
							  @callback="loginWithTelegram" 
							/>
					      </v-col>
					      <v-col cols="6">
					      	<v-btn variant="outlined" class="text-blue">
							  <p class="normal-text">+2 балла</p>
							</v-btn>
					      </v-col>
					    </v-row>
					  </v-container>
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
import { ButtonLogin } from 'televue'

//user.first_name + user.last_name + user.id + user.username
export default {
  props: ['complete'],
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
