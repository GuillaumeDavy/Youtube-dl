FROM python:3.9-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install youtube-dl
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "launchserver.py" ]