FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]

