# Python Script To Control Garage Door

# Load libraries
import RPi.GPIO as GPIO
import time
from bottle import route, run, post, request

# Set up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PIN_TRIG = 40
PIN_ECHO = 38
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(7, True)   
GPIO.output(11, True)

#define variables
fresh_login = True
pswd = 'xxxx'

#Define check_login (function that checks if password is correct by comparing it to the correct one)
def check_login(password):
    if password == pswd:
        return True
    else:
        return False

#Create the login form (html)
@route('/login') #http://servername/login
def login():
    #Making fresh_login true when new form is created
    
    global fresh_login #make fresh_login a global variable
    fresh_login = True
    #Create the html form
    return '''
        <form action="/login" method="post">
            Password: <input name="password" type="password" />
            <input value="Open" type="submit" />
        </form>
    '''

#Receive and check login info
@route('/login', method='POST')
def do_login():
    global fresh_login #make fresh_login global from inside function do_login
    password = request.forms.get('password') #request password from form created in login
    #Making sure the login is fresh
    if fresh_login == True:
        fresh_login = False #make fresh login false so page reload doesn't cause garage to re-open (a variable that takes place of a cookie, but clears on webpage closing)
        if check_login(password): #cycle the gpio to open garage if passwords match
            GPIO.output(7, False)
            time.sleep(.8)
            GPIO.output(7, True)
            return "<p>Opening Garage Door One.</p>" #confirm that garage is opening
        else:
            return "<p>Incorrect Password.</p>" #tell them to go away if password is incorrect
    else:
        return "<p>Please restart your browser</p>" #this triggers if fresh_login was false when the function ran, telling you to restart your browser/webpage to clear the fresh_login variable

#Create the login form (html) for the sensor page
@route('/sensor') #http://servername/sensor
def sensor():
    #Create the html form
    return '''
        <form action="/sensor" method="post">
            Password: <input name="password" type="password" />
            <input value="Authorize" type="submit" />
        </form>
    '''

#Create the sensor page (html)
@route('/sensor', method='POST') #http://servername/sensor
def do_sensor():
    password = request.forms.get('password') #request password from form created in login
    if check_login(password): #Continue to the sensor reading if the password is correct       
        GPIO.setup(PIN_TRIG, GPIO.OUT) #Setup the gpio trigger pin as input
        GPIO.setup(PIN_ECHO, GPIO.IN) #Setup the gpio echo pin as output
    
        time.sleep(2) #Wait for 2 seconds for sensor to settle

        GPIO.output(PIN_TRIG, GPIO.LOW) #Set trigger to low

        GPIO.output(PIN_TRIG, GPIO.HIGH) #Set trigger to high

        time.sleep(0.00001) #Wait for 0.1 milliseconds before setting to low again

        GPIO.output(PIN_TRIG, GPIO.LOW) #Set trigger to low again

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time() #Set the start time of when the waves are emitted by the sensor
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time() #Record the time the waves traveled back to the sensor
            pulse_duration = pulse_end_time - pulse_start_time #Calculate how long it took for the round trip of the waves
            distance = round(pulse_duration * 17150, 2) #Convert the time it took to centimeters and round to 2 decimals
       
        if distance >= 80: #Check if the distance is less than 80cm (This will depend on the garage)
            return '<p>The garage is closed.</p>'
        else:
            return '<p>The garage is open.</p>'
    else:
        return '<p>Sorry, the password entered was incorrect</p>' #Don't allow access if password isn't correct

#Run the bottle.py server           
run(host='0.0.0.0', port=1234)


