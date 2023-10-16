import { defineStore } from 'pinia';
import axios from 'axios'


export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user'))
    }),
    actions: {
        login(user) {
            if (!user.username) {
                alert('You are bot')
                return
            }
            axios.post('http://127.0.0.1:8000/api/auth', {
                first_name: user.first_name,
                last_name: user.last_name,
                username: user.username,
                user_id: user.id,
                tg_hash: user.hash,
                //auth_date: user.auth_date,
            })
            .then((response) => {
                if ( response.status == 200 ) {
                    this.user = response.data.data;
                    console.log(JSON.stringify(response.data.data))
                    localStorage.setItem('user', JSON.stringify(response.data.data));
                }
            })

            //router.push('/');
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
        }
    }
});
