FROM alpine:latest
WORKDIR /src/
RUN apk update && apk add \
    privoxy \
    curl \
    && rm -rf /var/cache/apk/*
# copy in our privoxy config file
# setting this so we can drop it as a volume mount in k8
# allowing for new configs without rebuilding of image.
COPY ./config/* /etc/privoxy/
# make sure files are owned by privoxy user
RUN chown -R privoxy /etc/privoxy/*
USER privoxy
ENTRYPOINT [ "/bin/sleep", "8000"]
# CMD ["/src/config/"]
