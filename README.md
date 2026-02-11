# 📸 AuraGram_AI-Powered-Social-Media

> [cite_start]**Target:** Build an app that we can share images with intelligent AI features, improve user experience through automation and personalization[cite: 1, 2].

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![AI Powered](https://img.shields.io/badge/AI-Powered-blueviolet)

## 📖 Introduction

- **AuraGram** is not a common social media. [cite_start]The project focuses on deeply integrating **AI** to solve user problems such as lack of ideas when writing captions, intelligent image searching based on semantic instead of keywords, and image personalization[cite: 15].

- The project is designed with Clean Architecture and clear separation between processing stages facilitates easy expansion and maintenance.

---

## 🚀 Features

### 1. Social Media Foundation
* [cite_start]**Authentication:** Signup and Login (JWT / Firebase Auth)[cite: 6].
* [cite_start]**Feed System:** Browse through a list of posts with images and captions, with support for Like/Comment interactions[cite: 7].
* [cite_start]**Upload:** Upload images from devices(AWS S3)[cite: 8].
* [cite_start]**Profile:** The profile page displays the user's image grid layout[cite: 9].

### 2. AI Core
* [cite_start]**Content AI:** Automatically generate engaging captions and suggest relevant hashtags based on the image content (Gemini API) [cite: 12].
* [cite_start]**Image AI (AI Stylist):** Integrates beauty filters or style transfers images into paintings/anime using Stable Diffusion[cite: 13].

### 3. Smart Search & Explore
* [cite_start]**Object Detection:** Automatically detects objects in images when uploaded and tags them (e.g., #dog, #sunset, #food)[cite: 16].
* **Semantic Search:** Searches based on natural semantics. [cite_start]Example: Typing "beach" will show images of beaches even if the caption doesn't contain that word[cite: 17].

### 4. UI/UX
* [cite_start]**Infinite Scroll:** Infinite scrolling for an optimized feed browsing experience[cite: 19].
* [cite_start]**Real-time Notifications:** Receive instant notifications when someone Likes or Comments (Uses Socket.io)[cite: 20].
* [cite_start]**AI Chatbot:** Virtual assistant that helps suggest replies to messages or create images quickly[cite: 21].

---

## 🛠 Tech Stack

| Element | Technology |
| :--- | :--- |
| **Frontend** | [cite_start]React Native (Mobile) hoặc React.js (Web) [cite: 23] |
| **Backend** | [cite_start]Python (FastAPI) [cite: 24] |
| **Database** | [cite_start]PostgreSQL hoặc MongoDB (Lưu trữ Metadata & Vector) [cite: 24] |
| **AI Models** | [cite_start]Google Gemini API, TensorFlow.js [cite: 24] |
| **Storage** | [cite_start]AWS S3 [cite: 8] |
| **Real-time** | [cite_start]Socket.io [cite: 20] |

---

## Project Structure

```text
AURAGRAM_PROJECT
├── app/            # Initialize the application, configure the server, and set up middleware (Socket.io, CORS).
├── controller/     # API Endpoints: Receive requests from clients (Auth, Post, Search).
├── core/           # Business Logic & AI Services:
│                   # - Handles core business logic.
│                   # - Integrates Gemini API calls, image processing, and search algorithms.
└── util/           # Shared utility functions (Helpers, Formatters, Validators).
```

## Installation
- Clone GitHub Repository:
```bash
git clone https://github.com/lecuong1502/AuraGram_AI-Powered-Social-Media.git
cd auragram
```

- Install dependencies:
```bash
npm install
```

- Create a new .env file:
```bash
PORT=5000
DATABASE_URL=mongodb://localhost:27017/auragram
GEMINI_API_KEY=your_api_key_here
CLOUDINARY_URL=your_cloudinary_url
JWT_SECRET=your_secret_key
```

- Run the app:
```bash
npm run dev
```

## Usage Guide




## Contributing
All contributions are welcome. Please create a Pull Request or open an Issue to discuss major changes!