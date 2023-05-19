FROM node:alpine

USER node
WORKDIR /home/node/

COPY ./backend /home/node/backend
COPY ./frontend /home/node/frontend

EXPOSE 4000

WORKDIR /home/node/backend/
CMD [ "npm", "start" ]