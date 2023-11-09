FROM python
WORKDIR /usr/src/python-dsm
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8080
CMD ["/bin/bash"]
