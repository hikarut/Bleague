FROM python:3
USER root

RUN apt-get update
RUN apt-get install -y vim less
RUN apt-get install -y zsh less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests
RUN pip install feedparser
RUN pip install pprint
RUN pip install --upgrade firebase-admin
RUN pip install beautifulsoup4

env LANG=ja_JP.UTF-8
env LANGUAGE=ja_JP:ja
env LC_ALL=ja_JP.UTF-8
env TZ=Asia/Tokyo

EXPOSE 8000
CMD ["bash"]
