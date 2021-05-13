FROM nginx: latest
MAINTAINER Daniel Prata
COPY /public /var/www/public
COPY /docker/config/nginx.config /etc/nginx/nginx.config
EXPOSE 80 443
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]