Chat Application
A real-time chat application built with Django, Django Channels, and WebSockets. Users can sign up, log in, view all registered users, and initiate a chat with any user. The application supports real-time messaging and stores chat messages in the database.

Setup Instructions
Step 1: Clone the Repository
git clone <repository-url>
cd <repository-name>

Step 2: Apply Database Migrations
Run the following commands to create the necessary database tables:
python manage.py makemigrations
python manage.py migrate


Step 3: Create a Superuser
Create a superuser account to access the Django admin panel:
python manage.py createsuperuser
You’ll be prompted to enter a username, email, and password.


Step 4: Start the Development Server
Run the Django development server:
python manage.py runserver
Visit the application at http://127.0.0.1:8000/.


FrontEnd
1. Open the HTML file in the browser
