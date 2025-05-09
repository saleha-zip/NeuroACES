# flaskr/routes.py
from flask import Blueprint, render_template, request

# Create a blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Renders the 'index.html' template from flaskr/templates/
    return render_template('index.html')  # :contentReference[oaicite:0]{index=0}

@main_bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        form = request.form

        # Convert checkbox values (on → 1, missing → 0)
        def checkbox(name): return 1 if form.get(name) == 'on' else 0

        user_data = {
            'ACE_PhysicalAbuse': checkbox('ACE_PhysicalAbuse'),
            'ACE_SexualAbuse': checkbox('ACE_SexualAbuse'),
            'ACE_EmotionalNeglect': checkbox('ACE_EmotionalNeglect'),
            'ACE_ParentalDivorce': checkbox('ACE_ParentalDivorce'),
        }

        # Calculate ACE_Score
        user_data['ACE_Score'] = sum(user_data.values())

        # Other form values
        user_data.update({
            'PHQ9_Score': int(form['PHQ9_Score']),
            'GAD7_Score': int(form['GAD7_Score']),
            'Sleep_Hours': float(form['Sleep_Hours']),
            'Substance_Use': checkbox('Substance_Use'),
            'Support_System': checkbox('Support_System'),
            'NR3C1_Methylation': float(form.get('NR3C1_Methylation', 0)),
            'Cortisol_Level': float(form.get('Cortisol_Level', 0)),
        })

        from app.aces import predict_diseases  # Adjust path as needed
        predictions = predict_diseases(user_data)

        return render_template('results.html', predictions=predictions, inputs=user_data)

    return render_template('input.html')
