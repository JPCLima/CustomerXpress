# CustomerXpress

CustomerXpress is a CRM (Customer Relationship Management) web application built using Django. It allows businesses to manage customer information, track orders, and provide a seamless experience for both customers and administrators.

## Features

1. User Registration and Authentication:

   - New users can register an account with a username, email, password, phone, and address.
   - User authentication ensures secure access to the application.

2. User Roles and Permissions:

   - Different user roles, such as "admin" and "customer," with specific permissions and access levels.
   - Admin users have full control over the application, while customer users have limited access to their own orders and account settings.

3. Dashboard and Analytics:

   - Admin users have access to a comprehensive dashboard displaying key metrics, including total orders, delivered orders, and pending orders.
   - Analytics provide insights into customer behavior, order trends, and other relevant data.

4. Order Management:

   - Admin users can create, update, and delete orders.
   - Customers can view their own orders and update order status.
   - Filtering and search functionality for efficient order management.

5. Product Catalog:

   - Admin users can manage a catalog of products, including product name, price, category, and description.
   - Customers can browse and view products.

6. Customer Management:

   - Admin users can manage customer information, including name, phone, email, and address.
   - Customer profiles provide a holistic view of customer details and order history.

7. Account Settings:

   - Customers can update their account information, including profile picture, phone, email, and address.

8. Pagination:
   - Efficient pagination implemented for the orders and customers lists, providing a smooth browsing experience.

## Technology Stack

The CustomerXpress CRM web application is built using the following technologies and frameworks:

- Django
- Bootstrap
- HTML
- CSS

## Setup Instructions

To get started with the Delights-Inventory project, follow these instructions:

1. Clone the repository:

```
git clone https://github.com/JPCLima/CustomerXpress
```

2. Install the necessary dependencies by running

```
pip install django
```

3. Set up the database by running the migrations:

```
python manage.py migrate
```

4. Create a superuser account:

```
 python manage.py createsuperuser
```

5. Start the development server:

```
python manage.py runserver.
```

6. Access the project by opening a web browser and navigating to

```
http://localhost:8000/
```
