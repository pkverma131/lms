# Pull docker images

```
docker pull <image_name>:<tag>
```

# List all images

```
docker images
```

# create docker container
```
docker run -dit --name lms_devpad -v E:\lms:/home/rahul/lms -p 3000:3000 -p 8000-8050:8000-8050 174c8c134b2a
```
# List all existing container
```
docker ps -a
```

## You can read me

### Install sudo
```
apt-get update
apt-get install sudo
sudo su
```

### Install neccessary packages
```
sudo apt-get install git zip curl wget mysql virtaulenv python
```

### Mysql server commands
```
/etc/init.d/mysql status
/etc/init.d/mysql start
/etc/init.d/mysql status
/etc/init.d/mysql stop
```


### Install latest pip
```
curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```