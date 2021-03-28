FROM python

RUN pip install requests
RUN pip install simplejson

ADD asignacion7.py /

CMD ["python", "./asignacion7.py"]


