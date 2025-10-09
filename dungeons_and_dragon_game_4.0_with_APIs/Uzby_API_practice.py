import requests
name = input("Type your name: ")
internet_status = input("Do you have a stable internet connection? (y/n): ")
if internet_status == "y":
    print("Making API request...")
    print("Generating stage name...")
    name = requests.get(f"https://uzby.com/api.php?min={len(name)}&max={len(name)}").text
    print(f"Your {len(name)} character stage name is: {name}")



