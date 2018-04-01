sudo apt-get update;
sudo apt-get install python-software-properties;
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D;
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main';
sudo apt-get update;
sudo apt-get install -y docker-engine;

cd ~/backend-nginx;
sudo docker build -t friendlyhello .
sudo docker run -p 5000:5000 friendlyhello

