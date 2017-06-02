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
    3. 