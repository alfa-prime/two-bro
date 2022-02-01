FROM python:slim

WORKDIR /usr/src/two-bro/

#утсановка виртуального окружения - не уверен пока надо или нет
#RUN pip install --upgrade pip; pip install virtualenv
#
#RUN virtualenv env
#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./run.sh .
RUN chmod a+x run.sh

COPY . .

CMD ["./run.sh"]