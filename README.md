# Social Media Platform API

A RESTful API for a social media platform that enables users to create profiles, follow others, create and retrieve
posts, manage likes and comments, and perform essential social media interactions.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Getting Started](#getting-started)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This API provides the backend services for a social media application, supporting user management, social connections,
content creation, and interaction. It follows RESTful principles to ensure scalability and ease of integration with
various frontend clients.

---

## Features

- **User Profiles**  
  Create, retrieve, update, and delete user profiles.

- **Follow System**  
  Follow and unfollow other users; retrieve follower and following lists.

- **Posts**  
  Create, retrieve, update, and delete posts with text and media support.

- **Likes**  
  Like and unlike posts.

- **Comments**  
  Add, retrieve, update, and delete comments on posts.

- **Feed**  
  Retrieve a personalized feed based on followed users.

- **Notifications** (optional, if implemented)  
  Notify users about likes, comments, and follows.

---

## API Endpoints

### Users

| Method | Endpoint                 | Description                 |
|--------|--------------------------|-----------------------------|
| POST   | `/users/`                | Create a new user profile   |
| GET    | `/users/{id}/`           | Retrieve user profile       |
| PUT    | `/users/{id}/`           | Update user profile         |
| DELETE | `/users/{id}/`           | Delete user profile         |
| POST   | `/users/{id}/follow/`    | Follow a user               |
| POST   | `/users/{id}/unfollow/`  | Unfollow a user             |
| GET    | `/users/{id}/followers/` | Get list of followers       |
| GET    | `/users/{id}/following/` | Get list of following users |

### Posts

| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| POST   | `/posts/`      | Create a new post        |
| GET    | `/posts/{id}/` | Retrieve a specific post |
| PUT    | `/posts/{id}/` | Update a post            |
| DELETE | `/posts/{id}/` | Delete a post            |
| GET    | `/posts/feed/` | Retrieve feed posts      |

### Likes

| Method | Endpoint              | Description   |
|--------|-----------------------|---------------|
| POST   | `/posts/{id}/like/`   | Like a post   |
| POST   | `/posts/{id}/unlike/` | Unlike a post |

### Comments

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| POST   | `/posts/{id}/comments/` | Add a comment to a post |
| GET    | `/posts/{id}/comments/` | Retrieve comments       |
| PUT    | `/comments/{id}/`       | Update a comment        |
| DELETE | `/comments/{id}/`       | Delete a comment        |

---

## Authentication

The API uses token-based authentication.

- **Register** and **login** endpoints provide tokens.
- Include the token in the `Authorization` header for protected routes:

