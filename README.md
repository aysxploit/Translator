# LinguaFlash

**LinguaFlash** is a real-time language translation tool built using FastAPI, Google Gemini 1.5 Flash, Gradio, and Supervisor. This tool leverages advanced AI models to provide fast and accurate translations between various languages.

## Features
- Real-time translation of text to multiple languages.
- User-friendly interface with Gradio.
- Scalable and robust architecture using FastAPI and Supervisor.
- Powered by Google Gemini 1.5 Flash for high-quality translations.

## Prerequisites
- Python 3.7+
- An API key for Google Gemini 1.5 Flash
- `pip` for package installation

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/LinguaFlash.git
    cd LinguaFlash
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Google Gemini 1.5 Flash API key:
    ```plaintext
    api_key=YOUR_API_KEY_HERE
    ```

## Usage
### Running the FastAPI Server
1. **Navigate to the project directory:**
    ```bash
    cd LinguaFlash
    ```

2. **Start the FastAPI server:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

### Running the Gradio Interface
1. **In a new terminal window, navigate to the project directory:**
    ```bash
    cd LinguaFlash
    ```

2. **Start the Gradio interface:**
    ```bash
    python app.py
    ```

### Using Supervisor
Supervisor can be used to manage both the FastAPI server and the Gradio interface.

1. **Install Supervisor:**
    ```bash
    sudo apt-get install supervisor
    ```

2. **Copy the `supervisord.conf` file to `/etc/supervisor/conf.d/`:**
    ```bash
    sudo cp supervisord.conf /etc/supervisor/conf.d/linguaflash.conf
    ```

3. **Update Supervisor and start the processes:**
    ```bash
    sudo supervisorctl update
    sudo supervisorctl start all
    ```

## Docker Setup
You can also run LinguaFlash using Docker. Here's how:

1. **Build the Docker image:**
    ```bash
    docker build -t linguaflash .
    ```

2. **Run the Docker container:**
    ```bash
    docker run -d -p 80:80 -p 7860:7860 linguaflash
    ```

### Dockerfile
Here is the content of the Dockerfile:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 and 7860 available to the world outside this container
EXPOSE 80
EXPOSE 7860

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start supervisord 
CMD ["supervisord"]
```

## Testing the FastAPI Endpoint
You can test the FastAPI endpoint using tools like `curl` or Postman. Here's how you can do it using `curl`:

1. **Ensure the FastAPI server is running on port 8000:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

2. **Send a POST request to the `/translate/` endpoint:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/translate/" -H "Content-Type: application/json" -d '{"text": "Hello, world!", "target_language": "es"}'
    ```

3. **Expected Response:**
    ```json
    {
        "translation": "¡Hola, mundo!"
    }
    ```

## Getting a Google Gemini API Key
To use the Google Gemini API, you'll need an API key. Here's how to get one:

1. **Sign in to Google AI Studio:**
    - Go to the Google AI Studio website and sign in with your Google account.

2. **Create a New Project or Select an Existing One:**
    - If you don't have a project, create a new one. If you already have one, select it from the list.

3. **Navigate to the Credentials Section:**
    - In the left menu, select "APIs & Services" and then "Credentials".

4. **Create a New API Key:**
    - Click on "Create credentials" and select "API key".
    - Copy the generated API key and keep it secure.

5. **Add the API Key to Your Project:**
    - Add the API key to your `.env` file as shown in the Prerequisites section.

## API Endpoint
### `/translate/`
- **Method:** POST
- **Request Body:**
    ```json
    {
        "text": "Hello, world!",
        "target_language": "es"
    }
    ```
- **Response:**
    ```json
    {
        "translation": "¡Hola, mundo!"
    }
    ```

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
