# Personal Illustration Portfolio Website

This project is a personal illustration portfolio website, where I showcase my artwork and designs. I have developed the front-end, back-end, and handled the UI/UX design to create a seamless experience for showcasing my illustrations, tools, and collections.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Models Overview](#models-overview)
- [Future Enhancements](#future-enhancements)


## Features

- **Collections Management**: Organize illustrations into collections, mark favorites, and add descriptions.
- **Tool Association**: Link each illustration with the tools used to create them.
- **Video Integration**: Upload and associate videos with illustrations.
- **User Authentication**: Custom user model with avatar support.
- **Comments**: Users can leave comments on collections.
- **Responsive Design**: Mobile-first design ensuring a seamless experience across devices.

![Capture1](https://github.com/user-attachments/assets/789fa8b7-00e3-4028-9968-3373bcec0f54)
![Capture](https://github.com/user-attachments/assets/6525f61a-f048-4add-84ba-e7c751f01d9b)
![Capture11](https://github.com/user-attachments/assets/731bf6b4-f421-42fb-b27b-ad66428dbc6e)
![Capture10](https://github.com/user-attachments/assets/e59d0dfe-3f09-4e81-8f73-d32b43e3b386)
![Capture9](https://github.com/user-attachments/assets/91255f25-f667-43dd-a69b-3c9d70946525)
![Capture8](https://github.com/user-attachments/assets/3385b5a8-9493-4f10-8cf5-87b3392db04e)
![Capture7](https://github.com/user-attachments/assets/1a8370ec-3ab5-4784-8fb3-ced59c159390)
![Capture6](https://github.com/user-attachments/assets/a9f5810d-7097-4fca-9071-e71a66a3defa)
![Capture5](https://github.com/user-attachments/assets/cb894913-d848-458c-872e-0c166411f30e)
![capture4](https://github.com/user-attachments/assets/9aeecca3-9ca6-46d1-9f33-bbe805493deb)
![Capture3](https://github.com/user-attachments/assets/b2aa365f-eeda-45fc-a5bf-9deb35e12e3f)
![Capture2](https://github.com/user-attachments/assets/eb65d15e-940a-4bee-b0b3-8d67411c73c4)


## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (with Django templates)
- **Database**: SQLite (default, can be swapped with PostgreSQL or MySQL)
- **Authentication**: Custom User model extending Django's `AbstractUser`
- **Deployment**: Instructions for Vercel deployment

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the website:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Use the admin panel to manage collections, tools, illustrations, videos, and users.
- **Frontend**: Explore the portfolio, view collections, and comment on your favorite artworks.

## Models Overview

### Collections
- `name`: The name of the collection.
- `description`: Optional description of the collection.
- `created_at`: Timestamp for when the collection was created.
- `is_favorite`: Boolean to mark favorite collections.

### Tools
- `name`: The name of the tool used for the illustrations.

### Illustration
- `image`: The uploaded image of the illustration.
- `name`: The name of the illustration.
- `description`: Optional description of the illustration.
- `tool`: Foreign key linking to the `Tools` model.
- `collection`: Foreign key linking to the `Collections` model.

### Video
- `file`: The uploaded video file.
- `name`: The name of the video.
- `description`: Optional description of the video.
- `illustration`: Foreign key linking to the `Illustration` model.

### User
- Custom user model extending `AbstractUser`.
- `collections`: Many-to-many relationship with `Collections`.
- `avatar`: Optional profile image for users.

### Comment
- `user`: Foreign key linking to the `User` model.
- `collection`: Foreign key linking to the `Collections` model.
- `body`: The comment text.
- `created`: Timestamp for when the comment was created.

## Future Enhancements

- **Search Functionality**: Implement search for illustrations, collections, and tools.
- **Advanced Filtering**: Enable filtering illustrations by tools, collections, or date.
- **User Profiles**: Allow users to create and manage their own profiles.

