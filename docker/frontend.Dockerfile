FROM node:18-alpine

WORKDIR /app

# Package config is copied from context (frontend)
COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
