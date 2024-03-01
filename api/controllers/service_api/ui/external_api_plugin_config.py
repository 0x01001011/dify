from flask import Blueprint, render_template, request

ui_bp = Blueprint('ui', __name__, url_prefix='/ui')

@ui_bp.route('/configure_external_api', methods=['GET', 'POST'])
def configure_external_api():
    if request.method == 'POST':
        api_url = request.form.get('api_url')
        # Assuming ExternalAPIPlugin has a method to save configurations
        # This part of the code would interact with ExternalAPIPlugin to save the provided configurations
        # For demonstration, we'll just return a success message
        return render_template('configuration_success.html', api_url=api_url)
    return render_template('configure_external_api.html')
