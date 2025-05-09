OVERVIEW OF FILES:
---
(This project makes use of HTML, CSS, Python and Flask)

Head to "templates" to see progress on the GUI:
(Ignore hello.html)
- *contact.html:* contact page
- *index.html:* homepage
- *input.html:* input form 
- *results.html:* predictions page (result of input form, as predicted by our model)
- *style.css:* contains style elements
---
Python files:
- *aces.py:* Random forest model for disease likelihood prediction based on ACE scores. (in progress)
- *__init__.py:* application factory for our Flask app (It defines a create_app() function that initializes and configures our Flask application)
- *config.py:* defines configuration settings for your Flask application across different environments: development, testing, and production.
- *routes.py:* defines URL routes and request handling logic for the Flask web application using a Blueprint named main_bp. It controls what happens when a user visits the homepage (/),fills and submits a form (/predict),receives prediction results.
