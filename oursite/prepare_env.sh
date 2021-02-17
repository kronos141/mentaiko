
#python関係のインストール
sudo yum install -y python3
sudo yum groupinstall -y "Development Tools"
sudo yum install -y python3-devel

#ライブラリ関係
sudo pip3 install -y wheel
sudo pip3 install -r requirement.txt


#nginx instal
sudo amazon-linux-extras install -y nginx1

#sqlite3のupdate,直接build
wget https://www.sqlite.org/2020/sqlite-autoconf-3310100.tar.gz
tar xvfz sqlite-autoconf-3310100.tar.gz 
cd sqlite-autoconf-3310100/
./configure --prefix=/usr/local
sudo make
sudo make install

rm ../sqlite-autoconf-3310100.tar.gz
rm -rf sqlite-autoconf-3310100

#sqlite3のpath周りの変更
sudo mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
sudo ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3

sudo sh -c "echo '/usr/local/lib' >> /etc/ld.so.conf"
sudo rm /lib64/libsqlite3.so.0
sudo rm -rf /lib64/libsqlite3.so.0.8.6
sudo ldconfig

#uwsgiとnginxの同期
sudo ln -s ~/mentaiko/oursite/server_conf/oursite_nginx.conf /etc/nginx/conf.d/oursite_nginx.conf

