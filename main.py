import requests
import re
import urllib
import time

def connection(link):
    response = requests.get(link)
    if response.status_code == 200:
        print("Api ile bağlantı sağlandı...")
        print("\nVeriler karşı taraftan alındı...\n")
        reg(response.content)
        pass

def reg(data):
    confirmedcases = re.findall(r"\"confirmed_cases\":(.*?),",data.decode("utf-8"))
    totaltests = re.findall(r"\"total_tests\":(.*?)}",data.decode("utf-8"))
    cctoday    = re.findall(r"\"confirmed_cases_today\":(.*?),",data.decode("utf-8"))
    deaths     = re.findall(r"\"deaths\":(.*?),",data.decode("utf-8"))
    deathstoday= re.findall(r"\"deaths_today\":(.*?),",data.decode("utf-8"))
    date       = re.findall(r"\"publication_date\":(.*?),",data.decode("utf-8"))  
    recoveredpatients = re.findall(r"\"recovered_patients\":(.*?),",data.decode("utf-8"))    
    todaytests = re.findall(r"\"tests_done_today\":(.*?),",data.decode("utf-8"))
    print("**************************************************************************\n\n")
    print("Tarih                == {}".format(date))
    print("\nToplam Test Sayısı   == {}".format(totaltests))
    print("\nBugünkü Test Sayısı  == {}".format(todaytests))
    print("\nToplam Vaka Sayısı   == {}".format(confirmedcases))
    print("\nBugünkü Vaka Sayısı  == {}".format(cctoday))
    print("\nToplam Ölüm Sayısı   == {}".format(deaths))
    print("\nBugünkü Ölüm Sayısı  == {}".format(deathstoday))
    print("\nİyileşen Vaka Sayısı == {}\n".format(recoveredpatients))
    print("\n\n**************************************************************************\n")

print("\n\nTÜRKİYE GÜNLÜK KORONAVİRÜS TABLOSU\n")
connection("http://covid19gunlukleri.com/api/")
print("Veriler anlık olarak https://covid19.saglik.gov.tr/ üzerinden güncellenmektedir.\nmsrexe")
time.sleep(60)
