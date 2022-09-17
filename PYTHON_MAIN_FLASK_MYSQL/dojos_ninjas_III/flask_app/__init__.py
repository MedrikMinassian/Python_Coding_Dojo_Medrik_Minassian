# from dataclasses import dataclass
from flask import Flask, render_template, request,redirect, session #flash (used for login and reg)
app = Flask(__name__)
app.secret_key="usercr"  