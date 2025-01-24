import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"


// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  // Proxy enabled when dev server being used
  server: {
    proxy: {
      '/api': {
        target: "http://localhost:5000",
      },
    },
  },
});
