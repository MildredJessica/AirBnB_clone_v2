# AirBnB clone - Web framework
## Tasks

### 0. Hello Flask!
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”

### 1. HBNB
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”

### 2. C is fun!

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
     
### 3. Python is cool!

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of text is “is cool”

### 4. Is it a number?

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of text is “is cool”
 - /number/<n>: display “n is a number” only if n is an integer
 - You must use the option strict_slashes=False in your route definition

### 5. Number template
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of text is “is cool”
 - /number/<n>: display “n is a number” only if n is an integer
 - /number_template/<n>: display a HTML page only if n is an integer:
   - H1 tag: “Number: n” inside the tag BODY
- You must use the option strict_slashes=False in your route definition

### 6. Odd or even?
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - The default value of text is “is cool”
 - /number/<n>: display “n is a number” only if n is an integer
 - /number_template/<n>: display a HTML page only if n is an integer:
   - H1 tag: “Number: n” inside the tag BODY
- /number_odd_or_even/<n>: display a HTML page only if n is an integer:
   - H1 tag: “Number: n is even|odd” inside the tag BODY
- You must use the option strict_slashes=False in your route definition