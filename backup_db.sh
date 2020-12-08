mkdir -p /home/incubator/dumps/$(date +"%y-%m-%d")
docker-compose -f /home/incubator/docker/apps/incubator/docker-compose.yml exec db /usr/local/bin/pg_dump --dbname="incubator_db" --username="incubator" -f /backup.dump
docker cp incubator_db_1:/backup.dump /home/incubator/dumps/$(date +"%y-%m-%d")/incubator.dump
