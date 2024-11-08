# Use the official PHP image with Apache support
FROM php:8.0-apache

# Install necessary PHP extensions for MySQL and other requirements
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Enable Apache mod_rewrite for URL rewriting if needed
RUN a2enmod rewrite

# Copy your PHP files into the container
COPY ./mompopcafe /var/www/html/

# Set permissions on the web directory (if needed)
RUN chown -R www-data:www-data /var/www/html

# Expose the port Apache will run on (80 by default)
EXPOSE 80

# Set the default command to start Apache in the foreground
CMD ["apache2-foreground"]
