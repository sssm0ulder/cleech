<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!--<header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>-->
  <v-app id="inspire">
    <v-main class="bg-grey-lighten-3">
      <v-container>
        <v-row>
          <v-col
            cols="6"
            sm="6"
            offset="3"
          >
            <h1 class="block-params">Cleech</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            cols="6"
            sm="6"
            offset="3"
          >
            <RouterView />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      links: [
        'Dashboard',
        'Messages',
        'Profile',
        'Updates',
      ],
    }),
  }
</script>

<style scoped>
  .bg-grey-lighten-3 {
    background-color: #F6F6FB !important;
  }
  .wrapper {
    width: 1000px;
    place-items: flex-start;
    flex-wrap: wrap;
  }
  .block-params {
    margin-top: 29px;
    border-radius: 7px;
    max-width: 80%;
    margin-left: 10%;
    margin-right: 10%;
  }
</style>
