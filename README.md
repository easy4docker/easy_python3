# easy_python3 setup document

1. create setup.sh file:

  #!/bin/bash
  
  SCR_DIR=$(pwd)
  
  rm -fr ${SCR_DIR}/data &&  rm -fr ${SCR_DIR}/code
  
  mkdir -p ${SCR_DIR}/data &&  mkdir -p ${SCR_DIR}/code
  
  cd ${SCR_DIR}/code
  
  git clone https://github.com/easy4docker/easy_python3.git .
  
  docker container stop easydocker-python-container
  
  docker container rm easydocker-python-container
  
  docker image rm easydocker-python-image

  docker build -f dockerFile -t easydocker-python-image .
  
  docker run -it  --name easydocker-python-container -v "${SCR_DIR}/code":/var/app -v "${SCR_DIR}/data":/var/appData easydocker-python-image

2. run setup

  sh setup.sh
  
3. When the setup code has finished creating the virtual environment, go to /var/app/src, run python3 historical.py to fetch the data.
4. Fetched data will be in /var/appData
5. To get the correlation, go to /var/app/src run python3 correlation.py [Stock1] [Stock2]

