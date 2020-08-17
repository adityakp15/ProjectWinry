Run the requirements file on your terminal using the command

    pip3 install -r requirements.txt

If you have an error installing PyAudio, run the following commands on your terminal.

    sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
    sudo apt-get install ffmpeg libav-tools
    sudo pip3 install pyaudio

To install the geckodriver for firefox, or the chromedriver for google chrome, run the following scripts

    Geckodriver

    wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
    sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
    sudo chmod +x /usr/bin/geckodriver
    rm geckodriver-v0.23.0-linux64.tar.gz

    Chromedriver
    
    wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo chmod +x chromedriver
    sudo mv chromedriver /usr/bin/
    rm chromedriver_linux64.zip

