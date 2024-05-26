#!/usr/bin/env bash
# Sets up server for deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
	
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

echo "<html>
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <h1>Hello Holberton!</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
