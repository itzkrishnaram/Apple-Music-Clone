# 🎵 Apple Music Recreation  

A **full-stack music streaming application** that enables users to browse, stream, and manage playlists efficiently.  
Built with **React.js** for the frontend, **FastAPI with SQLAlchemy** for the backend, and **MongoDB** for data storage.

## 🚀 Features  
- 🎧 **Music Streaming:** Play and explore songs from the database.  
- 📂 **Playlist Management:** Create, update, and delete playlists.  
- 🔑 **User Authentication:** Secure login and signup using JWT.  
- 📡 **FastAPI Backend:** Handles requests and integrates with the database.  
- 📊 **MongoDB Database:** Stores users, songs, playlists, and subscriptions.  
- 📀 **SQLAlchemy Integration:** Efficient ORM for database interactions.  

## 🛠 Tech Stack  

### **Frontend (React.js)**  
- Calls backend APIs (`GET /songs`, `POST /playlist`, etc.).  
- Displays the music player UI with a **responsive design**.  
- Manages user interactions and state with **React Hooks**.  
- Utilizes **Axios** for making API requests.  

### **Backend (FastAPI + SQLAlchemy)**  
- Implements **CRUD operations** for managing users, songs, and playlists.  
- Uses **SQLAlchemy ORM** for efficient database handling.  
- Secures API endpoints with **JWT authentication**.  
- Handles user requests and integrates with **MongoDB**.  
- Implements **asynchronous processing** for better performance.  

### **Database (MongoDB)**  
- Stores **users, playlists, songs, and subscription details**.  
- Ensures **efficient data retrieval and scalability**.  
- Uses **Indexes** for faster queries and optimized performance.  

---

## 🔧 Installation & Setup  

### **Prerequisites**  
Make sure you have the following installed on your system:  
- **Node.js** (for running the React frontend)  
- **Python 3.8+** (for FastAPI backend)  
- **MongoDB** (local or cloud instance like MongoDB Atlas)  

### **Clone the Repository**  
```sh
git clone https://github.com/itzkrishnaram/apple-music-recreation.git
cd apple-music-recreation
