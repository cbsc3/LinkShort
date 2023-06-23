import axios from "axios"
const auth_token = "9ba5f259-82b8-4cae-9ec3-97ab35dbf85d"
//The following functions in this file are for the use in react components, but they also serve as a testing method for the backend api
export function retrieve_ownership(auth_token, UUID_url){
    axios.get("http://127.0.0.1:5000/API/retrieve_ownership/" + auth_token + "/" + UUID_url)
    .then(function(response){
        var return_data = response.data;
        console.log(return_data.for_user, return_data.URL_fowarding_uuid, return_data.URL_given)
    })
}

export function shorten_url_non_existing(authentication_token, link, type, uuid){
    var URL_call_non_existing = "http://127.0.0.1:5000/API/" + authentication_token + "/" + link + "/" + type + "/" + uuid;
    axios.get(URL_call_non_existing)
    .then(function(response){
        var linkshort = response.data
        return linkshort.URL_for_user;
    })
}

export function shorten_url_existing(authentication_token, link, type, uuid){
    var URL_call_non_existing = "http://127.0.0.1:5000/API/" + authentication_token + "/" + link + "/" + type + "/" + uuid;
    axios.get(URL_call_non_existing)
    .then(function(response){
        var linkshort = response.data;
        return linkshort.URL_for_user;


    })
}
//Python API Route (Flask) @app.route('/API/<string:authenticationToken>/<string:URL>/<string:type>/<string:UUID_for_user>', methods=['GET', 'POST'])



