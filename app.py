from flask import Flask, render_template, request, flash, jsonify

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


from discord_webhook import DiscordWebhook

import time


@app.route("/")
def index():
	flash("Message to send.....")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():

	message = str(request.form['name_input'])
	flash("Your message: " +'"'+ message +'"'+ " was sent!!")
	
	address = str(request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr))
	li = list(address.split(","))
	address = str(li[0])

	

	webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1168329715547918396/tInXbaiewZtPjWDSIoscBfgFfbunvddaNZ7HNNWl4nGVSZPgRqENtcXpK7xfpFO1B-TL", content=str(time.ctime())+" "+address+" "+"'"+message+"'")
	webhook.execute()
	return render_template("index.html")
#Hello Me
