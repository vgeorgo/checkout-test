FROM node:14-alpine

WORKDIR /usr/src

COPY ./src/package*.json ./
RUN npm install

COPY ./src ./

EXPOSE 8080
ENTRYPOINT [ "npm", "run", "serve" ]