# PRACTISE OF DOCKER - DICE ROLL APP
## APP RUNNING:
<img width="777" height="757" alt="image" src="https://github.com/user-attachments/assets/7033b594-92d2-4f67-b826-c76d537ccc06" />

## CREATING THE ROLL DICE FUNCTIONALITY:
### To create the app functionality you must modify the function `get_sides()` by collecting the environment variable `DICE_SIDES`
### and validating it's a number and  > 1.

### Lately,  you must call the function and print a random result of the roll.

### For that, we will be importing 'random' and 'os'

## FUNCTION GET SIDES:
<img width="648" height="262" alt="image" src="https://github.com/user-attachments/assets/b88044b2-fa6f-4148-84c6-7217e97cd3e5" />

### First we collect the environment variable with getenv method in a variable called `sides_int`, and a "validator" number
### Then we cast the env variable to 'int'
### We check if the integed number is lower that 1. If true, we raise an error and return the correct "validation" number
### If `sides_int` is 2 or more, the variable is returned

## FUNCTION INDEX:
<img width="803" height="112" alt="image" src="https://github.com/user-attachments/assets/b1dc079d-c9d2-44d6-b2fc-330a0139dbf3" />

### We collect the previous function's returned value in `sides` and save a randomized value between 1 and `sides` value with random.randint method
### Then we return it by printing it in the index.html

## DOCKERFILE CREATED:
<img width="711" height="380" alt="image" src="https://github.com/user-attachments/assets/60970ec3-4ca5-45a8-b6a5-aef8a88913c2" />

## DOCKER COMMANDS:
## Building: `docker build -t dice_app .`
## Running: `docker run -p 8888:5000 dice_app`
