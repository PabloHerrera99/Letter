FROM python:3
RUN git clone https://github.com/PabloHerrera99/Letter.git
WORKDIR /Letter
CMD ["python3", "-m", "test"]