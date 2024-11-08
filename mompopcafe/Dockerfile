# Use PHP 7.4 with Apache
FROM php:7.4-apache

# Update sources list to avoid issues with Debian repositories
RUN sed -i 's|http://deb.debian.org/debian/|http://ftp.debian.org/debian/|g' /etc/apt/sources.list

# Install necessary PHP extensions and update dependencies
RUN apt-get update -y && \
    apt-get install -y libzip-dev zip && \
    docker-php-ext-install mysqli pdo_mysql

# Copy application source code to the Apache web root
COPY . /var/www/html/

# Set proper permissions for the web root directory
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

# Expose port 80 to access the application
EXPOSE 80

# Restart Apache in the foreground to keep the container running
CMD ["apache2-foreground"]
