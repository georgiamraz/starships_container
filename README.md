# starships_container


## Running Container (From Docker CLI)

```
> docker run --rm -it -v ./data:/home/jovyan/data -v /path/to/pRT_input_data_path:/home/jovyan/starships_data -p 8888:8888 -u $(id -u):$(id -g) ghcr.io/steob92/starships_container:latest
```

* `--rm` deletes the container once you've exited.
* `-it` requires an interactive terminal
* `-v ./data:/home/jovyan/data` mounts the location of the `./data` directory into the container at `/home/jovyan/data`. 
* `-v /path/to/pRT_input_data_path:/home/jovyan/starships_data` mounts the location of the `pRT_input_data_path` directory into the container at `/home/jovyan/starships_data`. 
* `-p 8888:8888` maps port 8888 outside of the container (on the host system, your machine) to port 8888 within the container. To map a different port on the host system, for example port 8001, change this to `-p 8001:8888`.
* `-u $(id -u):$(id -g)` will set the user id and group id within the container to the same as the user launching the container. This means that you will be able to modify files from within the container without worrying about permission issues.

## Running Container (From Docker Compose)

First you should clone this repo or download the `docker-compose.yml` file.

In the `docker-compose.yml` file, modify the following lines as needed:

```
    ports:
      - "8888:8888" # Map container port 8888 to host port 8888 for jupyter lab
    volumes:
      - ./data:/home/jovyan/data # Local data mapping
      - ./data:/home/jovyan/starships_data # Location of the pRT_input_data_path directory

```

* Port `8888:8888` maps port 8888 on your machine to port 8888 within the container. To change this port to, for example, port 8001 you would change to `8001:8888`
* `./data:/home/jovyan/data # Local data mapping` Here `./data` is the path to local directory which will be accessible within the container. For example you might store analysis notebooks here.
* `./data:/home/jovyan/starships_data`. This is the location of the `pRT_input_data_path` directory needed for `petitRADTRANS`.

To lauch the container simply run:
```
> UID=$(id -u) GID=$(id -g) docker compose up
```

`UID=$(id -u) GID=$(id -g)` will set the user id and group id within the container to the same as the user launching the container. This means that you will be able to modify files from within the container without worrying about permission issues.

To shutdown the container, simply press `ctrl + c`.