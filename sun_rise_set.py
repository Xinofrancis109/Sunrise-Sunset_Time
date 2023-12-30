import smtplib
import requests


LNG = 5.823310  # My location in Longitude
LAT = 5.578320  # My location in Latitude
params = {
    "lat": LNG,
    "lng": LAT,
    "formatted": 0,
    "tzid": "Africa/Lagos"  # time set to Lagos time but API uses UTC time
}
try:
    res1 = requests.get("https://api.sunrise-sunset.org/json", params=params)
    res1.raise_for_status()
    data1 = res1.json()

    res2 = requests.get("https://api.kanye.rest")
    res2.raise_for_status()
    data2 = res2.json()

    # slicing to get the required time from the output
    sunrise = data1["results"]["sunrise"].split("T")[1][:5]
    sunset = data1["results"]["sunset"].split("T")[1][:5]

    # connecting to gmail server and sending the message to email
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(user="waltxwill@gmail.com", password="operiukrkacnadpx")  # dummy email
        connect.sendmail(from_addr="waltxwill@gmail.com",
                         to_addrs="xinofranas109@gmail.com",  # replace with recipients email
                         msg=f"Subject: It's a new day\n\nGood Morning! How was your night?\nTake note that "
                             f"Sunrise is at: {sunrise}\nSunset is at: {sunset}\n"
                             f"Kanye quote of the day: '{data2['quote']}'\n"
                             f"Have a nice day pal😏❤"
                         )

except Exception as e:
    print(f'{e} occurred')
