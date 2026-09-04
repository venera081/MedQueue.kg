# MedQueue KG

**MedQueue KG** is a backend system for a clinic appointment management application designed for patients and clinics in Kyrgyzstan.

The system allows patients to find doctors, choose an available time slot, book appointments, and check in at the clinic. Doctors can manage their schedules and appointments, while administrators can manage clinics, doctors, and other system data.

The project supports **Russian and Kyrgyz languages**.

##  Main Features

* User registration and authentication
* JWT-based authentication
* Role-based access control
* Patient, doctor, and administrator roles
* Clinic management
* Medical specialization management
* Doctor profiles
* Doctor schedules
* Automatic generation of available appointment slots
* Appointment booking and cancellation
* Protection against double booking
* Patient check-in
* Notifications
* Russian and Kyrgyz language support
* Django Admin
* REST API
* API documentation with Swagger/OpenAPI

##  Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL** — production database
* **SQLite** — development
* **SimpleJWT** — authentication
* **django-modeltranslation** — multilingual database content
* **Redis**
* **Celery** — background tasks
* **Docker / Docker Compose**
* **Swagger / OpenAPI**
* **Git / GitHub**

##  Project Architecture

The project is divided into several Django applications:

```text
MedQueue_KG/
├── users/
├── clinics/
├── appointments/
├── notifications/
├── config/
└── manage.py
```

### Main entities

* **User** — patients, doctors and administrators
* **Clinic** — medical clinics
* **Specialization** — medical specializations
* **Doctor** — doctor profiles and information
* **Schedule** — doctor's working hours
* **Appointment** — patient appointments
* **Notification** — system notifications

##  Authentication & Permissions

The API uses **JWT authentication**.

Different user roles have different permissions:

* **Patient** — can search for doctors, view available slots, book and cancel appointments, and check in.
* **Doctor** — can manage their schedule and view their appointments.
* **Admin** — can manage clinics, doctors, specializations, schedules, users and appointments.

##  Appointment System

When a patient books an appointment, the system checks:

1. Whether the doctor exists.
2. Whether the doctor works at the selected clinic.
3. Whether the selected date is available.
4. Whether the selected time belongs to the doctor's schedule.
5. Whether the time slot has already been booked.

The system also protects against **double booking** using database constraints and transactions.

##  Localization

MedQueue KG supports:

* 🇷🇺 Russian
* 🇰🇬 Kyrgyz

Django internationalization is used for system messages, while `django-modeltranslation` is used for multilingual database content such as clinic names, specializations and doctor information.

##  Notifications

The notification system can inform users about important appointment events, such as:

* appointment creation
* appointment confirmation
* appointment cancellation
* appointment reminders
* check-in

Background tasks can be handled using **Celery and Redis**.

##  Project Status

🚧 **In development**

The project is currently being developed from scratch. New features, tests, API endpoints and infrastructure improvements will be added progressively.

##  Project Goals

The main goals of the project are:

* Build a real-world REST API using Django REST Framework.
* Practice backend architecture and database design.
* Implement authentication and role-based permissions.
* Work with scheduling and appointment business logic.
* Learn how to prevent race conditions and double booking.
* Practice testing, Docker, background tasks and API documentation.
* Build a production-oriented backend project for a healthcare application.

##  Future Improvements

Possible future features include:

* Push notifications
* Appointment reminders
* Doctor search and filtering
* Advanced appointment management
* Automated background tasks
* More comprehensive test coverage
* Production deployment
* Monitoring and logging

##  Author

**Venera**

Backend Developer

Built with Python, Django and Django REST Framework.
