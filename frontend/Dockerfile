# Temporary container for the build	
FROM node:22-alpine AS build
WORKDIR /frontend
COPY package*.json ./
RUN rm -rf node_modules package-lock.json && npm install
COPY . .
RUN npm run build

FROM nginx:alpine	
COPY nginx.conf /etc/nginx/nginx.conf	
COPY --from=build /frontend/dist /usr/share/nginx/html	
EXPOSE 80	
CMD ["nginx", "-g", "daemon off;"]	
