import requests
from datetime import datetime, timedelta
from twilio.rest import Client
#TWILIO DATA
from_number = "whatsapp:+14155238886"
to_number =  "whatsapp:+31624153113"
account_sid = 'AC6831e3454cec8d9bf0b9bda1ee1e4812'
auth_token = 'fa9e0fb7ae8b285b0181860f9042176e'
client = Client(account_sid, auth_token)
#PRACTICE DATA
FAKESTOCKDATA= {
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2025-02-03",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2025-02-03": {
            "1. open": "252.4000",
            "2. high": "262.0600",
            "3. low": "251.8400",
            "4. close": "300.7300",
            "5. volume": "8408523"
        },
        "2025-01-31": {
            "1. open": "256.0500",
            "2. high": "257.2350",
            "3. low": "251.8900",
            "4. close": "255.7000",
            "5. volume": "7203519"
        },
        "2025-01-30": {
            "1. open": "250.0000",
            "2. high": "261.8000",
            "3. low": "247.0100",
            "4. close": "258.2700",
            "5. volume": "15381890"
        },
        "2025-01-29": {
            "1. open": "225.6200",
            "2. high": "229.4700",
            "3. low": "223.7300",
            "4. close": "228.6300",
            "5. volume": "7079804"
        },
        "2025-01-28": {
            "1. open": "224.3200",
            "2. high": "225.7700",
            "3. low": "221.7700",
            "4. close": "225.6600",
            "5. volume": "4485429"
        },
        "2025-01-27": {
            "1. open": "222.1900",
            "2. high": "224.3000",
            "3. low": "219.8400",
            "4. close": "224.1300",
            "5. volume": "4898355"
        },
        "2025-01-24": {
            "1. open": "225.2700",
            "2. high": "226.8104",
            "3. low": "223.8000",
            "4. close": "224.8000",
            "5. volume": "3233293"
        },
        "2025-01-23": {
            "1. open": "223.9400",
            "2. high": "226.0400",
            "3. low": "223.1500",
            "4. close": "226.0400",
            "5. volume": "3619651"
        },
        "2025-01-22": {
            "1. open": "221.9800",
            "2. high": "224.4000",
            "3. low": "220.3500",
            "4. close": "223.2600",
            "5. volume": "4759490"
        },
        "2025-01-21": {
            "1. open": "224.9900",
            "2. high": "227.4500",
            "3. low": "222.8302",
            "4. close": "224.2600",
            "5. volume": "3982203"
        },
        "2025-01-17": {
            "1. open": "225.9550",
            "2. high": "225.9550",
            "3. low": "223.6400",
            "4. close": "224.7900",
            "5. volume": "5506837"
        },
        "2025-01-16": {
            "1. open": "219.6900",
            "2. high": "222.6800",
            "3. low": "217.3800",
            "4. close": "222.6600",
            "5. volume": "3329060"
        },
        "2025-01-15": {
            "1. open": "220.8700",
            "2. high": "221.6761",
            "3. low": "218.0100",
            "4. close": "220.0300",
            "5. volume": "2951825"
        },
        "2025-01-14": {
            "1. open": "218.0000",
            "2. high": "218.1250",
            "3. low": "214.6100",
            "4. close": "217.7500",
            "5. volume": "3485829"
        },
        "2025-01-13": {
            "1. open": "217.8900",
            "2. high": "219.5900",
            "3. low": "214.7500",
            "4. close": "217.4000",
            "5. volume": "3716816"
        },
        "2025-01-10": {
            "1. open": "222.0000",
            "2. high": "222.4300",
            "3. low": "216.8000",
            "4. close": "219.7500",
            "5. volume": "3570497"
        },
        "2025-01-08": {
            "1. open": "223.9100",
            "2. high": "224.9000",
            "3. low": "220.8300",
            "4. close": "223.1800",
            "5. volume": "2619768"
        },
        "2025-01-07": {
            "1. open": "223.3500",
            "2. high": "226.7110",
            "3. low": "222.8300",
            "4. close": "223.9600",
            "5. volume": "3299701"
        },
        "2025-01-06": {
            "1. open": "223.0000",
            "2. high": "224.3500",
            "3. low": "220.7500",
            "4. close": "222.6700",
            "5. volume": "2847128"
        },
        "2025-01-03": {
            "1. open": "220.5500",
            "2. high": "223.6600",
            "3. low": "220.5500",
            "4. close": "222.6500",
            "5. volume": "3873578"
        },
        "2025-01-02": {
            "1. open": "221.8200",
            "2. high": "222.4900",
            "3. low": "217.6000",
            "4. close": "219.9400",
            "5. volume": "2579498"
        },
        "2024-12-31": {
            "1. open": "220.7200",
            "2. high": "221.0493",
            "3. low": "218.4400",
            "4. close": "219.8300",
            "5. volume": "2270512"
        },
        "2024-12-30": {
            "1. open": "220.5400",
            "2. high": "221.5942",
            "3. low": "217.6523",
            "4. close": "220.2500",
            "5. volume": "2095565"
        },
        "2024-12-27": {
            "1. open": "223.1400",
            "2. high": "224.4200",
            "3. low": "221.4054",
            "4. close": "222.7800",
            "5. volume": "1810760"
        },
        "2024-12-26": {
            "1. open": "223.3100",
            "2. high": "225.4000",
            "3. low": "222.5500",
            "4. close": "224.8900",
            "5. volume": "3287238"
        },
        "2024-12-24": {
            "1. open": "222.2700",
            "2. high": "224.4446",
            "3. low": "221.5428",
            "4. close": "224.4100",
            "5. volume": "1186216"
        },
        "2024-12-23": {
            "1. open": "222.8100",
            "2. high": "223.7400",
            "3. low": "221.0800",
            "4. close": "221.9300",
            "5. volume": "2988137"
        },
        "2024-12-20": {
            "1. open": "222.7300",
            "2. high": "227.6847",
            "3. low": "221.6800",
            "4. close": "223.3600",
            "5. volume": "12423200"
        },
        "2024-12-19": {
            "1. open": "224.4200",
            "2. high": "226.2000",
            "3. low": "222.9800",
            "4. close": "223.9200",
            "5. volume": "4430120"
        },
        "2024-12-18": {
            "1. open": "229.0350",
            "2. high": "229.0350",
            "3. low": "220.0300",
            "4. close": "220.1700",
            "5. volume": "4152517"
        },
        "2024-12-17": {
            "1. open": "229.2300",
            "2. high": "230.2000",
            "3. low": "227.6200",
            "4. close": "228.9700",
            "5. volume": "3651346"
        },
        "2024-12-16": {
            "1. open": "230.7300",
            "2. high": "231.0300",
            "3. low": "226.8800",
            "4. close": "229.3300",
            "5. volume": "3610257"
        },
        "2024-12-13": {
            "1. open": "232.2500",
            "2. high": "233.7750",
            "3. low": "230.2600",
            "4. close": "230.8200",
            "5. volume": "2757683"
        },
        "2024-12-12": {
            "1. open": "230.6600",
            "2. high": "233.8900",
            "3. low": "230.3800",
            "4. close": "232.2600",
            "5. volume": "4515741"
        },
        "2024-12-11": {
            "1. open": "232.6900",
            "2. high": "233.0000",
            "3. low": "229.1300",
            "4. close": "230.1200",
            "5. volume": "3872680"
        },
        "2024-12-10": {
            "1. open": "228.4000",
            "2. high": "234.3900",
            "3. low": "227.8000",
            "4. close": "231.7200",
            "5. volume": "4769531"
        },
        "2024-12-09": {
            "1. open": "238.0000",
            "2. high": "239.3500",
            "3. low": "228.9100",
            "4. close": "230.0000",
            "5. volume": "4970449"
        },
        "2024-12-06": {
            "1. open": "234.4300",
            "2. high": "238.3800",
            "3. low": "234.2200",
            "4. close": "238.0400",
            "5. volume": "4028430"
        },
        "2024-12-05": {
            "1. open": "233.5500",
            "2. high": "236.5200",
            "3. low": "233.4600",
            "4. close": "234.7500",
            "5. volume": "4791116"
        },
        "2024-12-04": {
            "1. open": "230.0000",
            "2. high": "233.7400",
            "3. low": "229.3500",
            "4. close": "233.4900",
            "5. volume": "4104195"
        },
        "2024-12-03": {
            "1. open": "227.2400",
            "2. high": "229.1100",
            "3. low": "226.6700",
            "4. close": "229.0000",
            "5. volume": "3163815"
        },
        "2024-12-02": {
            "1. open": "227.5000",
            "2. high": "228.3800",
            "3. low": "225.5100",
            "4. close": "227.3900",
            "5. volume": "2656181"
        },
        "2024-11-29": {
            "1. open": "227.7500",
            "2. high": "230.3600",
            "3. low": "227.1900",
            "4. close": "227.4100",
            "5. volume": "2640253"
        },
        "2024-11-27": {
            "1. open": "228.8300",
            "2. high": "229.1900",
            "3. low": "224.2700",
            "4. close": "226.9200",
            "5. volume": "2995121"
        },
        "2024-11-26": {
            "1. open": "226.7300",
            "2. high": "228.9800",
            "3. low": "225.5115",
            "4. close": "228.8300",
            "5. volume": "4449543"
        },
        "2024-11-25": {
            "1. open": "223.3500",
            "2. high": "226.4200",
            "3. low": "222.6500",
            "4. close": "226.1300",
            "5. volume": "7189260"
        },
        "2024-11-22": {
            "1. open": "223.3500",
            "2. high": "227.2000",
            "3. low": "220.8900",
            "4. close": "222.9700",
            "5. volume": "5320740"
        },
        "2024-11-21": {
            "1. open": "215.8100",
            "2. high": "222.6300",
            "3. low": "215.2701",
            "4. close": "222.4000",
            "5. volume": "5236434"
        },
        "2024-11-20": {
            "1. open": "211.0000",
            "2. high": "214.9600",
            "3. low": "209.7725",
            "4. close": "214.6000",
            "5. volume": "4562901"
        },
        "2024-11-19": {
            "1. open": "206.5000",
            "2. high": "210.3300",
            "3. low": "206.1900",
            "4. close": "210.2500",
            "5. volume": "2860746"
        },
        "2024-11-18": {
            "1. open": "207.0000",
            "2. high": "208.4150",
            "3. low": "205.3701",
            "4. close": "208.0900",
            "5. volume": "3406045"
        },
        "2024-11-15": {
            "1. open": "207.4600",
            "2. high": "208.4900",
            "3. low": "204.0700",
            "4. close": "204.9900",
            "5. volume": "3986460"
        },
        "2024-11-14": {
            "1. open": "210.0000",
            "2. high": "210.4999",
            "3. low": "206.3500",
            "4. close": "208.9900",
            "5. volume": "6372853"
        },
        "2024-11-13": {
            "1. open": "209.5000",
            "2. high": "211.4100",
            "3. low": "209.0701",
            "4. close": "210.9200",
            "5. volume": "3247830"
        },
        "2024-11-12": {
            "1. open": "211.9000",
            "2. high": "213.0300",
            "3. low": "209.0600",
            "4. close": "210.8600",
            "5. volume": "2818216"
        },
        "2024-11-11": {
            "1. open": "214.4000",
            "2. high": "215.4100",
            "3. low": "213.4800",
            "4. close": "213.5700",
            "5. volume": "3012987"
        },
        "2024-11-08": {
            "1. open": "214.1600",
            "2. high": "216.7000",
            "3. low": "212.7809",
            "4. close": "213.7200",
            "5. volume": "3201038"
        },
        "2024-11-07": {
            "1. open": "213.6400",
            "2. high": "214.5199",
            "3. low": "211.9300",
            "4. close": "213.6900",
            "5. volume": "3675812"
        },
        "2024-11-06": {
            "1. open": "213.4800",
            "2. high": "214.3300",
            "3. low": "210.3700",
            "4. close": "213.6000",
            "5. volume": "3934386"
        },
        "2024-11-05": {
            "1. open": "206.1700",
            "2. high": "208.1150",
            "3. low": "205.5700",
            "4. close": "207.5700",
            "5. volume": "2441535"
        },
        "2024-11-04": {
            "1. open": "207.6500",
            "2. high": "207.7000",
            "3. low": "205.8000",
            "4. close": "206.3200",
            "5. volume": "2594119"
        },
        "2024-11-01": {
            "1. open": "207.7700",
            "2. high": "209.8400",
            "3. low": "207.4100",
            "4. close": "208.2500",
            "5. volume": "3334308"
        },
        "2024-10-31": {
            "1. open": "204.1300",
            "2. high": "208.1300",
            "3. low": "203.5100",
            "4. close": "206.7200",
            "5. volume": "5925250"
        },
        "2024-10-30": {
            "1. open": "209.4800",
            "2. high": "211.1200",
            "3. low": "204.2600",
            "4. close": "204.9000",
            "5. volume": "6956624"
        },
        "2024-10-29": {
            "1. open": "211.9900",
            "2. high": "213.3400",
            "3. low": "209.8500",
            "4. close": "210.4300",
            "5. volume": "5258366"
        },
        "2024-10-28": {
            "1. open": "215.5000",
            "2. high": "216.2500",
            "3. low": "212.7000",
            "4. close": "212.9100",
            "5. volume": "4993343"
        },
        "2024-10-25": {
            "1. open": "216.8000",
            "2. high": "218.6500",
            "3. low": "214.3850",
            "4. close": "214.6700",
            "5. volume": "8482235"
        },
        "2024-10-24": {
            "1. open": "220.8000",
            "2. high": "221.3200",
            "3. low": "216.1600",
            "4. close": "218.3900",
            "5. volume": "11193440"
        },
        "2024-10-23": {
            "1. open": "230.4100",
            "2. high": "233.3400",
            "3. low": "230.2600",
            "4. close": "232.7500",
            "5. volume": "5791002"
        },
        "2024-10-22": {
            "1. open": "231.9900",
            "2. high": "232.9700",
            "3. low": "230.6700",
            "4. close": "232.2500",
            "5. volume": "3180807"
        },
        "2024-10-21": {
            "1. open": "231.2100",
            "2. high": "232.4200",
            "3. low": "230.2600",
            "4. close": "231.7500",
            "5. volume": "2733336"
        },
        "2024-10-18": {
            "1. open": "231.9200",
            "2. high": "232.6499",
            "3. low": "230.1700",
            "4. close": "232.2000",
            "5. volume": "4715688"
        },
        "2024-10-17": {
            "1. open": "232.0000",
            "2. high": "233.1450",
            "3. low": "230.6550",
            "4. close": "232.8800",
            "5. volume": "5040092"
        },
        "2024-10-16": {
            "1. open": "232.1100",
            "2. high": "233.8800",
            "3. low": "231.1200",
            "4. close": "233.6700",
            "5. volume": "2846669"
        },
        "2024-10-15": {
            "1. open": "236.4000",
            "2. high": "237.3700",
            "3. low": "232.7100",
            "4. close": "232.9600",
            "5. volume": "3350556"
        },
        "2024-10-14": {
            "1. open": "233.5700",
            "2. high": "236.1200",
            "3. low": "233.1700",
            "4. close": "235.2600",
            "5. volume": "2524389"
        },
        "2024-10-11": {
            "1. open": "233.2500",
            "2. high": "233.4400",
            "3. low": "230.4600",
            "4. close": "233.2600",
            "5. volume": "3469322"
        },
        "2024-10-10": {
            "1. open": "235.1000",
            "2. high": "235.8300",
            "3. low": "231.8100",
            "4. close": "233.0200",
            "5. volume": "3142031"
        },
        "2024-10-09": {
            "1. open": "229.2000",
            "2. high": "234.9500",
            "3. low": "228.5000",
            "4. close": "234.3000",
            "5. volume": "5083566"
        },
        "2024-10-08": {
            "1. open": "228.1100",
            "2. high": "229.3450",
            "3. low": "227.0401",
            "4. close": "228.6200",
            "5. volume": "3245342"
        },
        "2024-10-07": {
            "1. open": "225.3800",
            "2. high": "227.6700",
            "3. low": "225.0200",
            "4. close": "227.1200",
            "5. volume": "3457952"
        },
        "2024-10-04": {
            "1. open": "223.7500",
            "2. high": "226.0800",
            "3. low": "223.2700",
            "4. close": "226.0000",
            "5. volume": "3554328"
        },
        "2024-10-03": {
            "1. open": "219.5000",
            "2. high": "222.8300",
            "3. low": "219.2700",
            "4. close": "222.7200",
            "5. volume": "3788265"
        },
        "2024-10-02": {
            "1. open": "218.3100",
            "2. high": "220.2000",
            "3. low": "215.7980",
            "4. close": "219.7300",
            "5. volume": "3343399"
        },
        "2024-10-01": {
            "1. open": "220.6300",
            "2. high": "221.1000",
            "3. low": "215.9000",
            "4. close": "219.3500",
            "5. volume": "3548374"
        },
        "2024-09-30": {
            "1. open": "220.6500",
            "2. high": "221.3200",
            "3. low": "219.0200",
            "4. close": "221.0800",
            "5. volume": "3544264"
        },
        "2024-09-27": {
            "1. open": "223.0000",
            "2. high": "224.1500",
            "3. low": "220.7700",
            "4. close": "220.8400",
            "5. volume": "3830335"
        },
        "2024-09-26": {
            "1. open": "222.1100",
            "2. high": "224.0000",
            "3. low": "221.3550",
            "4. close": "223.4300",
            "5. volume": "2673210"
        },
        "2024-09-25": {
            "1. open": "221.1700",
            "2. high": "221.8500",
            "3. low": "220.1600",
            "4. close": "221.2300",
            "5. volume": "2537751"
        },
        "2024-09-24": {
            "1. open": "219.7800",
            "2. high": "221.1900",
            "3. low": "218.1600",
            "4. close": "220.9700",
            "5. volume": "3184114"
        },
        "2024-09-23": {
            "1. open": "218.0000",
            "2. high": "220.6200",
            "3. low": "217.2700",
            "4. close": "220.5000",
            "5. volume": "4074755"
        },
        "2024-09-20": {
            "1. open": "214.3300",
            "2. high": "217.8500",
            "3. low": "213.7400",
            "4. close": "217.7000",
            "5. volume": "9958980"
        },
        "2024-09-19": {
            "1. open": "218.0100",
            "2. high": "218.4800",
            "3. low": "210.3700",
            "4. close": "213.8900",
            "5. volume": "5279559"
        },
        "2024-09-18": {
            "1. open": "214.1300",
            "2. high": "216.8600",
            "3. low": "213.5900",
            "4. close": "214.9400",
            "5. volume": "3482764"
        },
        "2024-09-17": {
            "1. open": "217.2500",
            "2. high": "218.8400",
            "3. low": "213.0000",
            "4. close": "214.1300",
            "5. volume": "5635210"
        },
        "2024-09-16": {
            "1. open": "215.8800",
            "2. high": "217.9000",
            "3. low": "215.5200",
            "4. close": "217.1600",
            "5. volume": "4176257"
        },
        "2024-09-13": {
            "1. open": "212.4800",
            "2. high": "216.0900",
            "3. low": "212.1300",
            "4. close": "214.7900",
            "5. volume": "4572344"
        },
        "2024-09-12": {
            "1. open": "210.0000",
            "2. high": "212.6500",
            "3. low": "208.2650",
            "4. close": "211.6100",
            "5. volume": "4616446"
        },
        "2024-09-11": {
            "1. open": "207.7600",
            "2. high": "210.1200",
            "3. low": "203.0400",
            "4. close": "209.8900",
            "5. volume": "5554309"
        },
        "2024-09-10": {
            "1. open": "204.2000",
            "2. high": "205.8300",
            "3. low": "202.8700",
            "4. close": "205.3200",
            "5. volume": "3070644"
        }
    }
}
FAKENEWSDATA = {
  'status': 'ok',
  'totalResults': 7,
  'articles': [
    {
      'source': {
        'id': 'business-insider',
        'name': 'Business Insider'
      },
      'author': 'Emily Stewart',
      'title': "One industry just got a big boost from Trump — and it wasn't crypto or Tesla",
      'description': "The president's mass deportation plans could funnel huge profits to private prison companies like Geo and CoreCivic.",
      'url': 'https://www.businessinsider.com/private-prisons-profit-trump-executive-order-immigration-deportation-geo-corecivic-2025-2',
      'urlToImage': 'https://i.insider.com/679bcb2b7bb3f854015b3316?width=1200&format=jpeg',
      'publishedAt': '2025-02-03T09:13:02Z',
      'content': "mactrunk/Getty, Tyler Le/BI\r\nIt's hard to know where to look in the flurry of activity from the opening days of President Donald Trump's second administration. There's Elon Musk at DOGE, a potential … [+12090 chars]"
    },
    {
      'source': {
        'id': None,
        'name': 'Live Science'
      },
      'author': 'Edd Gent',
      'title': '12 pivotal moments in the history of robotics, from Isaac Asimov to self-driving cars',
      'description': "From Isaac Asimov's Three Laws of Robotics to bipedal machines you can buy today, here are 12 important milestones in the development of robots.",
      'url': 'https://www.livescience.com/technology/robotics/history-of-robotics-from-isaac-asimov-to-self-driving-cars',
      'urlToImage': 'https://cdn.mos.cms.futurecdn.net/v8CnGsteD4a5Mm75vLArJj-1200-80.jpg',
      'publishedAt': '2025-02-03T12:00:00Z',
      'content': 'Few technologies have captured the human imagination in quite the same way as robots. The idea of machines that can walk and talk like us has been a staple of science fiction for decades. The reality… [+10355 chars]'
    },
    {
      'source': {
        'id': None,
        'name': 'Technews.tw'
      },
      'author': 'MoneyDJ',
      'title': '川普祭關稅重拳 汽車業首當其衝、特斯拉也遭殃',
      'description': '美國新任總統川普（Donald Trump）開啟關稅戰，全球汽車產業首當其衝，川普親密戰友馬斯克旗下的電動車巨頭特斯拉（Tesla）也受波及。 CNBC、霸榮等外媒報導，川普已簽署行政命令，自2月1日起對自墨西哥和加拿大進口的商品徵收25%高昂關稅，同時對中國商品加徵10%關稅，旨在因應非法移民和芬...',
      'url': 'https://finance.technews.tw/2025/02/03/trump-tariff-war-also-affects-tesla/',
      'urlToImage': 'https://img.technews.tw/wp-content/uploads/2022/02/09160618/shutterstock_1619989447-e1654153124312.jpg',
      'publishedAt': '2025-02-03T02:30:37Z',
      'content': '© 2013-2025 TechNews Inc. All rights reserved. | | | |'
    },
    {
      'source': {
        'id': None,
        'name': 'Securityaffairs.com'
      },
      'author': 'Pierluigi Paganini',
      'title': 'Law enforcement seized the domains of HeartSender cybercrime marketplaces',
      'description': 'U.S. and Dutch authorities seized 39 domains and servers linked to the HeartSender cybercrime group based in Pakistan. A joint law enforcement operation led to the seizure of 39 domains tied to a Pakistan-based HeartSender cybercrime group (aka Saim Raza and …',
      'url': 'https://securityaffairs.com/173750/cyber-crime/heartsender-cybercrime-marketplaces-seized.html',
      'urlToImage': 'https://securityaffairs.com/wp-content/uploads/2015/02/Rule-41-google-fbi-2.jpg',
      'publishedAt': '2025-02-03T06:20:33Z',
      'content': 'Law enforcement seized the domains of HeartSender cybercrime marketplaces\r\n\xa0|\xa0Security Affairs newsletter Round 509 by Pierluigi Paganini INTERNATIONAL EDITION\r\n\xa0|\xa0WhatsApp disrupted a hacking campai… [+136111 chars]'
    },
    {
      'source': {
        'id': None,
        'name': 'Securityaffairs.com'
      },
      'author': 'Pierluigi Paganini',
      'title': 'Texas is the first state to ban DeepSeek on government devices',
      'description': 'Texas bans DeepSeek and RedNote on government devices to block Chinese data-harvesting AI, citing security risks. Texas Governor Greg Abbott banned Chinese AI company DeepSeek and Chinese-owned social media apps Xiaohongshu (RedNote) and Lemon8 from all state…',
      'url': 'https://securityaffairs.com/173764/laws-and-regulations/texas-bans-deepseek-and-rednote-govt-devices.html',
      'urlToImage': 'https://securityaffairs.com/wp-content/uploads/2025/01/image-44.png',
      'publishedAt': '2025-02-03T07:23:14Z',
      'content': 'Texas is the first state to ban DeepSeek on government devices\r\n\xa0|\xa0Law enforcement seized the domains of HeartSender cybercrime marketplaces\r\n\xa0|\xa0Security Affairs newsletter Round 509 by Pierluigi Pag… [+136178 chars]'
    },
    {
      'source': {
        'id': None,
        'name': 'Securityaffairs.com'
      },
      'author': 'Pierluigi Paganini',
      'title': 'Elon Musk ’s DOGE team granted ‘full access’ to sensitive Treasury systems. What are the risks?',
      'description': 'US Sen. Ron Wyden warns of national security risks after Elon Musk ’s DOGE was given full access to sensitive Treasury systems. Sen. Ron Wyden warned of national security risks after Elon Musk ’s team, Department of Government Efficiency (DOGE), was granted f…',
      'url': 'https://securityaffairs.com/173776/security/elon-musk-s-doge-granted-full-access-to-sensitive-treasury-systems.html',
      'urlToImage': 'https://securityaffairs.com/wp-content/uploads/2024/08/Elon-Musk.jpeg',
      'publishedAt': '2025-02-03T11:06:55Z',
      'content': 'Elon Musk s DOGE team granted full access to sensitive Treasury systems. What are the risks?\r\n\xa0|\xa0Texas is the first state to ban DeepSeek on government devices\r\n\xa0|\xa0Law enforcement seized the domains … [+136275 chars]'
    },
    {
      'source': {
        'id': 'the-times-of-india',
        'name': 'The Times of India'
      },
      'author': 'ETMarkets.com',
      'title': 'Dollar and oil Surge, Asian stocks fall on Trump tariffs',
      'description': 'The yields on US Treasuries gained while stock futures slumped, and an index of Asia-Pacific shares also dropped in response to the punitive measures taken against some of America’s biggest trading partners. The Canadian dollar sank to its weakest since 2003,…',
      'url': 'https://economictimes.indiatimes.com/markets/stocks/news/dollar-and-oil-surge-asian-stocks-fall-on-trump-tariffs/articleshow/117871786.cms',
      'urlToImage': 'https://img.etimg.com/thumb/msid-117871776,width-1200,height-630,imgsize-252278,overlay-etmarkets/articleshow.jpg',
      'publishedAt': '2025-02-03T01:05:21Z',
      'content': 'The dollar surged, oil jumped and equity markets turned red after US President Donald Trump made good on his threat to impose tariffs on the exports of Canada, Mexico and China. The yields on US Trea… [+2357 chars]'
    }
  ]
}

#STOCK INFO
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_APP_ID = "YQ0U7SQ3T8EOUHAK"
STOCK_API= "https://www.alphavantage.co/query?"
INTERVAL = "60min"
STOCK_PARAMS= {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": STOCK_APP_ID,
}

#NEWS INFO
NEWS_APP_ID = "9e3ad09305794ba7a825d63aacd84a3c"
NEWS_API = "https://newsapi.org/v2/everything?"
yesterday = datetime.now() - timedelta(days=1)
NEWS_PARAMS= {
    "q" : COMPANY_NAME,
    "from" : yesterday.strftime('%Y-%m-%d'),
    "sortBy" : "popularity",
    "apikey": NEWS_APP_ID,
}

def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
def get_percentage():
    # stock_data_raw = requests.get(url=STOCK_API,params= STOCK_PARAMS)
    # stock_data_raw.raise_for_status()
    # stock_data_json = stock_data_raw.json()
    sorted_data = sorted(FAKESTOCKDATA["Time Series (Daily)"].keys(), reverse=True)
    close_today = FAKESTOCKDATA["Time Series (Daily)"][sorted_data[0]]['4. close']
    close_yesterday = FAKESTOCKDATA["Time Series (Daily)"][sorted_data[1]]['4. close']
    return (float(close_today) / float(close_yesterday)) * 100
def change_perc():
    percentage = get_percentage()
    percentage -= 100
    return int(percentage)
def get_news():
    # news_data_raw = requests.get(url=NEWS_API,params= NEWS_PARAMS)
    # news_data_raw.raise_for_status()
    # news_data_json = news_data_raw.json()
    top3list = []
    for article in FAKENEWSDATA["articles"]:
        if is_english(article["description"]):
            top3list.append(article)
    return top3list
def percent_string(percentage):
    if percentage > 0:
        return f"🔺{percentage}%"
    else:
        return f"🔻{percentage}%"
def refactor_news(toplist,percentage):
    refact_top_3 = []
    for article in toplist:
        refact_top_3.append(f"{STOCK}: {percentage}\n Headline: {article["title"]}\n Brief: {article["description"]}")
    return refact_top_3
def send_msg(msglist):
    for msg in msglist:
        message = client.messages.create(
            from_=from_number,
            body= msg,
            to=to_number
        )
        print(message.sid)




perc = change_perc()
if abs(perc) > 5:
    new_list = get_news()
    message = refactor_news(new_list,percent_string(perc))
    send_msg(message)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this:


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

