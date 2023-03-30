# Azure OpenAI Service GPT UI

This Docker image is designed to run text generation tasks using the Azure OpenAI Service's GPT model. The image is available on Docker Hub as [jkudo/azure-openai-gpt](https://hub.docker.com/r/jkudo/azure-openai-gpt).

## Prerequisites

To use this Docker image, you'll need Docker installed on your machine. If you don't have Docker installed, you can refer to the [official Docker documentation](https://docs.docker.com/get-docker/).

You'll also need an Azure OpenAI Service account and an API key. You can obtain an API key from the [OpenAI Dashboard](https://beta.openai.com/dashboard/api-credentials).

## Usage

To run text generation tasks using this Docker image, follow these steps:

1. Clone this repository and copy it to your local machine.

2. Build the Docker image with the following command:

`docker build -t azure-openai-gpt .`

3. Start a Docker container with the following command:

`docker run --rm -p 5000:5000 -e OPENAI_API_BASE="<OPENAI_API_BASE>" -e OPENAI_API_KEY="<OPENAI_API_KEY>" -e OPENAI_ENGINE="<OPENAI_ENGINE>" azure-openai-gpt
`

4. Open your browser and go to `http://localhost:5000` to open the UI.

5. Click the "Send" button in the UI to start Chat.
