# Django ORM Mastery

**Django ORM Mastery** is a hands-on project developed to help understand and master Django's ORM features. This project contains examples and implementations of various ORM queries, model relationships, signal handling, transactions, and custom managers.

## Features

- **Models**: Includes models such as `Students`, `Marks`, and `Students_details` to simulate a student records management system.
- **Querying**: Demonstrates advanced query methods, including aggregations, filtering with `Q` objects, and annotating data.
- **Transactions**: Uses Django's transaction management for atomic operations, ensuring data consistency.
- **Signals**: Implements Django signals to automate actions on model instance creation or updates.
- **Raw SQL**: Shows how to execute raw SQL queries when necessary for custom data fetching.
- **Custom Managers**: Custom manager classes to add custom query methods for specific data retrieval needs.
- **Admin Customization**: Uses Grappelli to enhance the Django admin interface for a more intuitive and visually appealing user experience.

## Installation

1. Clone the repository:
    ```bash
    https://github.com/shanu-shahbin/Django_Orm_mastery.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django_orm_mastery
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

Access the Django admin panel at `http://127.0.0.1:8000/admin`. Use the admin interface to add and view data for `Students`, `Marks`, and `Students_details` models. Additionally, the project includes custom query examples and showcases the Django ORM's flexibility.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is open-source and available under the MIT License.

