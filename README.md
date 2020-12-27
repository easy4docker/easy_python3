# easy_python3 setup document

1. create setup.sh file:

  #!/bin/bash
  
  SCR_DIR=$(cd `dirname $0` && pwd)
  
  echo ${SCR_DIR}/code
  
  mkdir -p ${SCR_DIR}/code && mkdir -p ${SCR_DIR}/data
  
  git clone https://github.com/easy4docker/easy_python3.git ${SCR_DIR}/code
  
  cd ${SCR_DIR}/code
  
  docker container stop easydocker-python-container
  
  docker container rm easydocker-python-container
  
  docker image rm easydocker-python-image

  docker build -f dockerFile -t easydocker-python-image .
  
  docker run -it  --name easydocker-python-container -v "${SCR_DIR}/code":/var/app -v "${SCR_DIR}/data":/var/appData easydocker-python-image

2. run setup

  sh setup.sh

