FROM python

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /home/app

CMD streamlit run --server.port $PORT --server.address 0.0.0.0 home.py