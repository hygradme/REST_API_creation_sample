import flask

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def example():
    #返答用のjsonの基本フォーマットを作成
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    #POSTRでリクエストがきているか
    if flask.request.method == "POST":
        #POSTで受けたリクエスト(json形式)に"feature1"というキーがあれば処理(feature1の値をresponse["feature1"]に、response["success"]にTrueを格納し返却)
        if flask.request.get_json().get("feature1"):
            feature1 = flask.request.get_json().get("feature1")
            response["feature1"] = feature1

            #feature2というキーがあればそれも格納
            if flask.request.get_json().get("feature2"):
                feature2=flask.request.get_json().get("feature2")
                response["feature2"]=feature2

            # APIが処理を正しく終えたことを示す
            response["success"] = True

    return flask.jsonify(response)

if __name__ == "__main__":
    print("Running server!")
    app.run()
