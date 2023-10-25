FROM python:3.8.13

# Install the necessary dependencies
RUN pip3 install ovmsclient numpy opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

CMD ["python3"]

