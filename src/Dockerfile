FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y  unzip curl python3 openssl python3-setuptools python3-pip python3-dev build-essential  libssl-dev


RUN curl -OL https://github.com/google/protobuf/releases/download/v3.13.0/protoc-3.13.0-linux-x86_64.zip && \
    unzip protoc-3.13.0-linux-x86_64.zip -d protoc3 && \
    mv protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/

RUN pip3 install grpcio-tools hexdump

ADD . /app
WORKDIR /app
RUN python3 -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. echo.proto 
EXPOSE 50051

#ENTRYPOINT ["python", "/app/server.py"]
#ENTRYPOINT ["python", "/app/client.py", "server.domain.com" , "50051"]
