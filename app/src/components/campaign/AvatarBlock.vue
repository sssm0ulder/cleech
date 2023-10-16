<template>
  <div class="block-params">
    <v-card class="mx-auto ps-2">
	   <v-card-item>
	     <div>
	       <div class="text-h6 mb-1 mt-2 titles">
	         Обложка
	       </div>
	       <div class="text-caption mt-2 texts">Поможет привлечь внимание. Не обязательна</div>
	     </div>
	   </v-card-item>
	   <v-card-actions>
	     <v-file-input
		    v-model="files"
		    color="deep-purple-accent-4"
		    counter
		    label="Прикрепить картинку"
		    multiple
		    placeholder="Select your files"
		    prepend-icon="mdi-paperclip"
		    variant="outlined"
		    :show-size="1000"
		  >
		    <template v-slot:selection="{ fileNames }">
		      <template v-for="(fileName, index) in fileNames" :key="fileName">
		        <v-chip
		          v-if="index < 2"
		          color="deep-purple-accent-4"
		          label
		          size="small"
		          class="me-2"
		        >
		          {{ fileName }}
		        </v-chip>

		        <span
		          v-else-if="index === 2"
		          class="text-overline text-grey-darken-3 mx-2"
		        >
		          +{{ files.length - 2 }} File(s)
		        </span>
		      </template>
		    </template>
		  </v-file-input>
	   </v-card-actions>
  	</v-card>
  </div>
</template>

<style>
  @import '@/assets/custom.css';
</style>
