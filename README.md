# WG Flask API
The main API inside our WG Network. It serves data form a PostgreSQL Server and acts as an intermediary for the Unifi Controller API.
The API is mostly used by our WG Website displaying usefull information about our WG.

## Getting Started
To locally run the API it is recommended to use vscode devcontainers.
Once opened inside a devcontainer run `flask run` to start a development instance of the API on port 5000.

## Environment variables
There are some environment variables that have to be set so that the API works properly.

- UNIFI_HOST_URL
- UNIFI_SITE
- UNIFI_USER
- UNIFI_PASSWORD

...
