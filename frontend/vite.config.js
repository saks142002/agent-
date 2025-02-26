
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5174,
    strictPort: true,
    hmr: {
      clientPort: 443,
      host: 'ee48701a-994f-45d3-a784-bf08f97a816e-00-3074n6145ecti.picard.replit.dev'
    },
    allowedHosts: 'all'
  }
})
