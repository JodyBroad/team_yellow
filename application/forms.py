from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, input_required

# need form to do email newsletter sign up

class EmailSignUpForm(FlaskForm):
    email = StringField('Email')
    submit = SubmitField('Sign Up')


# new form needs to link to userlogin person and address tables for registering customers (is set in the route to set the
# persontype to '2' which is customer
class CustomerRegistrationForm(FlaskForm):
    # userlogin elements
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('confirm_password', message="Passwords must match")]) #Equal to validator not working, will still submit even if passwords do not match

    # person elements
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Please supply a valid email')]) #email validator not working, form will still submit even if no @ or . is present in field.

    # address elements
    address_line_one = StringField('Address Line 1', validators=[DataRequired()])
    address_line_two = StringField('Address Line 2')
    address_line_three = StringField('Address Line 3')
    postcode = StringField('Postcode', validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    # submit
    submit = SubmitField('Sign Up')

    # Custom error created to raise error when special characters are used in username, however, error not raising when tested"
    def validate_username(self, username):
        # self.username = username
        excluded_chars = " *?!'^+%&/()=}][{$#"
        for char in self.username.data:
            if char in excluded_chars:
                raise ValidationError(
                    f'Character {char} is not allowed in username.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Please supply a valid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# as staff are now a type of person, this form gets a bit more complicated, needs to link to userlogin, address,
# person and staff info tables to be functional (can set persontype to '1' which is staff in the routes)
class StaffRegistrationForm(FlaskForm):
    # userlogin elements
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('confirm_password',
                                                                                             message="Passwords must match")])

    # person elements
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Please supply a valid email')])

    # address elements
    address_line_one = StringField('Address Line 1', validators=[DataRequired()])
    address_line_two = StringField('Address Line 2')
    address_line_three = StringField('Address Line 3')
    postcode = StringField('Postcode', validators=[DataRequired()])
    phone_number = StringField('Phone Number')

    # staff info elements
    job_title = StringField('Job title', validators=[DataRequired()])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    # submit
    submit = SubmitField('Register New Staff Member')


class PlantForm(FlaskForm):
    # plant_name = StringField('Plant Name', validators=[DataRequired()])
    #removed plant_name field as not sure it was necessary, can add again if needed. Had to completely remove from html file as form would not work with it commented out, was still picking up on the website after submitting the form"
    plant_species = StringField('Plant Species', validators=[DataRequired()])
    plant_type = SelectField('Type', choices=[('1', 'Cacti/Succulent'), ('2', 'Hanging'), ('3', 'Flowering'), ('4', 'Palms'), ('5', 'Ferns')], validators=[DataRequired()])
    plant_category = SelectField('Categories', choices=[('1', 'Indoor'), ('2', 'Outdoor')])
    plant_price = IntegerField('Plant Price', validators=[DataRequired()])
    plant_stock = IntegerField('Number Being Added To Stock', validators=[DataRequired()])
    plant_size = SelectField('Size', choices=[('1', 'Tiny'), ('2', 'Small'), ('3', 'Medium'), ('4', 'Tall')], validators=[DataRequired()])
    submit = SubmitField('Register Plant')


# add a new blog post
class NewBlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    post_content = StringField('Post Content', validators=[DataRequired()])

    submit = SubmitField('Add post')

# log in form
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    type = SelectField('Type', choices=[('1', 'Staff'), ('2', 'Customer')])

    submit = SubmitField('Log in')

# Victoria's code
class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')



