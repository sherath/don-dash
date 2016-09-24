import cloudpassage
from flask import Flask
from flask import render_template
app = Flask(__name__)


halo_creds = cloudpassage.ApiKeyManager()
halo_session = cloudpassage.HaloSession(halo_creds.key_id, halo_creds.secret_key)


def get_servers(halo_session):
    servers_object = cloudpassage.Server(halo_session)
    all_servers = servers_object.list_all()
    return all_servers


@app.route('/')
def home_page():
    return render_template('mainpage.html')


@app.route('/servers')
def server_list():
    return render_template('servers.html', servers=get_servers(halo_session))
