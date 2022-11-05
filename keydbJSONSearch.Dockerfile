ARG KEY_DB_VERSION=v6.2.2
ARG REDISEARCH_VERSION=v2.4.15
ARG BUILD_BIN=/build/bin
#----------------------------------------------------------------------------------------------
FROM redislabs/redisearch:latest as rs

# CMD ls /usr/lib/x86_64-linux-gnu/

FROM eqalpha/keydb:x86_64_${KEY_DB_VERSION}

ENV LIBDIR /usr/lib/redis/modules
RUN mkdir -p ${LIBDIR}
COPY --from=rs /usr/lib/ /usr/lib/
COPY --from=rs /usr/lib/redis/modules ${LIBDIR}/

RUN chmod 777 /usr/lib/redis/modules/redisearch.so

 CMD keydb-server /etc/keydb/keydb.conf --loadmodule /usr/lib/redis/modules/redisearch.so --loadmodule /usr/lib/redis/modules/rejson.so --server-threads 2 --requirepass ${KEYDB_PASSWORD}
