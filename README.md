🌸 Snap Sense
Snap Sense is an AI-powered web application designed to visually understand and interact with media. Upload an image or a PDF and interact with it using smart features like summarization, flashcard generation, emotion detection, and visual analysis — all in an elegant, intuitive interface.

✨ Features
📤 Image Upload: Upload images for analysis or emotion recognition.

📚 PDF Upload: Upload documents for summarization and flashcard generation.

🧠 Contextual AI Chatbot: Ask questions about your uploaded content and get intelligent answers.

🎭 Emotion Mapping: Understand the emotional context of artworks or facial expressions.

📝 PDF Summarization: Generate concise summaries from lengthy documents.

🧾 Flashcard Generator: Convert documents into study flashcards.

💬 Interactive Chat Interface: Clean and responsive chat interface with message history.

🧩 Modular Action Buttons: Tap action cards like "Summarize", "Analyze", "Flashcards", or "Emotion Identifier" to get started.

🎨 Aesthetic UI: Light rose-themed layout with modern typography and a custom creative font for "Snap Sense".

🛠 Tech Stack
Frontend: Next.js, TypeScript, Tailwind CSS

AI Backend: Genkit, Gemini API

UI Enhancements: Inter font, Lucide icons

PDF Parsing: Placeholder flow (real parsing to be integrated)

Image Analysis: AI-powered visual reasoning and emotion inference

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/snapsense.git
cd snapsense
2. Install Dependencies
bash
Copy
Edit
npm install
3. Set up Environment Variables
Create a .env.local file and add your Gemini API Key:

bash
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
4. Run the App
bash
Copy
Edit
npm run dev
Visit http://localhost:3000 in your browser to use Snap Sense.

📂 Project Structure
css
Copy
Edit
src/
│
├── ai/
│   ├── flows/
│   │   ├── analyze-image-question-flow.ts
│   │   ├── generate-flashcards-flow.ts
│   │   ├── summarize-text-flow.ts
│   │   └── map-emotion-flow.ts
│   └── dev.ts
│
├── components/
│   ├── chat/
│   │   └── ChatInterface.tsx
│
├── app/
│   ├── actions.ts
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
📸 UI Preview

A modern, clean, and emotionally engaging layout with soft rose colors and interactive cards.

💡 Future Improvements
Integrate full PDF text extraction

Real-time emotion tracking from webcam

Support for more file types (e.g., DOCX, TXT)

Export flashcards as Anki decks

🙌 Contributing
We welcome contributions! Please open an issue or a pull request for suggestions or enhancements.

📝 License
MIT License
