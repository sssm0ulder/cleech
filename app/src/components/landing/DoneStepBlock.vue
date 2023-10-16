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
			          Ты зарегистрирован!
			        </div>
			        <p class="text-black">Теперь ты в списке участников! </p>
			        <div style="margin-top: 10px;" class="text-h6 mb-1 text-blue">
			          Псс.. Хочешь больше баллов?
			        </div>
			        <p class="text-black">Пригласи друга на конкурс, получи <b>+2 балла</b> за каждого участника</p>
			    	<p class="text-black">Ссылка для приглашения:</p>
			          <v-container class="bg-surface-variant inherit-color">
				        <v-row
					      class="mb-6"
					      no-gutters
					    >
					      <v-col cols="8">
					      	<v-btn width="100%" variant="outlined">
					      	  <font-awesome-icon style="padding: 5px; color: #B1B4C9;" icon="fa-regular fa-copy" />
							  <p style="color: #333333;" class="normal-text">cleech.com/invite/6qn6lcd</p>
							</v-btn>
					      </v-col>
					      <v-col cols="4">
					      	<v-btn variant="outlined" class="text-blue ml-4">
							  <p class="normal-text">0 друзей</p>
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
			      	<div style="color: #9D9D9D !important; padding-top: 0.7rem;" class="text-h6 mb-1 text-blue">
			          Ты зарегистрирован!
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

}
</script>