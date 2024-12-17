# -*- coding: utf-8 -*-
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class PDF(db.Model):
    source: so.Mapped[str] = so.mapped_column(
        sa.String(100), primary_key=True
    )
    file: so.Mapped[sa.LargeBinary] = so.mapped_column(sa.LargeBinary)

    def __repr__(self):
        return f"PDF {self.source}"
