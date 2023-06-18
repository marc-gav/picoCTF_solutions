FROM arm64v8/debian:latest

RUN apt-get update && apt-get install -y gcc
COPY ./chall.S .
RUN gcc -o chall chall.S
CMD [ "./chall", "4004594377", "4110761777"]