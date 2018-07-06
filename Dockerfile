FROM python:3

RUN pip install requests==2.18.4 click==6.7
COPY . .
CMD python sample_bot.py

