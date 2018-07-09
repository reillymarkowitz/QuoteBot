var Twit = require('twit'),
	fs = require('fs'),
	readline = require('readline'),
	stream = require('stream'),
	dotenv = require('dotenv'),
	tokenizer = require('sbd')

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

var text = ''

// Process each line of book into array
rl.on('line', function(line) {
	text += line
})

var sentences = []

rl.on('close', function() {
	sentences = tokenizer.sentences(text)
	start()
})

var index = 0
var interval_id;

// Start tweeting, continue until end of sentences.
function start() {
    interval_id = setInterval(function() {
        if (index < sentences.length) {
        	var sentence = sentences[index]
            if (sentence.length <= 280)
                tweet(sentence)
            else
                process_long(sentence)
            index++
        } else
        	end()
    }, 30 * 60 * 1000) // 30 minutes between tweets
}

function end() {
	clearInterval(interval_id)
	tweet('End of book. Follow @ReillyMarkowitz for more projects.')
}

function process_long(sentence) {
	while(sentence.length > 280) {
		tweet(sentence.substring(0, 280))
		sentence = sentence.substring(280)
	}
	tweet(sentence)
}