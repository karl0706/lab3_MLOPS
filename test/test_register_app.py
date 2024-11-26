import sys
import os
# Ajouter le dossier `lab3` au chemin Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from register_app.py import *
from src.register_app import *
import pytest
import io

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test_get_user_name_from_input_space(monkeypatch):
    monkeypatch.setattr('sys.stdin',io.StringIO('Karl 99'))
    assert get_user_name_from_input() is None

def test_get_user_name_from_input_blank(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' '))
    assert get_user_name_from_input() is None

def test_get_user_name_from_input_blank(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    assert get_user_name_from_input() is None

def test_get_user_name_from_input_blank(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Karl99'))
    assert get_user_name_from_input() == 'Karl99'

