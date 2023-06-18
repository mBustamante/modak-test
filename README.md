
<div align="center">
  • <a href="#set-up">Set Up</a>
  • <a href="#start-backend">Start backend</a>
</div>

## Set up

To clone and run this application, you'll need [Git](https://git-scm.com), [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/). From your command line:

```bash
# Clone this repository
$ git clone git@github.com:mBustamante/modak-test.git

# Go into the project folder
$ cd modak-test

# First, run the backend  
$ docker compose build backend

# Load fixtures
$ docker compose run --rm backend python manage.py loaddata users notifications_types
```

## Start backend

If you're going to work with the backend:

```bash
# First, run the backend  
docker compose up backend
```
Finally you be able to login in [the admin](http://localhost:8000/admin), and see all the data (username: admin@modak.com, password: admin).