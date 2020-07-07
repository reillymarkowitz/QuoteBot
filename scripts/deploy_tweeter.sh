#!/bin/bash

# zip dependencies
cd ../venv/lib/python3.6/site-packages
echo "Zipping requirements..."
zip -r9q ${OLDPWD}/../function.zip .

cd $OLDPWD/../src/tweeter

# make a copy of tweet_queue
cp ../tweet_queue.py .

zip -g ../../function.zip lambda_handler.py
zip -g ../../function.zip bot.py
zip -g ../../function.zip tweeter.py
zip -g ../../function.zip tweet_queue.py
zip -g ../../function.zip .env

rm -f tweet_queue.py
cd ../../
echo "Deploying Lambda function..."

# deploy function code to Lambda
aws lambda update-function-code --function-name quote-tweeter --zip-file fileb://function.zip
rm -f function.zip
