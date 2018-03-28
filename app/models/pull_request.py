# -*- coding: utf-8 -*-

#
# Unless explicitly stated otherwise all files in this repository are licensed
# under the Apache 2 License.
#
# This product includes software developed at Datadog
# (https://www.datadoghq.com/).
#
# Copyright 2018 Datadog, Inc.
#

"""pull_request.py

PullRequest model.
"""

from datetime import datetime
from .. import db


class PullRequest(db.Model):
    __tablename__ = 'pull_requests'

    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    url = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    github_pull_request_id = db.Column(db.Integer, unique=True)
    trello_card_url = db.Column(db.String(64), unique=True)
    trello_card_id = db.Column(db.String(64), unique=True)

    # Associations
    repo_id = db.Column(db.Integer, db.ForeignKey('repos.github_repo_id'))
