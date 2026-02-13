# Digital Twin

An AI-powered digital twin chatbot that represents Kwabena Baah-Boakye on his professional website, providing visitors with an interactive way to learn about his background, skills, and experience.

## Description

This project features an intelligent chatbot that acts as a digital twin, engaging with website visitors and answering questions about Kwabena's professional experience as a Full-Stack Software Engineer and AI Specialist. The chatbot draws from comprehensive source documents including professional profile, resume, and LinkedIn data to provide accurate, contextual responses.

## Tech Stack

**Backend:**
- Python
- FastAPI
- Anthropic Claude API
- pypdf for PDF processing
- AWS Lambda (deployment)

**Frontend:**
- Next.js
- React
- TypeScript
- Tailwind CSS

## Project Structure

```
twin/
├── backend/          # FastAPI backend with AI chatbot logic
│   ├── data/        # Source documents (profile, resume, LinkedIn)
│   ├── context.py   # Digital twin prompt configuration
│   ├── resources.py # Document loaders
│   └── server.py    # API server
└── frontend/        # Next.js frontend application
```

## Setup & Running

### Backend
```bash
cd backend
pip install -r requirements.txt
python server.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Features

- AI-powered conversational interface
- Context-aware responses based on professional documents
- Professional and engaging user experience
- Real-time chat functionality
