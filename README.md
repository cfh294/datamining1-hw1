# Data Mining I HW 1

Repo containing improved examples for HW 1 in Data Mining I for Dr. Breitzman's course 
at Rowan University. The original code was written by Robert Preuss, a student who had previously
taken this course.

This repo contains code for scraping Google and Twitter using their respective API-wrapper Python 
libraries. 

### Disclaimer

This code is meant to be used as a guide to help people get basic Python API script examples
to work on their machines, **not** as a working *solution* for students to claim as their own.

## Getting this Repo

Use ```git``` to clone this repository. This would be much quicker than copying the files 
one by one.

```shell script
git clone https://github.com/cfh294/datamining1-hw1.git
```

## Requirements

Just run the ```requirements.txt``` file with ```pip```.

```shell script
cd datamining1-hw1
pip3 install -r requirements.txt
```

You will also need API keys and secrets for the Google and Twitter APIs if you
want to use their respective secrets. For more info on how to obtain these, 
visit these links:

- [Google API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key)
- [Twitter API Keys](https://developer.twitter.com/en/docs/basics/apps/guides/the-app-management-dashboard)

## Configuration

```shell script
cd datamining1-hw1
cp SAMPLE.config.ini ./config.ini

# use vim (or some other text editor) 
# to fill out the config values. 
vim config.ini
```

## Running the Code

```shell script
cd datamining1-hw1

# Twitter 
./twitter-app.py <twitter_user> -c ./config.ini

# Google
./google-app.py <query> -c ./config.ini
```

## Dependencies

- Python 3.7 +
