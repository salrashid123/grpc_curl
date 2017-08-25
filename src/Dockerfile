FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y  unzip curl python openssl python-setuptools python-pip python-dev build-essential nghttp2 libnghttp2-dev  libssl-dev

RUN curl -OL https://curl.haxx.se/download/curl-7.54.0.tar.bz2 && \
    tar -xvjf curl-7.54.0.tar.bz2 && \
    cd curl-7.54.0 && \
    ./configure --with-nghttp2 --with-ssl && \
    make && \
    make install && \    
    ldconfig 

RUN curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip && \
    unzip protoc-3.2.0-linux-x86_64.zip -d protoc3 && \
    mv protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/

RUN pip install grpcio-tools hexdump

ADD . /app
WORKDIR /app
RUN python -m grpc_tools.protoc -I .  --python_out=. --grpc_python_out=. echo.proto 
EXPOSE 8081
EXPOSE 50051

#ENTRYPOINT ["python", "/app/server.py"]
#ENTRYPOINT ["python", "/app/client.py", "main.esodemoapp2.com" , "50051"]
