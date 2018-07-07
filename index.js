var Twit = require('twit'),
	fs = require('fs'),
	readline = require('readline'),
	stream = require('stream'),
	dotenv = require('dotenv')

dotenv.load();

var T = new Twit({
  consumer_key:         process.env.CONSUMER_KEY,
  consumer_secret:      process.env.CONSUMER_SECRET,
  access_token:         process.env.ACCESS_TOKEN,
  access_token_secret:  process.env.ACCESS_TOKEN_SECRET,
  timeout_ms:           60 * 1000,  // optional HTTP request timeout to apply to all requests
  strictSSL:            true        // optional - requires SSL certificates to be valid
})

function tweet(text) {
	T.post('statuses/update', { status: text }, function(err, data, response) {
		console.log('Tweet #' + index + ' ID: ' + data.id_str)
	})
}

var rl = readline.createInterface(
	fs.createReadStream('ao.txt'), 
	new stream
)

var lines = []

// Process each line of book into array
rl.on('line', function(line) {
	if(typeof line !== undefined)
		if(line.length > 0)
			lines.push(line)
})

// Start tweeting after text processing finishes
rl.on('close', start)

var index = 0;

function start() {
	if(index < lines.length) {
		tweet(lines[index])
		index++
		setTimeout(start, 5 * 60 * 1000) // 5 minute pause between tweets
	} else {
		tweet('End of book. Follow @ReillyMarkowitz for more projects.')
		console.log('Process finished.')
	}
}