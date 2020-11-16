FROM node:10.19.0

# set work directory
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install

# copy project
COPY . /app

CMD npm run serve