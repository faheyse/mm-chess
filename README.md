To run the server, you must have python installed:
sudo apt install -y python3; sudo cp /bin/python3 /bin/python

and nginx:
sudo apt install nginx

then in the mm-chess/ directory, run:
./run.sh

the server should now be running


to debug on the server this may be helpful:
sudo tail -f /var/log/nginx/error.log
