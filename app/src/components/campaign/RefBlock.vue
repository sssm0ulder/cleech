<template>
  <div class="block-params">
    <v-card class="mx-auto ps-2">
	   <v-card-item>
	     <div>
	       <div class="text-h6 mb-1 mt-2 titles">
	         Реферальная программа
	       </div>
	       <div class="text-caption  mt-2 texts">Участники смогут привлекать друзей и знакомых за баллы</div>
	     </div>
	   </v-card-item>
	   <v-card-actions>
	    <v-switch
		    v-model="model"
		    hide-details
		    color="success"
		    true-value="Включено"
		    false-value="Выключено"
		    :label="`${model}`"
		  ></v-switch>
	      Outlined Button
	   </v-card-actions>
  	</v-card>
  </div>
</template>

<style>
  @import '@/assets/custom.css';
</style>
