#!/bin/bash

if [ -z "$UID" ] || [ $UID -eq 0 ]; then
    USER_ID=1000
else
    USER_ID=$UID
fi

# Create a new user with the specified UID
useradd -m -u $USER_ID -s /bin/bash jovyan

# Change ownership of the home directory
chown -R $USER_ID:$USER_ID /home/jovyan

mkdir -p /home/jovyan/starships_data && mkdir -p /home/jovyan/.local

# Switch to the new user and execute the command
exec gosu jovyan "$@"
