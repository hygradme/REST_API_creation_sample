import flask

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def example():
    #Create json format for response
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    #Check whether the request method is POST 
    if flask.request.method == "POST":
        #If key "feature1" exists, store the value into response.
        if flask.request.get_json().get("feature1"):
            feature1 = flask.request.get_json().get("feature1")
            response["feature1"] = feature1

            #If key "feature2" exists, store the value into response too(optional).
            if flask.request.get_json().get("feature2"):
                feature2=flask.request.get_json().get("feature2")
                response["feature2"]=feature2

            # Show API response is success
            response["success"] = True

    return flask.jsonify(response)

if __name__ == "__main__":
    print("Running server!")
    app.run()
