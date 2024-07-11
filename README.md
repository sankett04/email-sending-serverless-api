# Email Sender API

This project demonstrates a serverless API that mocks sending emails.

## Setup Instructions

1. Ensure you have Python 3.12 and Node.js installed.

2. Install the Serverless Framework globally:

3. Clone this repository and navigate to the project directory.

4. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

5. Install the required Python packages:

6. Install the Serverless Offline plugin:

## Running the API Locally

1. Start the local server:

2. The API will be available at `http://localhost:3000`

## Testing the API

Use Rest clinet for Vs code, curl or Postman to send a POST request to:
http://localhost:3000/dev/send-email

with a JSON body:
{
"receiver_email": "recipient@example.com",
"subject": "Test Email",
"body_text": "This is a test email."
}

The API will return a success message and print the email details to the console.

Note: This project uses a mock email sending function for demonstration purposes. No actual emails are sent.