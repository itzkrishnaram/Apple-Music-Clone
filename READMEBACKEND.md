

LOOM VIDEO LINK - https://www.loom.com/share/4b88f0073b824545aab470018d17108d
# Backend - Music Dashboard API

## Overview
This is the backend part of the Music Dashboard Application. The backend is built using Node.js and Express, providing RESTful APIs that serve music data to the frontend.

## Features
- **RESTful API**: Exposes APIs to get songs, playlists, and rankings.
- **Database Integration**: The backend interacts with a database to fetch music data like songs, artists, and album information.

## Installation

### Prerequisites:
Make sure you have the following installed:
- [Node.js](https://nodejs.org/) (Version 14 or higher)
- [npm](https://www.npmjs.com/) (Node package manager)
- [MongoDB](https://www.mongodb.com/) (for database)

### Steps to Install and Run:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/music-dashboard-backend.git
    cd music-dashboard-backend
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Set up the database and add relevant configurations for MongoDB or your preferred database.
4. Start the server:
    ```bash
    npm start
    ```
5. The backend server should be running on `http://localhost:5000`.

## API Endpoints:
- `GET /api/songs`: Fetch a list of songs.
- `GET /api/playlists`: Fetch a list of playlists.
- `GET /api/top-ranked`: Get top-ranked songs based on duration.

## Folder Structure
- **controllers/**: Contains logic for handling API requests.
- **models/**: Contains database models for songs, artists, and playlists.
- **routes/**: Contains API route definitions.
- **server.js**: Entry point for the Node.js application.

## Technologies Used:
- **Node.js**: JavaScript runtime for server-side operations.
- **Express**: Web framework for building APIs.
- **MongoDB**: NoSQL database for storing music-related data.
- **Mongoose**: ODM (Object Data Modeling) library for MongoDB.

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute!

## License
This project is licensed under the MIT License.