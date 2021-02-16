sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
pip3 install selenium

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
chrome_version=`google-chrome --version|grep -wo [0-9\.]* |sed 's/\.[0-9\.]*//'`

driver_version=`curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version`

wget https://chromedriver.storage.googleapis.com/$driver_version/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

export PATH=$PATH:/`pwd`

