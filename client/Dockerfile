FROM node:17-alpine as builder

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

ARG HOST

ARG PORT

ENV HOST=$HOST

ENV PORT=$PORT

RUN ./script.sh

RUN npm run build

FROM nginx

EXPOSE 80

COPY ./nginx-server/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html


