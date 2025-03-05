from flask import Flask ,render_template, request, redirect, url_for, flash
from . import db
from .models import PatientData
from .forms import CancerRiskForm

app = Flask('main', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CancerRiskForm()
    if form.validate_on_submit():
        patient = PatientData(
            age=form.age.data,
            gender=form.gender.data,
            country=form.country.data,
            ethnicity=form.ethnicity.data,
            family_history=form.family_history.data,
            radiation_exposure=form.radiation_exposure.data,
            iodine_deficiency=form.iodine_deficiency.data,
            smoking=form.smoking.data,
            obesity=form.obesity.data,
            diabetes=form.diabetes.data,
            tsh_level=form.tsh_level.data,
            t3_level=form.t3_level.data,
            t4_level=form.t4_level.data,
            nodule_size=form.nodule_size.data
        )
        db.session.add(patient)
        db.session.commit()
        
        flash("Prediction submitted!", "success")
        return redirect(url_for('main.index'))
    
    return render_template('index.html', form=form)
