# 📸 AuraGram_AI-Powered-Social-Media

**Target:** Build an app that we can share images with intelligent AI features, improve user experience through automation and personalization.

## 📖 Introduction

- **AuraGram** is not a common social media. The project focuses on deeply integrating **AI** to solve user problems such as lack of ideas when writing captions, intelligent image searching based on semantic instead of keywords, and image personalization.

- The project is designed with Clean Architecture and clear separation between processing stages facilitates easy expansion and maintenance.

---

## 🚀 Features

### 1. Social Media Foundation
* **Authentication:** Signup and Login (JWT / Firebase Auth).
* **Feed System:** Browse through a list of posts with images and captions, with support for Like/Comment interactions.
* **Upload:** Upload images from devices(AWS S3).
* **Profile:** The profile page displays the user's image grid layout.

### 2. AI Core
* **Content AI:** Automatically generate engaging captions and suggest relevant hashtags based on the image content (Gemini API).
* **Image AI (AI Stylist):** Integrates beauty filters or style transfers images into paintings/anime using Stable Diffusion.

### 3. Smart Search & Explore
* **Object Detection:** Automatically detects objects in images when uploaded and tags them (e.g., #dog, #sunset, #food).
* **Semantic Search:** Searches based on natural semantics. Example: Typing "beach" will show images of beaches even if the caption doesn't contain that word.

### 4. UI/UX
* **Infinite Scroll:** Infinite scrolling for an optimized feed browsing experience.
* **Real-time Notifications:** Receive instant notifications when someone Likes or Comments (Uses Socket.io).
* **AI Chatbot:** Virtual assistant that helps suggest replies to messages or create images quickly.

---

## 🛠 Tech Stack

| Element | Technology |
| :--- | :--- |
| **Frontend** | React Native (Mobile) hoặc React.js (Web) |
| **Backend** | Python (FastAPI) |
| **Database** | PostgreSQL hoặc MongoDB (Lưu trữ Metadata & Vector) |
| **AI Models** | Google Gemini API, TensorFlow.js |
| **Storage** | AWS S3 |
| **Real-time** | Socket.io |

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