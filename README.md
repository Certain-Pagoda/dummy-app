## Fastapi dummy app to check deployments
# dummy-app

This is a fastapi dummy app to test env variables, db connections and that sort of stuff while deploying.

So far to test aws tools

Create an .env with the aws credentials to pass to the env

The container expects the creds in the environment (like aws cli) or via env variable taken from the .env file

```
AWS_ACCESS_KEY_ID=<KEY>
AWS_SECRET_ACCESS_KEY=<SEcRET>
```

```
## Build
docker build -t dummyapp .

docker run -d -p 8080:8080 --env-file ./.env dummyapp-container-repository:latest
```
