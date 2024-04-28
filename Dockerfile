FROM python:3.11.0

WORKDIR /run3
COPY ./requirements.txt /run3/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*



COPY  . /run3/

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "run3.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD ["streamlit", "run","run.py", "--host", "0.0.0.0", "--port", "8501"]