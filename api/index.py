from flask import Flask,request,jsonify,Response

app = Flask(__name__)

@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

@app.route("/api/submit",methods=["POST","GET"])
def bezier():
    try:
        data = request.form
        iterasi = int(data.get("iterasi"))
        banyaktitik = int(data.get("banyaktitik"))
        poinX = data.getlist("xpoint")
        poinX = [int(x) for x in poinX]
        poinY = data.getlist("ypoint")
        poinY = [int(x) for x in poinY]
        return jsonify({
            "iterasi":iterasi,
            "banyaktitik":banyaktitik,
            "poinX":poinX,
            "poinY":poinY
            })
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__ == "__main__":
    app.run()   