from flask import Blueprint
from .api import  getPacket
from Project.extension import api

app_rustful = Blueprint('app_rustful', __name__)
api.init_app(app_rustful)


api.add_resource(getPacket, '/getpacket')
