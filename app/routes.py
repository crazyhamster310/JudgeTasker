# -*- coding: utf-8 -*-
import io
import sqlalchemy as sa
from flask import render_template, flash, redirect, url_for, send_file
from app import app, db
from app.forms import SearchForm
from app.models import PDF
from app.judge_parser import make_pdf


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        pdf = db.session.scalar(sa.select(PDF).where(PDF.source == form.source.data))
        flash("Загрузка задач, подождите")
        if pdf is None:
            file = make_pdf(form.source.data)
            if file is None:
                flash(f"Задачи соревнования {form.source.data} не найдены на сайте")
                return redirect(url_for("index"))
            pdf = PDF(source=form.source.data, file=file)
            db.session.add(pdf)
            db.session.commit()
        flash("Запрос обработан")
        if form.action.data == "download":
            return send_file(
                io.BytesIO(pdf.file),
                mimetype="application/pdf",
                conditional=True,
                as_attachment=True,
                download_name=pdf.source + ".pdf",
            )
        if form.action.data == "render":
            return send_file(
                io.BytesIO(pdf.file),
                mimetype="application/pdf",
                as_attachment=False,
                download_name=pdf.source,
            )
        return redirect(url_for("index"))
    return render_template("index.html", form=form)
