![The Queen Bee](docs/logo.png)

## Development

This is still under rapid development; things are liable to break without warning!

### Bootstrapping a dev environment

You should use:

- [asdf vm](https://github.com/asdf-vm/asdf) to manage your python runtime
- [docker](https://www.docker.com/products/docker-desktop) to run the database
- [pipenv](https://pipenv.readthedocs.io/en/latest/) to manage your python dependencies

Got all that? Good!

```bash
# get the proper python version
asdf install

# install pipenv and get the dev deps
pip install -U pipenv
pipenv install --dev

# pull the postgres image and run it in the background
docker pull postgres
docker run -d -p 5432:5432 postgres

# get into the python virtualenv
pipenv shell

# run the database migrations
./manage.py migrate
```

### Testing

While I generally feel like coverage benchmarks are trash (because they are), I like
having an easy way to tell if something I wrote _is_ tested.

```bash
coverage run manage.py test
coverage report
```
