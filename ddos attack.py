import requests
global x 
x = input("Enter your url => ")
y = int(input("Enter your number of packet => "))
for i in range(10):
    def send_request(url):
        try:
            response = requests.get(url)
            # You can handle the response here, such as checking the status code or content
            print("Request sent successfully!")
        except requests.exceptions.RequestException as e:
            print("An error occurred: {str(e)}")

    # Example usage
    url_to_request = x
    send_request(url_to_request)
