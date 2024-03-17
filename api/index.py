from flask import Flask,request,jsonify,Response
from bezier import Bezier

app = Flask(__name__)

poinXResult = []
poinYResult = []


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

        poinXResult.clear()
        poinYResult.clear()

        poin = []
        for i in range(len(poinX)):
            poin.append((poinX[i],poinY[i]))

        bezierClass = Bezier(iterasi,poin)
        bezierClass.createBezier()
        for i in range(len(bezierClass.bezier_points)):
            poinXResult.append(bezierClass.bezier_points[i][0])
            poinYResult.append(bezierClass.bezier_points[i][1])

        return jsonify({
            "iterasi":iterasi,
            "banyaktitik":banyaktitik,
            "poinX":poinXResult,
            "poinY":poinYResult
            })
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route("/api/getpoints",methods=["GET"])
def getPoints():
    try:
        if(poinXResult and poinYResult):
            return jsonify({
                "poinX":poinXResult,
                "poinY":poinYResult,
            })
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__ == "__main__":
    app.run()   