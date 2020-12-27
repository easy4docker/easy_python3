# easy_python3
docker image stop -f easydocker-python-container
docker image rm -f easydocker-python-container
docker image rm -f easydocker-python-image

docker build -f dockerFile -t easydocker-python-image .
docker run -it easydocker-python-image  easydocker-python-container
