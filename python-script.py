import requests
import time

ifttt_webhook_url = "https://maker.ifttt.com/trigger/my_event/with/key/n8nkmHXJoTt1yTTtQBaWQJJKpOnhqQQ-zuyynbZKsE8"

def check_website():
    # URL of the Met Office weather forecast for York, England
    url = "https://www.metoffice.gov.uk/weather/forecast/gcpvjfy7b"

    # Send a GET request to the website and get the content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the predicted sunshine percentage for the next hour
    sunshine_percentage = soup.find("span", {"data-testid": "hourly_sunshine_percentage_value"}).text.strip()

    # Send a notification if sunshine percentage is above 80%
    if int(sunshine_percentage) > 80:
        print("Sunshine percentage is above 80% - sending notification")
        data = {'value1': 'Sunshine percentage in York, England is predicted to be above 80% in the next hour!'}
        response = requests.post(ifttt_webhook_url, json=data)
        
while True:
    check_website()
    time.sleep(600) # wait for 10 minutes before checking again
