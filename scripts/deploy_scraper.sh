#!/bin/bash

# zip dependencies
cd ../venv/lib/python3.6/site-packages
echo "Zipping requirements..."
zip -r9q ${OLDPWD}/../function.zip .

cd $OLDPWD/../src/scraper

# make a copy of tweet_queue
cp ../tweet_queue.py .

# add source files to function.zip
zip -g ../../function.zip lambda_handler.py
zip -g ../../function.zip scraper.py
zip -g ../../function.zip tweet_queue.py

rm -f tweet_queue.py
cd ../../
echo "Deploying Lambda function..."

# deploy function code to Lambda
aws lambda update-function-code --function-name quote-scraper --zip-file fileb://function.zip
rm -f function.zip
