# starships_container


## Running Container (From Docker CLI)

```
> docker run --rm -it -v ./data:/home/jovyan/data -v /path/to/pRT_input_data_path:/home/jovyan/starships_data-p 8888:8888 -u $(id -u):$(id -g) path/to/starhships_container:latest
```
