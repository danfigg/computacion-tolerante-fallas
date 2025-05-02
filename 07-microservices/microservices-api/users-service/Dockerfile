FROM node:20

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de archivos
COPY . .

# Exponer el puerto (ajústalo si tu app usa otro)
EXPOSE 4000

# Comando para arrancar
CMD ["npm", "run", "dev"]
