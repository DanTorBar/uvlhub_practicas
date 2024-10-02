from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app.modules.notepad.forms import NotepadForm
from app.modules.notepad import notepad_bp
from app.modules.notepad.services import NotepadService

notepad_service = NotepadService()


@notepad_bp.route('/notepad', methods=['GET'])
def index():
    return render_template('notepad/index.html')
