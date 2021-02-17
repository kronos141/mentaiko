
#python関係のインストール
sudo yum install python3
sudo yum groupinstall "Development Tools"
sudo yum install python3-devel

#ライブラリ関係
sudo pip3 -r requirement.txt
sudo pip3 install wheel


#nginx instal
sudo amazon-linux-extras install nginx1

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

echo /usr/local/lib >> /etc/local/lib
sudo rm libsqlite3.so.0
sudo rm -rf libsqlite3.so.0.8.6
sudo ldconfig

#uwsgiとnginxの同期
sudo ln -s server_conf/oursite_nginx.conf /etc/nginx/conf.d/

