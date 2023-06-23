from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests
from ENV import collectionURL, collectionUsers, collectionToken
import uuid
from flask_cors import CORS
from urllib.parse import quote

#The first thing we are going to do is implement our database variables

app = Flask(__name__)

CORS(app)

def auth(token):
    locate_token = collectionToken.find_one({"UUID":token})
    if locate_token:
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def main_route():
    return jsonify({
        "Auth":None
    })

#The first thing we want to do is connect the frontend to the backend by creating a simple authentication token
@app.route('/API/<string:authenticationToken>/<string:URL>/<string:type>/<string:UUID_for_user>', methods=['GET', 'POST'])
def shorten_url_non_users(authenticationToken, URL, type, UUID_for_user):
    #First let's try to see if the user from the frontend is authenticated
    if auth(authenticationToken) == True:
        #Here, we are for the temp url connection, we are going to make a uuid that will be connected to the URL, the type will tell us wheter we want persistence or not,
        if type == "temp":
            uuid_for_url = str(uuid.uuid4())

            schema_url_short = {
                "URL_given":URL,
                "URL_fowarding_uuid":uuid_for_url,
                "for_user":"temp"

            }

            shortened = "http://localhost:5000/" + "linkshort" + "=" + uuid_for_url

            return_statment = {
                "Auth": True,
                "URL_for_user": shortened
            }


            collectionURL.insert_one(schema_url_short)
            return jsonify(return_statment)
        elif type == "existing":
            uuid_for_url = str(uuid.uuid4())
            schema_url_short = {
                "URL_given":URL,
                "URL_forwarding_uuid":uuid_for_url,
                "for_user":UUID_for_user
            }
            shortened = "http://127.0.0.1:5000/" + "linkshort" + "=" + uuid_for_url
            return_statment = {
                "Auth":True,
                "URL_for_user":shortened
            }

            collectionURL.insert_one(schema_url_short)


            return jsonify(return_statment)
    else:
        return jsonify({

            "Auth":None
        })

#The first thing we will do is begin to configure the authentication users for the authenticated users to be able to use the API
@app.route('/linkshort=<string:URL>', methods=["GET", "POST"])
def link_short(URL):
     find_url = collectionURL.find_one({"URL_fowarding_uuid":URL})
     if find_url:
         return redirect("https://" + find_url["URL_given"])
     else:
         return "The following path does not exist."
     return "..."
#Next this we are going to create a retreial url
@app.route('/API/retrieve_ownership/<string:authentication_token>/<string:UUID_url>', methods=["GET", "URL"])
def retr_ownership(authentication_token, UUID_url):
    if auth(authentication_token):
         locate = collectionURL.find_one({"URL_fowarding_uuid":UUID_url})

         if locate:
            return jsonify({
                "URL_fowarding_uuid": UUID_url,
                "URL_given":locate["URL_given"],
                "for_user":locate["for_user"]

            })

         else:
            return jsonify({
                "Results":None
            })
    return jsonify({
        "Auth":None
    })




if __name__ == '__main__':
    app.run()
