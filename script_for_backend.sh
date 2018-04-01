sudo apt-get update;
sudo apt-get install nginx;

cd ~/backend-nginx;

sudo mv default /etc/nginx/sites-enabled;
sudo nginx -s reload;
sudo apt-get update;
sudo apt install software-properties-common;
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D;
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main';
sudo apt-get update;
sudo apt-get install -y docker-engine;

sudo docker rm -f $(sudo docker ps -aq)
sudo docker build -t friendlyhello .
sudo docker run -d -p 5000:5000 friendlyhello
