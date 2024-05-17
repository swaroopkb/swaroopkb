FROM python
ENV LISTEN_PORT=5000
EXPOSE 5000
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD [ "python","api.py"]
