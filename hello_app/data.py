users = [
  {"first_name": "calvin",
   "last_name": "settachatgul",
   "email": "calvin@example.com",
   "bikeways": [
                 { "name": "home to work",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng": 456 },
                 },
                 { "name": "work to home",
                   "start_loc": { "lat": 123, "lng": 456},
                   "end_loc": { "lat": 123, "lng": 456}
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


