from flask import Flask, render_template, request

app = Flask(__name__)

deliveries = [] 

@app.route("/", methods=["GET", "POST"])
def logistics():
    if request.method == "POST":
        delivery = {
            "id": len(deliveries) + 1,
            "item": request.form["item"],
            "status": request.form["status"]
        }
        deliveries.append(delivery)
    return render_template("logistics.html", deliveries=deliveries)

if __name__ == "__main__":
    app.run(debug=True)
