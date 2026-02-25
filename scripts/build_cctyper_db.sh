#usr/bin/sh

curl -L https://github.com/Russel88/CRISPRCasTyper/archive/refs/heads/master.zip -o cctyper_master.zip
unzip cctyper_master.zip
mv CRISPRCasTyper-master/data ./data
rm cctyper_master.zip
rm -rf CRISPRCasTyper-master
tar -xvzf data/Profiles.tar.gz
mv Profiles/ data/
rm data/Profiles.tar.gz