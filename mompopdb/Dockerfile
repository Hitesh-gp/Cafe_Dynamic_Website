# Use the official MySQL image
FROM mysql:5.7

# Set the environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=Msois@123
ENV MYSQL_DATABASE=mom_pop_db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Msois@123

# Copy the database initialization script into the container
COPY ./create-db.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306

