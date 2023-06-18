# Fetch the PHP image from the official Docker Hub 
FROM php:7.4-apache

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Install necessary package
RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libzip-dev \
    libpng-dev \
    && docker-php-ext-install zip pdo_mysql gd

# Copy application source
COPY ./index.php /var/www/html/index.php
COPY ./flag.txt /tmp/flag.txt

# Change the ownership of the application inside docker to ensure proper access rights
RUN chown -R www-data:www-data /var/www/html/

# Expose port 80 for apache to listen on
EXPOSE 80

# Command to run when the container is started
CMD ["apache2-foreground"]

# Build the Docker image
# docker build -t my-php-app .

# Run the Docker container
# docker run -p 8080:80 -d my-php-app