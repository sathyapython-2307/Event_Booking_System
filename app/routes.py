from flask import render_template, request, redirect, url_for, flash
from app.models import events, bookings
from app.qr_util import generate_qr
from app.email_util import send_email
import os

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html", events=events)

    @app.route("/book/<int:event_id>", methods=["GET", "POST"])
    def book(event_id):
        event = events[event_id]
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            ticket_id = f"{name}_{event['name']}"
            qr_path = f"app/static/{ticket_id}.png"
            generate_qr(ticket_id, qr_path)
            bookings.append({"event": event["name"], "name": name, "email": email, "qr": qr_path})
            message = f"""You booked {event['name']}.\n\nQR saved at: {qr_path}"""
            send_email(email, "Booking Confirmed", message)
            return render_template("confirm.html", name=name, event=event["name"], qr=qr_path)
        return render_template("book.html", event=event)

    @app.route("/admin", methods=["GET", "POST"])
    def admin():
        if request.method == "POST":
            name = request.form["name"]
            date = request.form["date"]
            tickets = request.form["tickets"]
            events.append({"name": name, "date": date, "tickets": tickets})
            return redirect(url_for("admin"))
        return render_template("admin.html", events=events)

