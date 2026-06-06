import base64

# raw_configs.txt থেকে লিঙ্কগুলো পড়া
try:
    with open('raw_configs.txt', 'r') as f:
        content = f.read()

    # Base64 এনকোড করা
    encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    # configuration.txt ফাইলে রাইট করা
    with open('configuration.txt', 'w') as f:
        f.write(encoded)
    print("Successfully encoded configs.")
except FileNotFoundError:
    print("raw_configs.txt not found.")
