
# Classified Ads Website

This project is a Django-based classified ads website. Companies can register and post classified ads, while regular users can browse and interact with these ads. 

## Features

- User and Company registration
- User authentication and authorization
- Posting, updating, and deleting classified ads
- Displaying classified ads with detailed views
- Success and error messaging
- User group-based permissions
- Modal delete confirmation
- Toast notifications for success messages
- Company dashboard for managing ads

## Installation

### Prerequisites

- Python 3.7+
- Django 5.0.6
- Pip (Python package installer)
- Tabler v1.0.0-beta20

### Clone the Repository

```bash
git clone [https://github.com/upadesh/Classified-App.git]
cd Classified-App


### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

## Usage

### Accessing the Admin Panel

Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created earlier.

### Registering a Company

1. Navigate to `http://127.0.0.1:8000/company/register`.
2. Fill out the registration form and submit.

### Registering a User

1. Navigate to `http://127.0.0.1:8000/user/register`.
2. Fill out the registration form and submit.

### Posting a Classified Ad (Company Users Only)

1. Log in with a company account.
2. Navigate to `http://127.0.0.1:8000/listing/submit_ads`.
3. Fill out the ad submission form and submit.

### Updating or Deleting an Ad

1. Log in with a company account.
2. Navigate to the ad detail page.
3. Use the provided buttons to update or delete the ad.

## Code Overview

### Models

- `User`: The user model extended with phone and company_name fields.
- `Company`: A proxy model extending the user model for companies.
- `ClassifiedAd`: The model for classified ads with fields for title, description, price, contact details, location, images, and status.

### Forms

- `CompanyRegistrationForm`: Custom form for company registration.
- `ClassifiedAdForm`: Form for creating and updating classified ads.

### Views

- `CompanyRegisterView`: Handles company registration.
- `ClassifiedAdCreateView`: Handles creating classified ads.
- `ClassifiedAdUpdateView`: Handles updating classified ads.
- `ClassifiedAdDeleteView`: Handles deleting classified ads with modal confirmation.
- `ClassifiedAdDetailView`: Handles displaying detailed view of an ad.

### Templates

- `company/register.html`: Company registration form template.
- `listing/submit_ads.html`: Ad submission form template.
- `listing/update_ads.html`: Ad update form template.
- `listing/detail.html`: Ad detail view template.
- `listing/list_ads.html`: List of ads with delete confirmation modal and success toast.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

For any inquiries or support, please contact [upadesh@outlook.com].
