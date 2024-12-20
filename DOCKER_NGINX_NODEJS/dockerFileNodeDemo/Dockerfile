FROM node:16
RUN mkdir -p C:\Users\고대영\tools\dockerFile //이 두개는 
WORKDIR C:\Users\고대영\tools\dockerFile      //없어도 되나
COPY package.json ./
RUN npm install 
COPY ./ .
EXPOSE 8000
CMD ["node","index.js"]
