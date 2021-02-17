#webサーバー稼働
sudo systemctl restart nginx
#インターフェース起動
uwsgi --socket :8001 --module oursite.wsgi
