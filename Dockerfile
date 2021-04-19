FROM alpine:3.7
EXPOSE 5000
ENTRYPOINT ["python", "source/app.py"]

