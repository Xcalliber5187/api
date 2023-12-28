from flask import Flask, render_template, request, flash, jsonify
import ipinfo

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


from discord_webhook import DiscordWebhook

import time

#for ip info
access_token = '5ac8be8bb6fc6e'
handler = ipinfo.getHandler(access_token)




@app.route("/")
def index():
	flash("Message to send.....")
	address = str(request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr))
	li = list(address.split(","))
	address = str(li[0])
	
	webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1168329715547918396/tInXbaiewZtPjWDSIoscBfgFfbunvddaNZ7HNNWl4nGVSZPgRqENtcXpK7xfpFO1B-TL", content=str(time.ctime())+" "+address+" "+"'"+"GetRequest+"'")
	webhook.execute()
	
	return render_template("index.html", test = "hi")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():

	message = str(request.form['name_input'])
	
	
	address = str(request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr))
	li = list(address.split(","))
	address = str(li[0])

	details = handler.getDetails(address)
	city = details.city
	country = details.country

	flash("Your message: " +'"'+ message +'"'+ " was sent!!\n I Know where you are.... City :"+city+" "+"Country :"+country + address)

	webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1168329715547918396/tInXbaiewZtPjWDSIoscBfgFfbunvddaNZ7HNNWl4nGVSZPgRqENtcXpK7xfpFO1B-TL", content=str(time.ctime())+" "+address+" "+"'"+message+"'")
	webhook.execute()
	return render_template("index.html", test = "success")
#Hello Me
