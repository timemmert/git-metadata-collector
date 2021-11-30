FROM base-metadata-collector:latest

WORKDIR /code

COPY src/ .

ENTRYPOINT ["python3", "./analyze_metadata.py"]
