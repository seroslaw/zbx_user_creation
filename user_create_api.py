import requests
import json

if __name__ == '__main__':

    ZABBIX_API_URL = "http://172.19.122.99/zabbix/api_jsonrpc.php"
    UNAME = "api" #Type your user login in Zabbix
    PWORD = "1234" #Type your users pass

api_login = requests.post(
    ZABBIX_API_URL, json={
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                            "username": UNAME,
                            "password": PWORD
                        },
                        "id": 1
    }
)

AUTHTOKEN = api_login.json()["result"]
#print(AUTHTOKEN)

# New user:
USERNAME = input("Input a new user LDAP name: ")

# Request for adding new user to Zabbix
user_create = requests.post(
    ZABBIX_API_URL, json={
                        "jsonrpc": "2.0",
                        "method": "user.create",
                        "params": {
                            "username": USERNAME,
                            "passwd": "1234",          # LDAP user don't need this parameter, it's used only for local users
                            "roleid": "1",              # You need to check id of your role first
                            "usrgrps": [
                                {
                                    "usrgrpid": "14" # You need to check id of your usr grp first
                                }
                            ],
                            },
                            "auth": AUTHTOKEN,
                            "id": 1
        }
    )

print(f"User: {USERNAME} had added to Zabbix server.")
