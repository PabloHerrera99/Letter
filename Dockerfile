FROM python:3
RUN git clone https://github.com/
WORKDIR /carpeta
CMD ["python3", "-m", "test"]