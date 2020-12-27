# easy_python3

command line to run docker container

git clone https://github.com/easy4docker/easy_python3.git
cd easy_python3
- docker container stop easydocker-python-container
- docker container rm easydocker-python-container
- docker image rm easydocker-python-image

- docker build -f dockerFile -t easydocker-python-image .
- docker run -it  --name easydocker-python-container easydocker-python-image 
