# This is our website for Data Dazzlers script to install docker, traefik/nginx, and BeEF. 
most commands are ran in 'sudo' because permissions suck
## --- Docker Instructions---
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done # this unistalls conflicting packages

### Install docker using apt repository
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

### Add the repository to Apt sources:
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

Install docker packages:
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin 
Verify Docker is working by running this command:
    sudo docker run hello-world

## --- Traefik Instructions ---
### First you must locate the docker-compose.yml file included in the repository, when in this directory you can type docker-compose up -d traefik to start traefik
    docker-compose up -d traefik

## --- BeEF Instructions ---
### First, you must download the beefproject zip file and unzip (or you can use Git clone to download it)
wget method:
    wget https://github.com/beefproject/beef/archive/master.zip
    unzip master.zip
Or, clone the repository from GitHub using Git:
    git clone https://github.com/beefproject/beef

### Next we must build our beef docker container
Build the beef container
Note: The (period) represents the current directory, where the Dockerfile is (./install) This is located in the same directory as unzipped directory
    docker build -t beef .
Run a new instance of Beef and enter it.
    docker run -p 3000:3000 -p 6789:6789 -p 61985:61985 -p 61986:61986 --name beef --entrypoint=/bin/bash -it beef # Run the container
From within the container run
    ./beef
If the container is running, and you need to change the network adapter use this command, make sure to change 'eth0' to whatever network interface is desired
    docker exec -it beef ifconfig eth0