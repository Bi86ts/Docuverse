# Team_GitForge

Enhance and manage documentation for software repositories with ease.

## About

Team_GitForge is a full-stack application that integrates with GitHub to help developers generate and maintain comprehensive documentation for their codebases. It simplifies the process of creating walkthroughs, visual diagrams, and structured documentation, making it easier to onboard new team members or contribute to open-source projects.

## Features

- Connect GitHub repositories
- Generate documentation automatically
- Create visual diagrams
- Produce AI voice narrations for walkthroughs
- Manage repository files
- Execute code in a sandbox environment
- Analyze code dependencies
- Store and retrieve documentation and assets

## Tech Stack

- **Backend:** Python, FastAPI, AWS DynamoDB, AWS S3
- **Frontend:** React, Next.js
- **Services:** Microsoft Edge-TTS, Amazon Bedrock

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- AWS account (for DynamoDB and S3)
- GitHub account

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Bi86ts/Team_GitForge.git
    cd Team_GitForge
    ```

2. Set up the backend:
    ```sh
    cd backend
    pip install -r requirements.txt
    ```

3. Set up the frontend:
    ```sh
    cd../frontend
    npm install
    ```

### Running the Application

1. Start the backend server:
    ```sh
    cd backend
    uvicorn app.main:app --reload
    ```

2. Start the frontend development server:
    ```sh
    cd../frontend
    npm run dev
    ```

## Project Structure

- **`backend/`**: Contains the server-side code, including API endpoints and services.
- **`frontend/`**: Contains the client-side code, built with React and Next.js.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

MIT

## Code Improvements Applied

- Added regression tests for high-risk files: `Bi86ts-Team_GitForge-c2c428b8aa4203c26e42644f79bfc3632a1566cf/frontend/src/app/providers.tsx`, `frontend/src/app/providers.tsx`, `Bi86ts-Team_GitForge-c2c428b8aa4203c26e42644f79bfc3632a1566cf/backend/app/main.py`.
- Proposed extraction of shared utility code into a dedicated module to reduce coupling.
- Updated and regenerated documentation walkthroughs/diagrams post structural changes.
