from flask import Flask,request,jsonify,Response
from bezier import Bezier,Point,BezierCurve

app = Flask(__name__)

poinXResult = []
poinYResult = []


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

@app.route("/api/submitdnc",methods=["POST","GET"])
def bezier():
    try:
        data = request.form
        iterasi = int(data.get("iterasi"))
        banyaktitik = int(data.get("banyaktitik"))
        poinX = data.getlist("xpoint")
        poinX = [float(x) for x in poinX]
        poinY = data.getlist("ypoint")
        poinY = [float(x) for x in poinY]

        poinXResult.clear()
        poinYResult.clear()

        poin = []
        for i in range(len(poinX)):
            poin.append(Point(poinX[i],poinY[i]))

        bezierClass = BezierCurve(poin,iterasi)
        bezierClass.create_bezier_dnc()
        for i in range(len(bezierClass.get_result_points_dnc())):
            poinXResult.append(bezierClass.get_result_points_dnc()[i].x)
            poinYResult.append(bezierClass.get_result_points_dnc()[i].y)

        return jsonify({
            "iterasi":iterasi,
            "banyaktitik":banyaktitik,
            "poinX":poinXResult,
            "poinY":poinYResult,
            "executionTime":bezierClass.dnc_execution_time
            })
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route("/api/submitbrute",methods=["POST","GET"])
def getPoints():
    try:
        data = request.form
        iterasi = int(data.get("iterasi"))
        banyaktitik = int(data.get("banyaktitik"))
        poinX = data.getlist("xpoint")
        poinX = [float(x) for x in poinX]
        poinY = data.getlist("ypoint")
        poinY = [float(x) for x in poinY]

        poinXResult.clear()
        poinYResult.clear()

        poin = []
        for i in range(len(poinX)):
            poin.append(Point(poinX[i],poinY[i]))

        bezierClass = BezierCurve(poin,iterasi)
        bezierClass.create_bezier_brutal()
        for i in range(len(bezierClass.get_result_points_brutal())):
            poinXResult.append(bezierClass.get_result_points_brutal()[i].x)
            poinYResult.append(bezierClass.get_result_points_brutal()[i].y)

        return jsonify({
            "iterasi":iterasi,
            "banyaktitik":banyaktitik,
            "poinX":poinXResult,
            "poinY":poinYResult,
            "executionTime":bezierClass.brutal_execution_time
            })
    except Exception as e:
        return jsonify({"error":str(e)})

if __name__ == "__main__":
    app.run()   