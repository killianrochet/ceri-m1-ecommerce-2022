# build stage
FROM node:lts-alpine as build-stage

WORKDIR /code

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run serve

# production stage
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /code/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]