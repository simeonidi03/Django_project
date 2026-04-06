# GeoLearn

GeoLearn is an educational web application built with Django for studying countries and their key geographical characteristics.

The application helps users learn:
- which languages are spoken by more than half of the population,
- which countries share borders,
- what the largest cities are,
- which international organizations a country participates in.

In addition to the study mode, the project also includes a test mode where users can guess a country using geographical clues.

## Project idea

The goal of the project is to create an educational geography web service for students and anyone interested in countries of the world.

The application combines two approaches:
- **learning mode** — browsing countries and reading information,
- **test mode** — checking knowledge through an interactive guessing task.

## Main features

- Home page with project description
- Countries list page
- Country detail page
- Test mode page
- Add country form
- Edit country form
- Search by country name
- Validation with user-friendly error messages
- Django admin panel for managing data
- Country images displayed in the interface

## Pages

The project contains more than 4 pages, including:

1. **Home** — main page with project description
2. **Countries** — list of countries with search and images
3. **Country detail** — detailed information about one country
4. **Test mode** — geography training page
5. **Add country** — form for creating a new country
6. **Edit country** — form for updating an existing country

## Forms

The project contains more than 2 forms, including:

- Add country form
- Edit country form
- Test answer form

All forms include validation and readable error messages.

## Technologies used

- Python
- Django
- SQLite
- HTML
- CSS

## Data stored in the project

Each country may contain:
- name
- capital
- population
- area
- region
- description
- image
- neighboring countries
- international organizations
- languages with percentages
- largest cities

## Project structure

```text
geolearn_project/
├── config/
├── countries/
│   ├── migrations/
│   ├── templates/
│   │   └── countries/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── country_list.html
│   │       ├── country_detail.html
│   │       ├── country_form.html
│   │       └── test_mode.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md
```

## How to run the project locally

1. Clone the repository

```bash
git clone <your-repository-link>
cd geolearn_project

2. Create a virtual environment
python3 -m venv venv

3. Activate the virtual environment
On macOS / Linux:
```
source venv/bin/activate
```

4. Install Django
pip install django
5. Apply migrations
python manage.py makemigrations
python manage.py migrate
6. Run the server
python manage.py runserver

Then open:

http://127.0.0.1:8000/
Admin panel

To create an admin user:

python manage.py createsuperuser

After that open:

http://127.0.0.1:8000/admin/

The admin panel can be used to:

create countries,
edit countries,
add languages,
add cities,
add organizations,
connect neighboring countries.
Validation examples

The project includes form validation such as:

country name cannot be empty,
capital cannot be empty,
percentage cannot be greater than 100,
answer in test mode cannot be empty,
answer must contain at least 2 characters.
Educational value

This project is designed as a geography learning portal.
It can be useful for:

school students,
university students,
learners preparing for geography quizzes,
users interested in countries and international relations.
