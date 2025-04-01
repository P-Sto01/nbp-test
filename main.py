import requests
from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

def fetch_currency_rates(date=None):
    """Fetch currency rates from the NBP API. If date is None, fetch current rates."""
    base_url = "https://api.nbp.pl/api/exchangerates/tables/A/"
    url = f"{base_url}{date}/?format=json" if date else f"{base_url}?format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[0]['rates']
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"No data available for the date: {date}. Attempting fallback...")
            # Fallback: Try the previous day if a specific date was requested
            if date:
                previous_date = (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
                return fetch_currency_rates(previous_date)
            return []  # Return an empty list if no fallback is possible
        else:
            print(f"HTTP error occurred: {e}")
            raise
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NBP API: {e}")
        return []

@app.route("/")
def index():
    # Fetch current rates
    current_rates = fetch_currency_rates()
    # Fetch rates from 10 days ago
    ten_days_ago = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')
    past_rates = fetch_currency_rates(ten_days_ago)

    # Calculate differences
    past_rates_dict = {rate['code']: rate['mid'] for rate in past_rates}
    rates_data = []
    for rate in current_rates:
        code = rate['code']
        current_rate = round(rate['mid'], 4)  # Round current rate to 4 decimal places
        past_rate = past_rates_dict.get(code, None)
        difference = round(current_rate - past_rate, 4) if past_rate else None
        rates_data.append({
            'code': code,
            'current_rate': current_rate,
            'difference': difference
        })

    return render_template("index.html", rates=rates_data)

@app.route("/test-favicon")
def test_favicon():
    return app.send_static_file("icon.ico")

if __name__ == "__main__":
    app.run(debug=True)
