cd project
ray start --head
ray stop

ray metrics launch-prometheus

wget https://dl.grafana.com/enterprise/release/grafana-enterprise-11.1.4.linux-amd64.tar.gz
tar -zxvf grafana-enterprise-11.1.4.linux-amd64.tar.gz
./grafana-v11.1.4/bin/grafana-server --homepath grafana-v11.1.4 --config /tmp/ray/session_latest/metrics/grafana/grafana.ini

RAY_GRAFANA_HOST=https://bookish-meme-grx6xp4jvjrc9qx4-3000.app.github.dev/?orgId=1 RAY_PROMETHEUS_HOST=https://bookish-meme-grx6xp4jvjrc9qx4-9090.app.github.dev ray start --head