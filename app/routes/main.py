from flask import render_template, redirect, url_for, Blueprint, request, flash , jsonify 
from flask_login import login_required, current_user
from app.extensions import db
from app.models import CP, Platform

main = Blueprint("main", __name__)

# ---------------- HOME ----------------

@main.route("/")
@login_required
def home():

    search_query = request.args.get("search", "")
    platform_filter = request.args.get("platform", "")

    query = CP.query.filter_by(user_id=current_user.id)

    if search_query:
        query = query.filter(CP.ques_no.ilike(f"%{search_query}%"))

    if platform_filter:
        query = query.join(Platform).filter(Platform.name == platform_filter)

    page = request.args.get('page' , 1 , type = int)
    content = query.order_by(
        CP.is_fav.desc(),
        CP.done_at.desc()
    ).paginate(page = page , per_page = 3)

    platforms = Platform.query.order_by(Platform.name).all()

    return render_template(
        "home.html",
        content=content,
        platforms=platforms,
        search_query=search_query,
        platform_filter=platform_filter
    )

@main.route("/home")
@login_required
def home2():
    return redirect(url_for('main.home'))

#---------------------APIs-------------------------#

@main.route("/api/problems")
@login_required
def api_problems():
    
    platform = request.args.get("platform")
    difficulty = request.args.get("difficulty")
    page = request.args.get("page", 1, type=int)

    query = CP.query.filter_by(user_id=current_user.id)

    if platform:
        query = query.join(Platform).filter(Platform.name == platform)

    if difficulty:
        query = query.filter(CP.difficulty.ilike(difficulty))

    pagination = query.order_by(CP.done_at.desc()).paginate(page=page, per_page=3)

    problems = pagination.items

    data = []

    for p in problems:
        data.append({
            "id": p.id,
            "platform": p.platform.name if p.platform else None,
            "rating": p.rating,
            "difficulty": p.difficulty.capitalize() if p.difficulty else None,
            "is_fav": p.is_fav,
            "is_completed": p.is_completed
        })

    return jsonify({
        "problems": data,
        "page": pagination.page,
        "pages": pagination.pages,
        "total": pagination.total
    })

#----------------- Dashboard --------------

@main.route("/dashboard" , methods = ["GET" , "POST"])
@login_required
def dashboard():

    name = current_user.username

    fav = CP.query.filter_by(user_id = current_user.id , is_fav = True).count()

    completed = CP.query.filter_by(user_id = current_user.id , is_completed = True).count()

    total = CP.query.filter_by(user_id = current_user.id ).count()

    percent = round(completed/total * 100 , 2) if total > 0 else 0.0

    from zoneinfo import ZoneInfo

    last_problem = CP.query.filter_by(
        user_id=current_user.id
    ).order_by(CP.done_at.desc()).first()

    if last_problem:
        utc_time = last_problem.done_at.replace(tzinfo=ZoneInfo("UTC"))
        ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
        last_seen = ist_time.strftime("%d %b %Y, %I:%M %p")
    else:
        last_seen = "No submissions yet"

    return render_template("dashboard.html" , name = name , last_seen = last_seen , completed = completed , fav = fav , total = total , percent = percent ) 

# ---------------- ADD ----------------

@main.route("/add", methods=["GET", "POST"])
@login_required
def add_ques():
    if request.method == "POST":
        rating = request.form.get("rating")
        difficulty = request.form.get("difficulty")
        if difficulty : difficulty = difficulty.capitalize()

        if not rating and not difficulty:
            flash("Please enter rating or difficulty")
            return render_template("add_ques.html")
        platform_name = request.form.get("platform") or "CodeForces"
        ques_no = request.form.get("ques_no")

        if not ques_no:
            flash("Question number is required 🫠")
            return render_template("add_ques.html")

        platform = Platform.query.filter_by(name=platform_name).first()

        if not platform:
            platform = Platform(name=platform_name)
            db.session.add(platform)

        c = CP(
            rating= int(rating) if rating else None,
            difficulty = difficulty if difficulty else None,
            ques_no=ques_no,
            platform=platform,
            user=current_user
        )

        db.session.add(c)
        db.session.commit()

        flash("Question Added Successfully ✅")
        return redirect(url_for("main.home"))

    return render_template("add_ques.html")

# ---------------- FAVORITE ----------------

@main.route("/toggle-fav/<int:id>", methods=["POST"])
@login_required
def favorite(id):
    c = CP.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    c.is_fav = not c.is_fav
    db.session.commit()

    return {
        "status": "success",
        "is_fav": c.is_fav
    }

# ---------------- COMPLETED ----------------

@main.route("/toggle-completed/<int:id>", methods=["POST"])
@login_required
def completed(id):
    c = CP.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    c.is_completed = not c.is_completed
    db.session.commit()

    return {
        "status": "success",
        "is_completed": c.is_completed
    }

# ---------------- EDIT ----------------

@main.route("/edit/<int:id>")
@login_required
def edit_ques(id):
    c = CP.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    return render_template("edit_ques.html", c=c)

# ---------------- UPDATE ----------------

@main.route("/update/<int:id>", methods=["POST"])
@login_required
def update(id):
    c = CP.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    rating = request.form.get("rating") or "800"
    difficulty = request.form.get("difficulty") or "easy"
    platform_name = request.form.get("platform") or "CodeForces"
    ques_no = request.form.get("ques_no")

    platform = Platform.query.filter_by(name=platform_name).first()

    if not platform:
        platform = Platform(name=platform_name)
        db.session.add(platform)

    c.rating = rating
    c.difficulty = difficulty
    c.ques_no = ques_no
    c.platform = platform

    db.session.commit()

    flash("Updated Successfully 👍")
    return redirect(url_for("main.home"))

# ---------------- DELETE ----------------

@main.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    c = CP.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(c)
    db.session.commit()

    flash("Deleted Successfully 👌")
    return redirect(url_for("main.home"))