FROM mozillamarketplace/centos-python27-mkt:0.5

RUN yum install -y openresty
ENV PATH /opt/openresty/nginx/sbin/:$PATH

ADD nginx.conf /etc/nginx/nginx.conf
ADD lang.lua /etc/nginx/
ADD payments-env.conf /etc/nginx/conf.d/payments-env.conf
ADD locales /srv/locales

RUN mkdir /var/log/nginx/
RUN cp /opt/openresty/nginx/conf.example/mime.types /etc/nginx/

EXPOSE 80

CMD ["/opt/openresty/nginx/sbin/nginx" "-c" "/etc/nginx/nginx.conf"]
