<script setup>
import AuthStepBlock from '../components/landing/AuthStepBlock.vue'
import SubscribeStepBlock from '../components/landing/SubscribeStepBlock.vue'
import DoneStepBlock from '../components/landing/DoneStepBlock.vue'

import HeaderBlock from '../components/landing/HeaderBlock.vue'
import DiscriptionBlock from '../components/landing/DiscriptionBlock.vue'
import TimerBlock from '../components/landing/TimerBlock.vue'
import ScoreBlock from '../components/landing/ScoreBlock.vue'

import { storeToRefs } from 'pinia';

import { useAuthStore } from '@/stores/auth.store.js';

const authStore = useAuthStore();
const { user: authUser } = storeToRefs(authStore);
</script>

<template>
  <main>
    <HeaderBlock />
    <DiscriptionBlock />
    <TimerBlock />
    <ScoreBlock />

    <div v-if="authUser">
      <SubscribeStepBlock number="1" complete="ready" />
      <DoneStepBlock number="2" complete="notready" />
    </div>
    <div v-else>
      <AuthStepBlock complete="ready" />
      <SubscribeStepBlock number="2" complete="notready" />
      <DoneStepBlock number="3" complete="notready" />
    </div>
  </main>
</template>

<style>
	.block-params {
		margin-top: 10px;
	}
</style>
