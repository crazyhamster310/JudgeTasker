# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    source = StringField("Источник задачи", validators=[DataRequired()])
    action = SelectField(
        label="Действие с документом",
        choices=[("download", "Скачать"), ("render", "Отобразить на странице")],
    )
    search = SubmitField("Поиск")
