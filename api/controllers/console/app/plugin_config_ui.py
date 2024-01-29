from flask import Blueprint, flash, redirect, render_template, request, url_for

plugin_config_ui_bp = Blueprint('plugin_config_ui', __name__, template_folder='templates')

class PluginConfigUI:
    def render_config_form(self):
        return render_template('plugin_config_form.html')

    def handle_form_submission(self):
        api_url = request.form.get('api_url')
        if not api_url:
            flash('API URL is required.', 'error')
            return redirect(url_for('plugin_config_ui.render_config_form'))

        # Here, add logic to validate the API URL and save the configuration.
        # For example, you might want to verify that the URL is well-formed,
        # reachable, and that the server responds with valid JSON.
        # If the URL is valid, save the configuration using the appropriate
        # method or service. If saving fails, flash an error message.

        flash('Plugin configuration saved successfully.', 'success')
        return redirect(url_for('plugin_config_ui.render_config_form'))

@plugin_config_ui_bp.route('/config', methods=['GET'])
def config():
    return PluginConfigUI().render_config_form()

@plugin_config_ui_bp.route('/config', methods=['POST'])
def save_config():
    return PluginConfigUI().handle_form_submission()
