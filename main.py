import requests
import time
def verifyTransaction(transaction_id, account_number, download_pdf=False):
    url = f"https://apps.cbe.com.et:100/?id={transaction_id}{account_number}"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        if(download_pdf):
            with open(f"{str(time.time())}.pdf", 'wb') as f:
                f.write(response.content)
            print("PDF downloaded successfully")
        return response.status_code
    else:
        return response.status_code

transaction_id = "your_transaction_id"
account_number = "your_or_receiver_account_number"
verifyTransaction(transaction_id, account_number,True)
