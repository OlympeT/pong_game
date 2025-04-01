import turtle
import time

# Screen setup
wn = turtle.Screen()  # Create the game window
wn.title("Pong by Olympe Tchibozo")  # Set the window title
wn.bgcolor("black")  # Set the background color to black
wn.setup(width=800, height=600)  # Set the window size
wn.tracer(0)  # Turns off automatic screen updates

# Paddle A
paddle_a = turtle.Turtle()  # Create the left paddle
paddle_a.speed(0)  # Set the paddle's speed to the fastest
paddle_a.shape("square")  # Set the paddle's shape to a square
paddle_a.color("white")  # Set the paddle's color to white
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square to create a rectangle
paddle_a.penup()  # Prevent the paddle from drawing lines when it moves
paddle_a.goto(-350, 0)  # Set the paddle's initial position

# Paddle B
paddle_b = turtle.Turtle()  # Create the right paddle
paddle_b.speed(0)  # Set the paddle's speed to the fastest
paddle_b.shape("square")  # Set the paddle's shape to a square
paddle_b.color("white")  # Set the paddle's color to white
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square to create a rectangle
paddle_b.penup()  # Prevent the paddle from drawing lines when it moves
paddle_b.goto(350, 0)  # Set the paddle's initial position

# Ball
ball = turtle.Turtle()  # Create the ball
ball.speed(0)  # Set the ball's speed to the fastest
ball.shape("square")  # Set the ball's shape to a square
ball.color("white")  # Set the ball's color to white
ball.penup()  # Prevent the ball from drawing lines when it moves
ball.goto(0, 0)  # Set the ball's initial position
ball.dx = 0.2  # Set the ball's x-axis speed
ball.dy = 0.2  # Set the ball's y-axis speed

# Score
score_a = 0  # Initialize Player A's score
score_b = 0  # Initialize Player B's score

# Pen (for displaying the score)
pen = turtle.Turtle()  # Create a turtle for displaying the score
pen.speed(0)  # Set the pen's speed to the fastest
pen.color("white")  # Set the pen's color to white
pen.penup()  # Prevent the pen from drawing lines when it moves
pen.hideturtle()  # Hide the pen turtle
pen.goto(0, 260)  # Set the pen's initial position
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))  # Write the initial score

# Functions
def paddle_a_up():  # Function to move Paddle A up
    y = paddle_a.ycor()  # Get the paddle's current y-coordinate
    y += 20  # Increase the y-coordinate
    paddle_a.sety(y)  # Set the paddle's new y-coordinate

def paddle_a_down():  # Function to move Paddle A down
    y = paddle_a.ycor()  # Get the paddle's current y-coordinate
    y -= 20  # Decrease the y-coordinate
    paddle_a.sety(y)  # Set the paddle's new y-coordinate

def paddle_b_up():  # Function to move Paddle B up
    y = paddle_b.ycor()  # Get the paddle's current y-coordinate
    y += 20  # Increase the y-coordinate
    paddle_b.sety(y)  # Set the paddle's new y-coordinate

def paddle_b_down():  # Function to move Paddle B down
    y = paddle_b.ycor()  # Get the paddle's current y-coordinate
    y -= 20  # Decrease the y-coordinate
    paddle_b.sety(y)  # Set the paddle's new y-coordinate

# Keyboard bindings
wn.listen()  # Listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # Call paddle_a_up when 'w' is pressed
wn.onkeypress(paddle_a_down, "s")  # Call paddle_a_down when 's' is pressed
wn.onkeypress(paddle_b_up, "Up")  # Call paddle_b_up when the up arrow is pressed
wn.onkeypress(paddle_b_down, "Down")  # Call paddle_b_down when the down arrow is pressed

# Main game loop
while True:
    wn.update()  # Update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Move the ball along the x-axis
    ball.sety(ball.ycor() + ball.dy)  # Move the ball along the y-axis

    # Border checking
    if ball.ycor() > 290:  # If the ball hits the top wall
        ball.sety(290)  # Move the ball back within the wall
        ball.dy *= -1  # Reverse the ball's y-axis direction

    if ball.ycor() < -290:  # If the ball hits the bottom wall
        ball.sety(-290)  # Move the ball back within the wall
        ball.dy *= -1  # Reverse the ball's y-axis direction

    if ball.xcor() > 390:  # If the ball goes past Paddle B
        ball.goto(0, 0)  # Reset the ball's position
        ball.dx *= -1  # Reverse the ball's x-axis direction
        score_a += 1  # Increment Player A's score
        pen.clear()  # Clear the previous score display
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

    if ball.xcor() < -390:  # If the ball goes past Paddle A
        ball.goto(0, 0)  # Reset the ball's position
        ball.dx *= -1  # Reverse the ball's x-axis direction
        score_b += 1  # Increment Player B's score
        pen.clear()  # Clear the previous score display
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):  # If the ball hits Paddle B
        ball.setx(340)  # Move the ball back within the paddle's bounds
        ball.dx *= -1  # Reverse the ball's x-axis direction

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):  # If the ball hits Paddle A
        ball.setx(-340)  # Move the ball back within the paddle's bounds
        ball.dx *= -1  # Reverse the ball's x-axis direction

    time.sleep(1/60)  # Add a small delay for smooth gameplay
