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
                   "start_loc": {"lat": 37.601092, "lng": -122.386551},
                   "end_loc": { "lat": 37.574373, "lng": -122.334168}
                 }
                ]
  },
  {"first_name": "wendy",
   "last_name": "mol",
   "email": "wen@example.com",
   "bikeways": [
                 { "name": "san mateo library to burlingame library",
                   "start_loc": {"lat": 37.564988, "lng": -122.326465},
                   "end_loc": { "lat": 37.579509, "lng": -122.349226},
                 },
                 { "name": "burliname library rwc library",
                   "start_loc": {"lat": 37.579509, "lng": -122.349226},
                   "end_loc": {"lat": 37.484364, "lng": -122.227500}
                 }
               ]
  },
  {"first_name": "diana",
   "last_name": "mol",
   "email": "dian@example.com",
   "bikeways": [
                 { "name": "bart to autodesk sf",
                   "start_loc": {"lat": 37.600467, "lng": -122.386729},
                   "end_loc": {"lat": 37.601092, "lng": -122.386551},
                 },
                 { "name": "work to home",
                   "start_loc": {"lat": 37.600467, "lng": -122.386729},
                   "end_loc": {"lat": 37.579509, "lng": -122.349226}
                 }
               ]
  },
  {"first_name": "ben",
   "last_name": "pap",
   "email": "ben@example.com",
   "bikeways": [
                 { "name": "library to airport",
                   "start_loc": {"lat": 37.484364, "lng": -122.227500},
                   "end_loc": {"lat": 37.621593, "lng": -122.378966},
                 },
                 { "name": "airport to library",
                   "start_loc": {"lat": 37.621593, "lng": -122.378966},
                   "end_loc": {"lat": 37.579509, "lng": -122.349226}
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
Millbrae bart
Millbrae
California 94030
"lat": 37.600467, "lng": -122.386729

522 N San Mateo Dr
San Mateo, CA 94401
"lat": 37.574373, "lng": -122.334168

San Mateo Public Library Downtown
San Mateo, CA
"lat": 37.564988, "lng": -122.326465

824 Cowan Rd
Burlingame, CA 94010
"lat": 37.602910, "lng": -122.374729

Burlingame Public Library 480 Primrose Rd
Burlingame, CA 94010
"lat": 37.579509, "lng": -122.349226

101 San Francisco International Airport Tram
San Francisco, CA 94128
"lat": 37.621593, "lng": -122.378966

redwood city public library Centennial
Redwood City, CA
"lat": 37.484364, "lng": -122.227500

Autodesk sf
San Francisco
California 94105
"lat": 37.794059, "lng":-122.394805
'''
