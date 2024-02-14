from flask import Blueprint, redirect, render_template, request, url_for

external_api_plugin_ui = Blueprint('external_api_plugin_ui', __name__, template_folder='templates', url_prefix='/v1/ui')

@external_api_plugin_ui.route('/configure', methods=['GET'])
def show_configuration_form():
    return render_template('configure_external_api_plugin.html')

@external_api_plugin_ui.route('/configure', methods=['POST'])
def handle_configuration_form_submission():
    api_url = request.form.get('api_url')
    if not api_url:
        return render_template('configure_external_api_plugin.html', error="API URL is required.")
    try:
        update_external_api_plugin_configuration(api_url)
        return redirect(url_for('external_api_plugin_ui.configuration_success'))
    except Exception as e:
        return render_template('configure_external_api_plugin.html', error=str(e))

@external_api_plugin_ui.route('/success', methods=['GET'])
def configuration_success():
    return render_template('configuration_success.html')

def update_external_api_plugin_configuration(api_url):
    # Assuming there's a global or accessible instance of ExternalAPIPlugin
    external_api_plugin_instance.set_api_url(api_url)
