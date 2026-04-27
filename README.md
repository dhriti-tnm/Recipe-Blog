# Recipe Blog

A Django-based recipe management system demonstrating full-stack backend development, REST API design, containerization, and CI/CD automation using Jenkins.

---

## Overview

Recipe Blog is a web application built with Django that allows users to create, manage, and search recipes with image support. The project is containerized using Docker and integrates a CI/CD pipeline using Jenkins, triggered via GitHub webhooks.

This project was developed primarily for learning and experimentation while also following production-like development practices.

---

## Features

- User authentication system (login/logout)
- Full CRUD functionality for recipes
- Image upload support for recipes
- Recipe search functionality
- REST API for recipe operations
- Dockerized application setup using Docker Compose
- CI/CD pipeline integration with Jenkins
- Webhook-based automated pipeline triggering

---

## Tech Stack

- Backend: Django
- API: Django REST Framework
- Database: SQLite (default Django configuration)
- Containerization: Docker, Docker Compose
- CI/CD: Jenkins (webhook-triggered pipelines)

---

## Architecture Overview

- Django handles core application logic and routing
- Django REST Framework exposes API endpoints for recipe data
- Media files (recipe images) are handled within Docker container setup
- Docker Compose manages service orchestration
- Jenkins pipeline is triggered via GitHub webhooks on repository updates
- CI/CD pipeline automates build and deployment workflow

---

## API

The application exposes RESTful endpoints for managing recipes, including:

- Create recipe
- Retrieve recipe(s)
- Update recipe
- Delete recipe
- Search recipes

API structure and endpoint details can be reviewed directly in the Django REST Framework configuration within the project.

---

## CI/CD Pipeline

The project includes a Jenkins-based CI/CD pipeline configured to:

- Trigger automatically via GitHub webhooks
- Build and validate the application
- Rebuild Docker images when changes are pushed
- Support automated deployment workflow (based on pipeline configuration)

---

## Project Purpose

This project was built to explore and practice:

- Django backend development
- REST API implementation using Django REST Framework
- File and image handling in web applications
- Docker-based development workflows
- CI/CD pipeline setup using Jenkins and GitHub webhooks
- Real-world backend system structuring

---

## Status

This is an active learning project and is continuously evolving as new tools, workflows, and improvements are tested and integrated.

---

## Notes

- No external installation instructions are provided as the project is fully managed via Docker Compose.
- Configuration details are intended to be explored within the codebase and Docker setup.

---
