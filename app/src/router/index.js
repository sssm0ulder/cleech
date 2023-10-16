import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateTask from '../views/CreateTask.vue'
import ListTask from '../views/ListTask.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/task/create',
      name: 'task',
      component: CreateTask
    },
    {
      path: '/task',
      name: 'task_list',
      component: ListTask
    },
  ]
})

export default router
