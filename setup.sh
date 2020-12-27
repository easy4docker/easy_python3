SCR_DIR=$(cd `dirname $0` && pwd)
docker container stop easydocker-python-container
docker container rm easydocker-python-container
docker image rm easydocker-python-image

docker build -f dockerFile -t easydocker-python-image .
docker run -it  --name easydocker-python-container -v "${SCR_DIR}":/var/app easydocker-python-image 
