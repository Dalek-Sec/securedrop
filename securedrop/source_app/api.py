import json
import platform

from flask import Blueprint, make_response

import version


def make_blueprint(config):
    view = Blueprint('api', __name__)

    @view.route('/metadata')
    def metadata():
        meta = {'supported_languages': config.SUPPORTED_LOCALES,
                'gpg_fpr': config.JOURNALIST_KEY,
                'sd_version': version.__version__,
                'server_os': platform.linux_distribution()[1],
                }
        resp = make_response(json.dumps(meta))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    return view
