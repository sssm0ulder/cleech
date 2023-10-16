import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

//import basicSsl from '@vitejs/plugin-basic-ssl'



// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  if (command === 'serve') {
    return {
      server: {
      	origin: 'https://0.0.0.0:8080',
        proxy: {
          '/api': {
            target: 'http://localhost:3000/',
            changeOrigin: true,
            secure: false,
            //rewrite: (path) => path.replace(/^\/api/, ''),
          },
        },
        cors: {
		  "origin": "*",
		  "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
		  "preflightContinue": false,
		  "optionsSuccessStatus": 204
		},
        headers: {
        	"Access-Control-Allow-Origin": "*",
    		"Access-Control-Allow-Methods": "GET,POST,DELETE,PATCH,PUT",
    		"Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
    	},
        https: false,
      },
      plugins: [
        vue(),
        //basicSsl(),
      ],
	  resolve: {
	    alias: {
	      '@': fileURLToPath(new URL('./src', import.meta.url))
	    }
	  }
    }
  } else {
  	return {
  	  server: {
        cors: {
		  "origin": "*",
		  "methods": "GET,HEAD,PUT,PATCH,POST,DELETE",
		  "preflightContinue": false,
		  "optionsSuccessStatus": 204
		},
        headers: {
        	"Access-Control-Allow-Origin": "*",
    		"Access-Control-Allow-Methods": "GET,POST,DELETE,PATCH,PUT",
    		"Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
    	},
        http: true,
      },
	  plugins: [
	    vue(),
	  ],
	  resolve: {
	    alias: {
	      '@': fileURLToPath(new URL('./src', import.meta.url))
	    }
	  },
	}
  }
})
