from azure.identity import ClientSecretCredential, InteractiveBrowserCredential
from pbipy import PowerBI

import json
from os.path import exists
import re

# https://www.datalineo.com/post/power-bi-rest-api-with-python-part-iii-azure-identity
# https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups

tenant_id = '2fc13e34-f03f-498b-982a-7cb446e25bc6'
client_id = '91a317e3-a2b3-4c75-854a-bdab1928ebb0'
client_secret = 'abcdefg123456***abcdefg123456'
scope = 'https://analysis.windows.net/powerbi/api/.default'


# client_secret_credential_class = ClientSecretCredential(
#     tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
# access_token_class = client_secret_credential_class.get_token(scope)
# token_string = access_token_class.token
# print(token_string)
token_file = "token_file.txt"
response_file = "response.json"
# pbi_group = "93ae130b-02b5-4258-b7d3-f2802f64f735"
pbi_report = "93ae130b-02b5-4258-b7d3-f2802f64f735"
pbi_dataset = "f180c734-b2a1-4872-8da9-f575446c9e23"

if not exists(token_file):
    interactive_browser_credential_class = InteractiveBrowserCredential()
    token_string = interactive_browser_credential_class.get_token(scope).token
    with open(token_file, mode="w+", encoding="utf-8") as ff:
        ff .write(token_string)
else:
    with open(token_file, mode="r", encoding="utf-8") as ff:
        token_string = ff.read()

pbi = PowerBI(token_string)
# admin = pbi.admin()
# admin.datasets(pbi_group)
# report.download("./")

# qry = "SELECT * FROM $System.TMSCHEMA_PARTITIONS" # Need US
qry = "EVALUATE TOPN(10,'fact_sales_with_retailers_profit_pool')"
# qry = "SELECT * FROM $System.DISCOVER_CALC_DEPENDENCY"
qry = "select * from $System.TMSCHEMA_OBJECT_TRANSLATIONS"


ds = pbi.dataset(pbi_dataset)
for ds in ds.datasources():
    print(ds)
