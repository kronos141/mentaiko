#webサーバー稼働
sudo systemctl start nginx
#インターフェース起動
uwsgi --socket :8001 --module oursite.wsgi
