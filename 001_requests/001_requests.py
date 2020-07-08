import requests

def main():
    while True:
        print("1. First type of requests \n2. Second type of requests\n3. Third type of requests\n4. Fourth type of requests")
        choice = int(input("Insert choice: "))
        if choice < 1 or choice > 4:
            print("Error")
        
        if choice == 1:
            requests_1()
            break
        
        if choice == 2:
            requests_2()
            break
        
        if choice == 3:
            requests_3()
            break
        
        if choice == 4:
            requests_4()
            break
               
 
def requests_1():
    # Do a HTTP Call (GET) on the host http://www.google.com
    response = requests.get("http://www.google.com")
    
    # This is a Status Code print
    print("Status Code: ", response.status_code)
    print(" ")
    
    # This is the Headers print
    print("Headers: ", response.headers)
    print(" ")
    
    # This is a Content-Type Header print
    print("Content-Type Header: ", response.headers["Content-Type"])
    print(" ")
    
    # This is all the Content page print
    print("Content: ", response.text)
    print(" ")
    

def requests_2():
    # Do a HTTP Call (GET) on the host https://api.exchangeratesapi.io/latest
    
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        # This is a Status Code print
        print("Status Code: ", response.status_code)
        print(" ")
        raise Exception("Request to API have occurred an error")
    
    print("JSON Data: ", response.json())
    
    
def requests_3():
    # Do a HTTP Call (GET) on the host https://api.exchangeratesapi.io/latest
    
    payload = { 'base' : 'USD', 'symbols' : 'GBP' }
    
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    
    if response.status_code != 200:
        # This is a Status Code print
        print("Status Code: ", response.status_code)
        print(" ")
        raise Exception("Request to API have occurred an error")
    
    print("JSON Data: ", response.json())
    
def requests_4():
    
    first_valuta = input("Insert first valuta: ")
    second_valuta = input("Insert second valuta: ")
    
    payload = { 'base' : first_valuta, 'symbols' : second_valuta }
    
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    
    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("Request to API have occurred an error")
    
    response_data = response.json()
    change_tax = response_data["rates"][second_valuta]
    
    print("Data: ", response_data["date"])
    print(f"1 { first_valuta } correspond to { change_tax } { second_valuta } ")

if __name__ == "__main__":
    main()