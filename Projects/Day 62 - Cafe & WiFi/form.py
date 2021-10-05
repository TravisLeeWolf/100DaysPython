from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, URL

DRINKS_RATING = [(0, "✘"), (1, "☕"), (2, "☕☕"), (3, "☕☕☕"), (4, "☕☕☕☕"), (5, "☕☕☕☕☕")]
WIFI_RATING = [(0, "✘"), (1, "💪"), (2, "💪💪"), (3, "💪💪💪"), (4, "💪💪💪💪"), (5, "💪💪💪💪💪")]
OUTLET_RATING = [(0, "✘"), (1, "🔌"), (2, "🔌🔌"), (3, "🔌🔌🔌"), (4, "🔌🔌🔌🔌"), (5, "🔌🔌🔌🔌🔌")]

class NewShopForm(FlaskForm):
    cafeName = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(label="Location (Maps URL)", validators=[URL()])
    timeOpen = StringField(label="Opening Time")
    timeClosed = StringField(label="Closing Time")
    coffeeRating = SelectField(label="How's the coffee?", choices=DRINKS_RATING, validators=[DataRequired()])
    wifiRating = SelectField(label="How's the WiFi?", choices=WIFI_RATING, validators=[DataRequired()])
    outletRating = SelectField(label="How's the availablity of outlets?", choices=OUTLET_RATING, validators=[DataRequired()])