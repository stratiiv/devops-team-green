set -o allexport
source .env
set +o allexport

sudo apt-get update
sudo apt install apache2 -y
sudo apt install openjdk-11-jdk -y
sudo apt install snapd -y
sudo apt install postgresql -y
sudo apt install gnupg -y
sudo apt install curl -y
sudo apt install zip -y
sudo apt install unzip -y

mkdir $APP_HOME
git clone https://github.com/stratiiv/java-schedule-app.git $APP_HOME
curl -s "https://get.sdkman.io/" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk version
sdk install gradle 7.0

#redis install
sudo apt install redis-server -y
sudo sed -i "s/supervised no/supervised systemd/" /etc/redis/redis.conf
sudo systemctl restart redis.service

#mongodb install
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
sudo touch /etc/apt/sources.list.d/mongodb-org-7.0.list
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod

#add postgresql user and databases
#sudo adduser *insert ur expected database owner*
sudo groupadd schedule
sudo useradd -g schedule schedule
cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER;
CREATE DATABASE $APP_DB_NAME$_TEST WITH OWNER=$APP_DB_USER;
EOF

# restore db from dump
sudo -u schedule psql -d schedule -f /tmp/dump/2023-09-07.dump #replace with ur dump name and/or path 

# Add Tomcat user
sudo groupadd tomcat
sudo useradd -s /bin/bash -g tomcat -d /opt/tomcat tomcat

# Download Tomcat
cd /home/vagrant
sudo apt-get -y install curl
curl -O --progress-bar https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.82/bin/apache-tomcat-9.0.82.tar.gz

# Extract into target directory
sudo mkdir /opt/tomcat
sudo tar xzvf apache-tomcat-9*tar.gz -C /opt/tomcat --strip-components=1

# Assign ownership over target directory
sudo chgrp -R tomcat /opt/tomcat
sudo chmod -R g+r /opt/tomcat/conf
sudo chmod g+x /opt/tomcat/conf
sudo chown -R tomcat /opt/tomcat/webapps/ /opt/tomcat/work/ /opt/tomcat/temp/ /opt/tomcat/logs/

# Copy basic Tomcat configuration files
sudo cp /home/vagrant/webapps/config/context.xml /opt/tomcat/webapps/manager/META-INF/context.xml
sudo cp /home/vagrant/webapps/config/context.xml /opt/tomcat/webapps/host-manager/META-INF/context.xml
sudo cp /home/vagrant/webapps/config/tomcat-users.xml /opt/tomcat/conf/tomcat-users.xml

# Copy service file and reload daemon
sudo cp webapps/config/setenv.sh /opt/tomcat/bin
sudo chmod 755 /opt/tomcat/bin/setenv.sh
sudo cp webapps/config/tomcat.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start tomcat
sudo ufw allow 8080
sudo systemctl enable tomcat

#nodejs & npm install
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get update
sudo apt install nodejs -y
sudo apt install npm -y

#comment this line if it's not working
#sudo -u tomcat set -o allexport && source /home/vagrant/scripts/.env && set +o allexport
find $APP_DIR -type f -name "hibernate.properties" -exec sed -i "s/hibernate.connection.password=.*/hibernate.connection.password=\${APP_DB_PASS}/" {} + 

#build and deploy, modify it to fit in ur project
cd $APP_HOME/frontend
sudo chmod -c ugo+w .env 
sudo sed -i "s/localhost/192.168.56.20/" $APP_HOME/frontend/.env 
npm install
cd $APP_HOME
gradle build
cp $APP_HOME/build/libs/class_schedule.war /opt/tomcat/webapps/ROOT.war #replace with expected path to ur war file here
rm -rf /opt/tomcat/webapps/ROOT #optional
systemctl restart tomcat
cd $APP_HOME/frontend
npm start