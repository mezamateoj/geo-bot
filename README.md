# GeoVictoria clock in bot 

Bot deploy on a aws lambda using serverless: https://www.serverless.com/

And for the chrome drivers for selenium we get them from this image:
https://github.com/umihico/docker-selenium-lambda/blob/main/README.md

```bash
$ npm install -g serverless # skip this line if you have already installed Serverless Framework
$ serverless deploy
# test deploy function
$ sls invoke --function your-func-name
```

### run locally

```bash
python main.py
```

TODO:
* add schedule to the serverless.yml
* github actions