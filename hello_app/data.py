users = [
  {"first_name": "calvin",
   "last_name": "settachatgul",
   "email": "calvin@example.com",
   "bikeways": [
                 { "name": "home to bart",
                   "start_loc": { "lat": 37.574373, "lng": -122.334168},
                   "end_loc": { "lat": 37.601092, "lng": -122.386551 },

                 },
                 { "name": "bart to home",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 37.574373, "lng": -122.334168}
                 }
                ]
  },
  {"first_name": "wendy",
   "last_name": "mol",
   "email": "wen@example.com",
   "bikeways": [
                 { "name": "home to work",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 },
                 },
                 { "name": "work to home",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 }
                 }
               ]
  },
  {"first_name": "diana",
   "last_name": "mol",
   "email": "dian@example.com",
   "bikeways": [
                 { "name": "home to work",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 },
                 },
                 { "name": "work to home",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 }
                 }
               ]
  },
  {"first_name": "ben",
   "last_name": "pap",
   "email": "ben@example.com",
   "bikeways": [
                 { "name": "home to work",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 },
                 },
                 { "name": "work to home",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng":456 }
                 }
               ]
  },
]

print (users[0]["first_name"])

for user in users:
  print(user["first_name"])
  print(user["last_name"])
  print(user["bikeways"][0])

'''
Millbrae
California 94030
37.601092, -122.386551

522 N San Mateo Dr
San Mateo, CA 94401
37.574373, -122.334168

San Mateo Public Library Downtown
San Mateo, CA
37.564988, -122.326465

824 Cowan Rd
Burlingame, CA 94010
37.602910, -122.374729

Burlingame Public Library 480 Primrose Rd
Burlingame, CA 94010
37.579509, -122.349226

101 San Francisco International Airport Tram
San Francisco, CA 94128
37.621593, -122.378966

101 San Francisco International Airport Tram
San Francisco, CA 94128
37.621593, -122.378966

101 San Francisco International Airport Tram
San Francisco, CA 94128
37.621593, -122.378966

'''
