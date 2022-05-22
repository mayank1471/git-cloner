FROM ubuntu:20.04

MAINTAINER Mayank Soni<mayank.soni@mayanksoni.tech>
ENV SRC_DIR /usr/local/git-cloner

COPY hosts-to-scan .

RUN apt update \
    && apt upgrade -y \
    && apt install -y openssh-client git python3 pip \
    && ssh-keygen -t rsa -N '' -C "svc.git-cloner@mayanksoni.tech" -f "id_rsa" \
    && mkdir -p /root/.ssh/ && touch /root/.ssh/known_hosts \
#    && ssh-keyscan -t rsa -f hosts-to-scan >> /root/.ssh/known_hosts \
    && pip install fastapi uvicorn[standard] \
    && mkdir -p ${SRC_DIR} \
    && cd ${SRC_DIR}

WORKDIR ${SRC_DIR}

ENV GIT_SSH_COMMAND ssh -i /id_rsa

COPY known_hosts /root/.ssh/

COPY *.py ${SRC_DIR}/

EXPOSE 8000

ENTRYPOINT ["python3", "-m","uvicorn","main:app","--reload","--host" ,"0.0.0.0"]