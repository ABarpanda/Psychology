from datetime import date

class Main:
    def __init__(self,req_date:str):
        self.date_zero = date.fromisoformat('1900-01-01')
        
        self.target_date = date.fromisoformat(req_date)
        self.target_year = self.target_date.year
        self.target_month = self.target_date.month
        self.target_day = self.target_date.day

        self.diff = self.target_date - self.date_zero
        self.starttime = self.diff.days + 2
        
        self.url = f"https://timesofindia.indiatimes.com/{self.target_year}/{self.target_month}/{self.target_day}/archivelist/year-{self.target_year},month-{self.target_month},starttime-{self.starttime}.cms"
        
    
    def test_Main(self):
        print("Date zero:", self.date_zero)
        print("Start time:", self.starttime)
        print("URL:", self.url)

    def get_url(self):
        return self.url

if __name__ == "__main__":
    main_instance = Main("2024-06-13")
    generated_url = main_instance.get_url()
    Main("2024-06-13").test_Main()