# Lab: 34 - Putting it All Together

---

### Project: Putting it All Together
### Authors: Daniel Brott & Alejandro Rivera

---

### Setup

* Install dependencies in a `venv`
  * **run:** pip install -r requirements.txt
* Dependencies:
  * [requirements.txt](requirements.txt)
* Update `.env` file with secret key


### How to initialize / run application

* Initialize server:
  * **run:** docker-compose up --build

### Links and Resources

* main page:
  * Mac: http://0.0.0.0:8000/
  * Windows: http://localhost:8000/
* api page:
  * Mac: http://0.0.0.0:8000/api/v1/cookie_stands/
  * Windows: http://localhost:8000/api/v1/cookie_stands/
* admin page:
  * Mac: http://0.0.0.0:8000/admin/
  * Windows: http://localhost:8000/admin/
    * username: admin
    * password: admin

### Tests

* **run:** python3 manage.py test
