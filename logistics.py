from flask import Blueprint, render_template, request

logistics_bp = Blueprint("logistics", __name__, template_folder="../templates")

deliveries = [] 

@logistics_bp.route("/logistics", methods=["GET", "POST"])
def logistics():
    if request.method == "POST":
        delivery = {
            "id": len(deliveries) + 1,
            "item": request.form["item"],
            "status": request.form["status"]
        }
        deliveries.append(delivery)
    return render_template("logistics.html", deliveries=deliveries)
