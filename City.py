import sqlite3


class City:
    def __init__(self, city_names):
        self.city_names = city_names

    def add_city(self):
        conn = sqlite3.connect("User.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS city (
            city_id TEXT PRIMARY KEY DEFAULT (hex(randomblob(16))),
            city_name TEXT NOT NULL
        );
        """)
        for city_name in self.city_names:
            try:
                cursor.execute("INSERT INTO city (city_name) VALUES (?);", (city_name,))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Could not insert {city_name}: {e}")
        conn.close()

city_names = [
    "Ahmedabad", "Aligarh", "Ambala", "Amravati", "Amritsar", "Anand", "Bangalore", "Bareilly",
    "Bhopal", "Bhubaneswar", "Bikaner", "Bilaspur", "Chandigarh", "Chennai", "Coimbatore",
    "Dehradun", "Delhi", "Dhanbad", "Dharamsala", "Durg", "Faridabad", "Gandhinagar", "Ghaziabad",
    "Gurgaon", "Guwahati", "Gwalior", "Haldwani", "Haridwar", "Hyderabad", "Indore", "Jabalpur",
    "Jaipur", "Jalandhar", "Jammu", "Jamshedpur", "Jodhpur", "Kanpur", "Kolhapur", "Kolkata", "Kota",
    "Lucknow", "Ludhiana", "Madurai", "Mangalore", "Meerut", "Mumbai", "Mysuru", "Nagpur", "Nashik",
    "Noida", "Patna", "Pune", "Raipur", "Rajkot", "Ranchi", "Rishikesh", "Surat", "Thane", "Udaipur",
    "Vadodara", "Varanasi", "Vijayawada", "Visakhapatnam", "Warangal", "Agra", "Aurangabad", "Bhopal",
    "Bhubaneswar", "Chidambaram", "Dibrugarh", "Erode", "Gandhinagar", "Guntur", "Hoshiarpur", "Howrah",
    "Imphal", "Jalandhar", "Jind", "Jodhpur", "Kakinada", "Kannur", "Kochi", "Kota", "Kottayam",
    "Krishnanagar", "Latur", "Madurai", "Malda", "Manipal", "Mathura", "Meerut", "Moga", "Moradabad",
    "Muzaffarnagar", "Nanded", "Nainital", "Palakkad", "Panaji", "Patiala", "Pudukottai", "Rajahmundry",
    "Raipur", "Ranchi", "Shimla", "Siliguri", "Surat", "Thiruvananthapuram", "Udupi", "Vadodara",
    "Vellore", "Visakhapatnam", "Warangal", "Durgapur", "Gaya", "Kanpur", "Kollam", "Mangalore",
    "Moradabad", "Nadiad", "Namakkal", "Nellore", "Palakkad", "Patan", "Ratlam", "Rourkela", "Salem",
    "Sikar", "Solapur", "Sonipat", "Surat", "Thane", "Tumkur", "Udaipur", "Vadodara", "Varanasi",
    "Vellore", "Visakhapatnam", "Yavatmal",
]

a = City(city_names)
a.add_city()
