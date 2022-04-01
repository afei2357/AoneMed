import re
import random
import time
import os
from datetime import datetime
import string
from flask import jsonify,request,g
from app.api import bp
from app.models.model_user import *

@bp.route('/channel', methods=['GET'])
#@token_auth.login_required
def get_channels():
    u = User.query.first()
    print(u)
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 100,type=int)
    name = request.args.get('name',type=str, default=None)
    #data = Channel.to_collection_dict(Channel.query.order_by(Channel.id.desc()), page, page_size)
    data = {'aa':'bb'}

    return jsonify({'code': 200, 'infos': data})

