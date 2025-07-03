# ALX Travel App

A Django REST API for a travel booking application.

## Features

- **Listings Management**: Create, read, update, and delete travel listings
- **API Documentation**: Swagger/OpenAPI documentation available
- **Image Support**: Upload and manage listing images
- **Search & Filter**: Search listings by location, type, price, and guest capacity
- **Authentication**: Token-based authentication
- **Admin Interface**: Django admin for managing listings

## Tech Stack

- **Backend**: Django 5.2.4
- **API**: Django REST Framework
- **Database**: MySQL (configurable via environment)
- **Task Queue**: Celery
- **Documentation**: drf-yasg (Swagger)
- **Image Processing**: Pillow

## Installation

1. **Clone the repository**
   ```bash
   git clone 
   cd alx_travel_app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Copy `.env.example` to `.env` and configure your settings:
   ```bash
   cp .env.example .env
   ```

5. **Configure database**
   Update the database settings in `.env`:
   ```
   DB_NAME=alx_travel_db
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout

### Listings
- `GET /api/v1/listings/` - List all listings
- `POST /api/v1/listings/` - Create a new listing
- `GET /api/v1/listings/{id}/` - Get listing details
- `PUT /api/v1/listings/{id}/` - Update listing
- `DELETE /api/v1/listings/{id}/` - Delete listing
- `GET /api/v1/listings/search/` - Search listings with filters
- `GET /api/v1/listings/my_listings/` - Get current user's listings

### Documentation
- `GET /swagger/` - Swagger UI
- `GET /redoc/` - ReDoc UI

## Query Parameters for Search

- `location` - Filter by location
- `type` - Filter by listing type (hotel, apartment, house, villa, hostel)
- `min_price` - Minimum price per night
- `max_price` - Maximum price per night
- `guests` - Minimum number of guests

## Example API Usage

### Search for listings
```bash
curl "http://localhost:8000/api/v1/listings/search/?location=nairobi&type=hotel&min_price=50&max_price=200&guests=2"
```

### Create a new listing
```bash
curl -X POST "http://localhost:8000/api/v1/listings/" \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Beautiful Apartment in Nairobi",
    "description": "A cozy apartment in the heart of Nairobi",
    "listing_type": "apartment",
    "price_per_night": 100.00,
    "location": "Nairobi",
    "address": "123 Main Street, Nairobi",
    "max_guests": 4,
    "bedrooms": 2,
    "bathrooms": 1,
    "amenities": ["wifi", "kitchen", "parking"]
  }'
```

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` with your superuser credentials to manage listings and users.

## Celery (Optional)

For background tasks, you can set up Celery:

1. **Install Redis** (as message broker)
   ```bash
   sudo apt-get install redis-server
   ```

2. **Start Celery worker**
   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
The project follows Django coding standards and PEP 8.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
