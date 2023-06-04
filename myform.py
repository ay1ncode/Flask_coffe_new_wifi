from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired

class Coffee_form(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()], render_kw={"style": "width:50%"})
    coffee_loc = StringField(label="coffee Location", validators=[DataRequired()], render_kw={"style": "width:50%"})
    open_time = StringField(label="Opening time e.g 10.00am", validators=[DataRequired()], render_kw={"style": "width:50%"})
    close_time = StringField(label="Closing time e.g 10.00am", validators=[DataRequired()], render_kw={"style": "width:50%"})
    coffee_rate = SelectField(label="Coffee rating", choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕')],
                              render_kw={"style": "width:50%"})  # Select field for coffee rating
    wifi = SelectField(label="Wifi Strength", choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪')],
                      render_kw={"style": "width:50%"})  # Select field for wifi strength
    power_soc = SelectField(label="Power socket availability",
                            choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌')],
                            render_kw={"style": "width:50%"})  # Select field for power socket availability
    submit = SubmitField('Submit')  # Submit button
