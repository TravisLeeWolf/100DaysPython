from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL

DRINKS_RATING = ["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
WIFI_RATING = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
OUTLET_RATING = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]

class NewShopForm(FlaskForm):
    cafeName = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(label="Location (Maps URL)", validators=[URL()])
    timeOpen = StringField(label="Opening Time")
    timeClosed = StringField(label="Closing Time")
    coffeeRating = SelectField(label="How's the coffee?", choices=DRINKS_RATING, validators=[DataRequired()])
    wifiRating = SelectField(label="How's the WiFi?", choices=WIFI_RATING, validators=[DataRequired()])
    outletRating = SelectField(label="How's the availablity of outlets?", choices=OUTLET_RATING, validators=[DataRequired()])
    submit = SubmitField(label="Add Cafe")