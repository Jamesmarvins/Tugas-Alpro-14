import re
from datetime import datetime

def find_and_convert_dates(text):
    date_pattern = r'\b(\d{4})-(\d{2})-(\d{2})\b'
    dates = re.findall(date_pattern, text)
    today = datetime.now()
    results = []
    
    for date in dates:
        original_date_str = f"{date[0]}-{date[1]}-{date[2]}"
        date_obj = datetime.strptime(original_date_str, '%Y-%m-%d')
        converted_date_str = date_obj.strftime('%d-%m-%Y')
        
        days_difference = (today - date_obj).days
        
        result = f"{original_date_str} 00:00:00 selisih {days_difference} hari"
        results.append(result)
    
    return results

text = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

results = find_and_convert_dates(text)
for res in results:
    print(res)