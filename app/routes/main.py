from flask import Flask , render_template , redirect , url_for , Blueprint , request , flash
from app.extensions import db
from app.models import CP

main = Blueprint("main" , __name__)

@main.route("/")
def home():
    content = CP.query.order_by(
    CP.is_fav.desc(),
    CP.done_at.desc()
    ).all()
    return render_template("home.html" , content = content)

@main.route("/add" , methods = ["POST" , "GET"]) 
def add_ques() :
    if request.method == "POST" :
        rating = request.form.get("rating") or "800"
        platform = request.form.get("platform") or "CodeForces"
        ques_no = request.form.get("ques_no")

        if not ques_no :
            flash("Question number is required dummy 🫠\nNow type again 😊")
            return render_template("add_ques.html")
        c = CP(rating = rating , platform = platform , ques_no = ques_no)
        db.session.add(c)
        db.session.commit()
        flash("Question Added Successfully ✅")
        return redirect(url_for("main.home"))
    
    return render_template("add_ques.html")

@main.route("/toggle-fav/<int:id>" , methods = ["POST"])
def favorite(id):
    c = CP.query.get_or_404(id)
    if not c.is_fav :
        flash("Marked as Favorite 💝")
    else : flash("Unmarked as Favorite 🩶")
    c.is_fav = not c.is_fav

    db.session.commit()
    return redirect(url_for("main.home"))

@main.route("/toggle-completed/<int:id>" , methods = ["POST"])
def completed(id):
    c = CP.query.get_or_404(id)
    if not c.is_completed :
        flash("Marked as completed ✅")
    else : flash("Unmarked from completed")

    c.is_completed = not c.is_completed

    db.session.commit()
    return redirect(url_for("main.home"))

@main.route("/edit/<int:id>" , methods = ["GET" , "POST"])
def edit_ques(id):
    c = CP.query.get_or_404(id)
    return render_template("edit_ques.html" , c = c )

@main.route("/update/<int:id>" , methods = ["POST"])
def update(id):
    rating = request.form.get("rating") or "800"
    platform = request.form.get("platform") or "CodeForces"
    ques_no = request.form.get("ques_no")

    if not ques_no :
        flash("Question number can't be empty ! ")
        return render_template("edit_ques.html" , c = c)
    
    c = CP.query.get(id)
    c.rating = rating 
    c.platform = platform 
    c.ques_no = ques_no

    db.session.commit()
    flash("Updated the Question details Successfully 👍")
    return redirect(url_for("main.home"))

@main.route("/delete/<int:id>" , methods = ["POST"])
def delete(id):
    c = CP.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash(f"Deleted the question {c.ques_no} Successfully 👌")
    return redirect(url_for("main.home"))

