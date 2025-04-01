# Currency Rates Web Application

This project is a Flask-based web application that displays current currency rates and their differences compared to rates from 10 days ago. The data is fetched from the NBP (National Bank of Poland) API.

## Features

- Fetches current currency rates from the NBP API.
- Fetches currency rates from 10 days ago for comparison.
- Displays a table with:
  - Currency codes.
  - Current rates (rounded to 4 decimal places).
  - Differences between current rates and rates from 10 days ago (rounded to 4 decimal places).
- Allows sorting the table by:
  - Current rate (ascending/descending).
  - Difference (ascending/descending).
- Responsive design for mobile and desktop.
- Includes a favicon.

## Requirements

- Python 3.7 or higher
- Flask
- Requests library

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd nbp-test
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install flask requests
   ```
6. Run the application:
   ```bash
   python main.py
   ```
7. Open your browser and navigate to `http://127.0.0.1:5000/`.

## File Structure

- `main.py`: The main Flask application file that handles API requests and renders the webpage.
- `templates/index.html`: The HTML template for the webpage.
- `static/icon.ico`: The favicon for the webpage.

## API Endpoints

- `/`: Displays the currency rates table.
- `/test-favicon`: Serves the favicon for testing purposes.

## Notes

- The application uses the NBP API to fetch currency rates. Ensure you have an active internet connection.
- If the API does not have data for a specific date (e.g., weekends or holidays), the application will attempt to fetch data from the previous day.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

##Credits

This was made to test for Claude 3.5 Sonnet's ability to generate simple python application.
