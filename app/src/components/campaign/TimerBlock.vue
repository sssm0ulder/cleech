<template>
  <div class="block-params">
    <v-card class="mx-auto ps-2">
	   <v-card-item>
	     <div>
	       <div class="text-h6 mb-1 mt-2 titles">
	         Таймер
	       </div>
	       <div class="text-caption mt-2 texts">Введите дату и время завершения конкурса. Время по МСК</div>
	     </div>
	   </v-card-item>
	   <v-card-actions>
	      <v-switch
		    v-model="ex11"
		    hide-details
		    color="success"
		    true-value="Включено"
		    false-value="Выключено"
		    :label="`${ex11}`"
		  ></v-switch>
	   </v-card-actions>
  	</v-card>
  </div>
</template>


<script>
  export default {
    data: () => ({
      ex11: 'Выключено',
    }),
  }
</script>

<style>
  @import '@/assets/custom.css';
</style>