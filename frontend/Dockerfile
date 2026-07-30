FROM node:22-bookworm

WORKDIR /workspace/simple-web-app/frontend

COPY package*.json ./
RUN npm ci

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
