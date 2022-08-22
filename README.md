# Fyyur_app
Udacity Nanodegree project 1. Testing database skills 
This is the first Udacity nanodegree full stack web development project 
Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

Your job is to build out the data models to power the API endpoints for the Fyyur site by connecting to a PostgreSQL database for storing, querying, and creating information about artists and venues on Fyyur.

Overview

This app is nearly complete. It is only missing one thing… real data! While the views and controllers are defined in this application, it is missing models and model interactions to be able to store retrieve, and update data from a database. By the end of this project, you should have a fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

creating new venues, artists, and creating new shows.

searching for venues and artists.

learning more about a specific artist or venue.

We want Fyyur to be the next new platform that artists and musical venues can use to find each other, and discover new music shows. Let's make that happen!

Tech Stack (Dependencies)

1. Backend Dependencies

Our tech stack will include the following:

virtualenv as a tool to create isolated Python environments

SQLAlchemy ORM to be our ORM library of choice

PostgreSQL as our database of choice

Python3 and Flask as our server language and server framework

Flask-Migrate for creating and running schema migrations You can download and install the dependencies mentioned above using pip as:

pip install virtualenv

pip install SQLAlchemy

pip install postgres

pip install Flask

pip install Flask-Migrate

Note - If we do not mention the specific version of a package, then the default latest stable package will be installed.

2. Frontend Dependencies

You must have the HTML, CSS, and Javascript with Bootstrap 3 for our website's frontend. Bootstrap can only be installed by Node Package Manager (NPM). Therefore, if not already, download and install the Node.js. Windows users must run the executable as an Administrator, and restart the computer after installation. After successfully installing the Node, verify the installation as shown below.

node -v

npm -v

Install Bootstrap 3 for the website's frontend:

npm init -y

npm install bootstrap@3
