# Running the STARSHIPS Container on Your Local Machine

This guide walks you through downloading, modifying, and running the `starships_container` using Docker and VS Code.  
Please complete these steps before arriving at ExoSlam.  
If you run into any issues, email georgia.mraz@mail.mcgill.ca or come find us on Day 1 during the debug hour.

---

## Prerequisites

- Docker Desktop must be installed and running  
  Install here: https://docs.docker.com/get-started/get-docker/  
  Docker is running if you see the whale icon in your system tray (near Wi-Fi/battery).

- (Optional but Recommended) Install Visual Studio Code (VS Code): https://code.visualstudio.com/

- Important: You may need to increase Docker's memory allocation  
  Go to: Docker → Settings → Resources → Adjust the memory sliders.

---

## Step 1: Clone the Repository

You will need approximately 2 GB of free space.

Open your terminal and run:

```bash
git clone -b developeHOST https://github.com/georgiamraz/starships_container.git
cd starships_container
```

Important: Make sure you are on the `developeHOST` branch and not `main`.

---

## Step 2: Edit `docker-compose.yaml`if needed [Mac Users Only]

Open `docker-compose.yaml` in VS Code or another text editor.  


Uncomment this line in `docker-compose.yaml`:

```yaml
# platform: linux/amd64
```

Change it to:

```yaml
platform: linux/amd64
```

This is necessary for macOS.  
Windows and Linux users can leave it commented or remove it.



## Step 3: Launch the Container

From the root directory (`starships_container`), run:

```bash
docker compose up
```

Docker will begin building or launching the container.

If you see a "permission denied" error, run the same command again — it usually works the second time.

---

## Step 5: Open Jupyter Lab

After the container launches, a URL like this will appear in the terminal:

```
http://127.0.0.1:8091/lab?token=...
```

Copy and paste the URL into your browser to open Jupyter Lab.

---

## You’re Done

You should now be in a working Jupyter Lab environment and ready to explore the STARSHIPS notebooks.

---

## To Stop the Container

Press `Control + C` in the terminal where the container is running.
