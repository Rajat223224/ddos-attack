import requests
from multiprocessing.pool import ThreadPool

def send_request(url):
    try:
        session = requests.Session()
        response = session.get(url)
        # You can handle the response here, such as checking the status code or content
        print("Request sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

def main():
    url = input("Enter your URL => ")
    num_packets = int(input("Enter the number of packets => "))

    pool = ThreadPool()
    pool.map(send_request, [url] * num_packets)
    pool.close()
    pool.join()

# Run the main function
main()
