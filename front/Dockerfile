# build stage
FROM node:lts-alpine as build-stage

WORKDIR /code

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]