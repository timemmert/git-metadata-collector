FROM base-metadata-collector:latest

COPY src/ /src/
COPY demo/ /demo/
RUN mkdir out

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN python3 src/analyze_metadata.py --repo-path demo/perceval --out-file out/out.json
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN cat out/out.json
RUN graal cocom https://github.com/fkautz/serve --git-path /tmp/graal-cocom > /graal-cocom.test