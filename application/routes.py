from flask import render_template, request, flash, redirect, url_for
from application import app, db
from application.forms import BasicForm, RegistrationForm, StaffForm, PlantForm  # LoginForm
from application.models import Person, Address
# Car, Customer, Staff

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register_basic_form():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            person = Person(first_name=first_name, last_name=last_name)
            db.session.add(person)
            db.session.commit()
            return 'Thank you!'
    return render_template('home.html', form=form, message=error, title='home')

# made this simple home route to try and get it working
# @app.route('/home', methods=['GET'])
# def home():
#     return render_template('home.html', title='home')


@app.route('/people', methods=['GET'])
def show_people():
    error = ""
    people = Person.query.all()
    if len(people) == 0:
        error = "There are no people to display"
        print(people)
    return render_template('people.html', people=people, message=error)


# @app.route('/cars', methods=['GET'])
# def show_cars():
#     error = ""
#     cars = Car.query.all()
#     if len(cars) == 0:
#         error = "There are no cars to display"
#         print(cars)
#     return render_template('cars.html', cars=cars, message=error, title="Car")


@app.route('/people/<int:person_id>', methods=['GET'])
def show_person(person_id):
    error = ""
    # use filter_by for any column
    # person = Person.query.filter_by(id=person_id).first()
    #  use get for the PK
    person = Person.query.get(person_id)

    # simpsons = Person.query.filter_by(last_name="simpson").all()

    # to sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).all()
    # descending sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name.desc()).all()
    # limit to top 2 simpsons
    simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).limit(2).all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=simpsons)


@app.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = "Flanders"
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=[])


@app.route('/people/<int:person_id>/<string:new_last_name>', methods=['PUT'])
def update_person_with_name(person_id, new_last_name):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = new_last_name
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Updated Person", family=[])


@app.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    people = Person.query.all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        # print(person)
    return render_template('people.html', people=people, message=error, title="People")


@app.route('/personandcars/<int:person_id>', methods=['GET'])
def people_and_cars(person_id):
    error = ""
    person = Person.query.get(person_id)
    # cars= person.cars
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
        # print(person_and_carinfo)
    return render_template('person_and_cars.html', person=person, message=error, title="Person and Car Info")

    # return render_template('home.html', form=form, message=error)


# LINKS TO PLANT HTML PAGES

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/contact_us', methods=['GET'])
def contact():
    return render_template('contact_us.html', title='Contact Us')


@app.route('/plant_care', methods=['GET'])
def plant_care():
    return render_template('plant_care.html', title='Plant Care')


@app.route('/shop', methods=['GET'])
def shop():
    return render_template('shop.html', title='Shop')


@app.route('/plant1', methods=['GET'])
def plant1():
    return render_template('plant1.html', title='Plant 1')


@app.route('/plant2', methods=['GET'])
def plant2():
    return render_template('plant2.html', title='Plant 2')


@app.route('/plant3', methods=['GET'])
def plant3():
    return render_template('plant3.html', title='Plant 3')


@app.route('/plant4', methods=['GET'])
def plant4():
    return render_template('plant4.html', title='Plant 4')


@app.route('/plant5', methods=['GET'])
def plant5():
    return render_template('plant5.html', title='Plant 5')


@app.route('/plant6', methods=['GET'])
def plant6():
    return render_template('plant6.html', title='Plant 6')


@app.route('/plant7', methods=['GET'])
def plant7():
    return render_template('plant7.html', title='Plant 7')


@app.route('/plant8', methods=['GET'])
def plant8():
    return render_template('plant8.html', title='Plant 8')


@app.route('/plant9', methods=['GET'])
def plant9():
    return render_template('plant9.html', title='Plant 9')


@app.route('/plant10', methods=['GET'])
def plant10():
    return render_template('plant10.html', title='Plant 10')


# CUSTOMER RELATED ROUTES:

# REGISTERING A NEW CUSTOMER:
# not yet functional, issues linking address foreign key
# combine staff and customer into person and add person_type
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address_line_one = form.address_line_one.data
        address_line_two = form.address_line_two.data
        address_line_three = form.address_line_three.data
        postcode = form.postcode.data
        # username = form.username.data
        # password = form.password.data


# here would need to also add in username and password
        # or len(password) < 4
        # or len(username0 == 0

        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(address_line_two) == 0\
                or len(address_line_three) == 0\
                or len(postcode) == 0:
            error = "Please complete each section of this form"
        else:
            address = Address(address_line_one=address_line_one,
                              address_line_two=address_line_two,
                              address_line_three=address_line_three,
                              postcode=postcode)
            person = Person(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                address=address)
                                # username=username,
                                # password=password,
            db.session.add(address)
            db.session.add(person)
            db.session.commit()
            return 'Thank you'
    return render_template('register.html', title='Register', message= error, form=form)


# ACCESSING A LIST OF CUSTOMERS
# This is functional
# will just need to add filter by person type - see line 67 for filtering
@app.route('/customer_list', methods=['GET'])
def show_customers():
    error = ""
    customer = Customer.query.all()
    if len(customer) == 0:
        error = "There are no people to display"
        print(customer)
    return render_template('customer_list.html', customer=customer, message=error)



# STAFF RELATED ROUTES

# REGISTERING A NEW MEMBER OF STAFF:
# This is functional
# remove, combine into person

@app.route('/register_staff', methods=['GET', 'POST'])
def register_staff():
    error = ""
    form = StaffForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        if len(first_name) == 0\
                or len(last_name) == 0\
                or len(email) == 0\
                or len(password) < 4:
            error = "Please supply an email and password"
        else:
            staff = Staff(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          password=password)
            db.session.add(staff)
            db.session.commit()
            return 'Thank you'
    return render_template('register_staff.html', title='Register New Staff', message= error, form=form)


# ACCESSING A LIST OF CURRENT STAFF
# will just need to add filter by person type - see line 67 for filtering
@app.route('/staff_list', methods=['GET'])
def show_staff():
    error = ""
    staff = Staff.query.all()
    if len(staff) == 0:
        error = "There are no people to display"
        print(staff)
    return render_template('staff_list.html', staff=staff, message=error)

# DELETE STAFF ACCOUNTS - currently provides error message 'method not allowed'
# @app.route('/staff/<int:staff_id>', methods=['DELETE'])
# def delete_staff(staff_id):
#     error = ""
#     staff = Staff.query.get(staff_id)
#     db.session.delete(staff)
#     db.session.commit()
#     staff = Staff.query.all()
#     if not staff:
#         error = "There is no staff with ID: " + str(staff_id)
#         print(staff)
#     return render_template('staff_deletion.html', staff=staff, message=error, title="Delete Staff")




# REGISTERING A NEW PLANT:

# not yet complete, needs rest of the fields filling in

@app.route('/plantform', methods=['GET', 'POST'])
def plantform():
    error = ""
    form = PlantForm()

    if request.method == 'POST':
        plant = form.plant_name.data
        category = form.plant_category.data

        if len(plant) == 0 or category :
            error = "Please complete the fields"
        else:
            # person = Person(first_name=first_name, last_name=last_name)
            # db.session.add(person)
            # db.session.commit()
            return 'Thank you'
    return render_template('plantform.html', title='Register a Plant', message= error, form=form)

# ACCESSING A LIST OF PLANTS:
# to do
# DELETING PLANTS WE NO LONGER STOCK:
# to do

