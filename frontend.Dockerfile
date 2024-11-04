# Use Node.js base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the application code
COPY . .

# Build the frontend
RUN npm run build

# Expose the default port
EXPOSE 3000

# Serve the build using a static file server
CMD ["npx", "serve", "-s", "build"]
