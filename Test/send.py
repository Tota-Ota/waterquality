import requests
import time

def send_data_to_server(url, data_string):
    try:
        # Set headers
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # Send POST request to the server
        response = requests.post(url, data=data_string, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data sent successfully to the server.")
        else:
            print(f"Failed to send data. Server returned status code: {response.status_code}")
            print("Response content:", response.content)
    except requests.RequestException as e:
        print("An error occurred while sending data:", str(e))

# Example usage:
if __name__ == "__main__":
    server_url = 'http://192.168.27.132:8001/'  # Replace with your server URL
    data_to_send = "pH=7&Turbidity=100&Temperature=27"

    while True:
        send_data_to_server(server_url, data_to_send)
        time.sleep(5)
