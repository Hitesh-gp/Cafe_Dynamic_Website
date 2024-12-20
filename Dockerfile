FROM mysql:5.7 AS mysql_stage

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=Msois@123
ENV MYSQL_DATABASE=mom_pop_db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Msois@123

# Copy the database initialization script into the container

COPY mompopcafe/mompopdb/create-db.sql /docker-entrypoint-initdb.d/

# Expose MySQL port
EXPOSE 3306

# Stage 2: Apache and PHP setup
FROM php:8.0-apache

# Install necessary PHP extensions for MySQL and other requirements
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Enable Apache mod_rewrite for URL rewriting if needed
RUN a2enmod rewrite

# Copy the MySQL stage database setup files from the previous stage
COPY --from=mysql_stage /docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/

# Copy PHP application files into the container
COPY ./mompopcafe /var/www/html/

# Set the correct permissions for the web directory (if needed)
RUN chown -R www-data:www-data /var/www/html

# Expose the Apache port
EXPOSE 80

# Start both MySQL and Apache services
CMD service mysql start && apache2-foreground
