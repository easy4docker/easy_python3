# easy_python3

command line to run docker container

- docker contaniner stop -f easydocker-python-container
- docker contaniner rm -f easydocker-python-container
- docker image rm -f easydocker-python-image

- docker build -f dockerFile -t easydocker-python-image .
- docker run -it --name easydocker-python-container easydocker-python-image 
