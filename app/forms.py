from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description= TextAreaField("Description", validators=[DataRequired()])
    photo = FileField("Photo Upload", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
