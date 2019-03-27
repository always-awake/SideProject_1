docker run \
    --rm -it \
    --publish 5432:5432 \
    --env POSTGRES_PASSWORD="admin12345" \
    --volume `pwd`/data_pg:/var/lib/postgresql/data \
    postgres:11