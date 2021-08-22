FROM node:14-alpine

WORKDIR /usr/src

COPY ./src .
RUN npm install

ENTRYPOINT ["npm", "run", "serve"]