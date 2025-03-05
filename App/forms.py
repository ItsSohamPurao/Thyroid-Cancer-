from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CancerRiskForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    ethnicity = StringField('Ethnicity', validators=[DataRequired()])
    family_history = SelectField('Family History', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    radiation_exposure = SelectField('Radiation Exposure', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    iodine_deficiency = SelectField('Iodine Deficiency', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    smoking = SelectField('Smoking', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    obesity = SelectField('Obesity', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    diabetes = SelectField('Diabetes', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    tsh_level = FloatField('TSH Level', validators=[DataRequired()])
    t3_level = FloatField('T3 Level', validators=[DataRequired()])
    t4_level = FloatField('T4 Level', validators=[DataRequired()])
    nodule_size = FloatField('Nodule Size (mm)', validators=[DataRequired()])
    submit = SubmitField('Predict')
