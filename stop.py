import os

os.system('ps aux | grep gunicorn > gunicorn.txt')

# kill all gunicorn processes
with open('gunicorn.txt', 'r') as f:
    for line in f:
        line = line.split()
        os.system('kill ' + line[1])

os.system('rm gunicorn.txt')

# stop nginx
os.system('sudo service nginx stop')


