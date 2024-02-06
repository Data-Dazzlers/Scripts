# This is our website for Data Dazzlers script to install docker, traefik/nginx, and BeEF. 

--- docker ---
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done # this unistalls conflicting packages

# Install docker using apt repository
# Add Docker's official GPG key:

    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin # Install docker packages
sudo docker run hello-world # This should print "Hello from Docker!" To verify Docker is working

--- traefik ---
# First you must locate the docker-compose.yml file included in the repository, when in this directory you can type docker-compose up -d traefik to start traefik
docker-compose up -d traefik

--- BeEF Instructions ---
# First, you must download the beefproject zip file and unzip (or you can use Git clone to download it)
wget https://github.com/beefproject/beef/archive/master.zip
unzip master.zip

# Next we must build our beef docker container
docker build -t beef . # the (period) represents the current directory, where the Dockerfile is (./install) This is located in the same directory as unzipped directory
docker run -p 3000:3000 -p 6789:6789 -p 61985:61985 -p 61986:61986 --name beef --entrypoint=/bin/bash -it beef # Run the container
docker exec -it beef ifconfig eth0 # If you need to change the ethernet adapter, here is the command to do it
