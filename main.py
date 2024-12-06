import requests
import time

def verifyTransaction(transaction_id, account_number, download_pdf=False):
    url = f"https://apps.cbe.com.et:100/?id={transaction_id}{account_number}"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        if download_pdf:
            filename = f"{int(time.time()*int(account_number))}.pdf"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"PDF downloaded successfully")

        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

transaction_id = "FT24110G8YL1"
account_number = "42690937"
status_code = verifyTransaction(transaction_id, account_number, True)
if status_code is not None:
    print(f"Status code: {status_code}")
