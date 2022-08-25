# Todo
## [https://todo.dmfstuff.xyz](https://todo.dmfstuff.xyz)


Todo is a very basic CRUD app that is very robustly deployed.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

I've made a few personal changes:
* In [production.yml](https://github.com/DaveFriedman/todo/blob/master/production.yml), the Traefik ports are set to `localhost:801` and `:4431`. This
  is because Todo is hosted on my AWS EC2 instance, with other personal
  projects. To route traffic, I use Nginx as a reverse proxy. Nginx listens on
  ports 80 and 443, so, to avoid a conflict, I make Traefik listen on ports 80
  #1 and 443 #1 and Nginx passes through the traffic.
  If you do this, be sure to pass through the original header of the request. By
  default, [Nginx redefines the Host field in proxied
  requests](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/),
  but Django is configured to only accept connections from the original Host and
  will reject all others. [This is my Nginx configuration file](https://github.com/DaveFriedman/todo/blob/master/todo.dmfstuff.xyz).

* In
  [.pre-commit-config.yaml](https://github.com/DaveFriedman/todo/blob/master/.pre-commit-config.yaml),
  I've cut flake8. I've got black, it's enough.

* The main Django app providing the Todo functionality is called `appcore`. With
  hindsight, I might've called it either `core` or `todocore`. This is mostly a
  note to myself.

* In
  [requirements/base.txt](https://github.com/DaveFriedman/todo/blob/master/requirements/base.txt),
  `pytz` is commented out, as it is deprecated. In
  [requirements/local.txt](https://github.com/DaveFriedman/todo/blob/master/requirements/local.txt),
  I'm using `psycopg2-binary`, as I had issues with `psycopg2`.

* In
  [config/settings/production.py](https://github.com/DaveFriedman/todo/blob/master/config/settings/production.py),
  in order to use Amazon SES for email and avoid a `NoRegionError`, include the
  AWS region you're using. [This Stackoverflow
  answer](https://stackoverflow.com/a/68776536/6775693) was helpful.

* In [config/urls.py](), the root URLs come from `appcore`, which makes much
  more sense to me than the using `home` or `about` pages that aren't connected
  to any app. I've cut those pages.
