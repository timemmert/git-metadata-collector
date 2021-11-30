FROM base-metadata-collector:latest

COPY src/ /src/
COPY demo/ /demo/
RUN mkdir out

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN python3 src/analyze_metadata.py --scan-path demo --out-folder out
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN cat out/*.json
RUN ls out
#RUN graal cocom https://github.com/fkautz/serve --git-path /tmp/graal-cocom > /graal-cocom.test