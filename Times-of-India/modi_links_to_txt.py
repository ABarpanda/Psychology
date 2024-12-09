import os
import json
from datetime import date, datetime
import individual_scraper

with open("Modi_links.json","r") as file:
    mydict = json.load(file)

# print(mydict)
demodict = {
        "2022-12-26" : ["http://timesofindia.indiatimes.com//india/follow-covid-protocol-as-cases-rising-in-many-nations-pm-modi/articleshow/96503095.cms", "http://timesofindia.indiatimes.com//india/un-applause-for-namami-gange-proof-of-indias-willpower-pm-modi/articleshow/96503255.cms"],
    "2022-12-27" : ["http://timesofindia.indiatimes.com//india/fabricated-narratives-overlooked-sacrifice-by-guru-gobinds-sons-pm-modi/articleshow/96527006.cms", "http://timesofindia.indiatimes.com//city/patna/bihar-cm-nitish-to-skip-pms-meet-on-ganga/articleshow/96527692.cms", "http://timesofindia.indiatimes.com//world/europe/over-call-with-ukraine-president-zelenskyy-pm-modi-urges-for-end-to-war/articleshow/96528356.cms"],
    "2022-12-28" : ["http://timesofindia.indiatimes.com//city/nagpur/cant-stand-insult-of-pm-modi-bjp-mlc-prasad-lad/articleshow/96552522.cms"],
    "2022-12-29" : ["http://timesofindia.indiatimes.com//india/pm-modi-visits-ailing-mother-in-ahmedabad-hospital/articleshow/96583122.cms"],
    "2022-12-30" : ["http://timesofindia.indiatimes.com//city/nagpur/if-rahul-violated-security-norms-113-times-pm-modi-too-has-done-the-same-patole/articleshow/96605974.cms", "http://timesofindia.indiatimes.com//india/buzz-that-pm-modi-may-rejig-team-after-january-14/articleshow/96608630.cms", "http://timesofindia.indiatimes.com//india/my-mother-is-simple-and-extraordinary/articleshow/96609184.cms", "http://timesofindia.indiatimes.com//india/pm-modis-mother-heeraben-passes-away-tributes-pour-in/articleshow/96609747.cms", "http://timesofindia.indiatimes.com//india/pm-modi-may-join-development-works-in-west-bengal-via-video-conferencing/articleshow/96609772.cms"],
    "2022-12-31" : ["http://timesofindia.indiatimes.com//india/in-my-mothers-life-story-i-see-the-penance-sacrifice-and-contribution-of-indias-matrushakti-pm-modi/articleshow/96631105.cms", "http://timesofindia.indiatimes.com//india/soon-after-last-rites-of-mother-pm-modi-returns-to-work/articleshow/96632724.cms", "http://timesofindia.indiatimes.com//india/pm-modi-phones-speaks-to-pants-mother/articleshow/96633045.cms", "http://timesofindia.indiatimes.com//city/goa/cm-will-urge-modi-shah-torevoke-nod-to-kalasa-dpr/articleshow/96631093.cms"]
}

for key in mydict.keys():
    mytuple = date.fromisoformat(key).timetuple()
    print([mytuple[0],mytuple[1]])
    file_name = f"TOI_Modi_data_{mytuple[0]}_{mytuple[1]}.txt"

    folder_path = f"{mytuple[0]}"
    file_path = os.path.join(folder_path, file_name)

    os.makedirs(folder_path, exist_ok=True)

    with open(file_path, "a", encoding="utf-8") as file:
        for link in mydict[key]:
            data = individual_scraper.Main(link).return_text()
            # print(data)
            file.write(data[0]+"\n"+data[1]+'\n')
    # with open("TOI_Modi_data.txt", "a") as file:
    #         file.write(data+",\n")
