## Sentiment analysis of spanish sentences
This repository is built to predict the sentiment of sentences written in spanish. It has been trained with open source datasets (wiki and twitter). 

### Requirements
    Tensorflow 1.0.1
    python 2.7
    tflearn 0.3
    flask 0.12.2
    numpy 1.12.1
    scipy 0.19.0

To deploy into the server, first, create a new environment and install tensorflow as follows:

    1. Install pip and virtualenv: 
        sudo apt-get install python-pip python-dev python-virtualenv

    2. Create virual env environment:
        virtualenv --system-site-packages ~/tensorflow.1.0.1

    3. Activate the virtualenv environment
        source ~/tensorflow.1.0.1/bin/activate
    
    4. Install tensorflow
        pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp27-none-linux_x86_64.whl

    5. Install tflearn
        pip install tflearn
    
    6. Install miniconda
        download: https://conda.io/miniconda.html
        ./Miniconda3-latest-Linux-x86_64.sh
        
    6. Install h5py
        conda install h5py
    
    6. Install Flask
        pip install flask



    
## Deployment

1. Apache2 configuration

    add to /etc/apache2/sites-enabled/000-default.conf: 
    
        WSGIDaemonProcess sentiment
        WSGIScriptAlias /sentiment /var/www/NLP/sentiment/start.py
        <Directory /var/www/NLP/sentiment>
                WSGIProcessGroup sentiment
                WSGIApplicationGroup %{GLOBAL}
                Allow from all
        </Directory>
    

2. Modify config.py and put the path where the repository was downloaded.

        import sys
        sys.path.insert(0, '/var/www/NLP/sentiment/')

3. Add the virtualenv environment:

        python_home = '/home/gustavo/tensorflow.1.0.1/'
        activate_this = python_home + '/bin/activate_this.py'
        execfile(activate_this, dict(__file__=activate_this))

4. restart apache by typing: 

        sudo service apache2 restart

## logs

To check if the REST API is correctly deployed, check the logs of apache under: 

        sudo nano /var/log/apache2/error.log

