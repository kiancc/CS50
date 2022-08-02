-- Keep a log of any SQL queries you execute as you solve the mystery.

-- querying all columns in crime_scene_reports table --
SELECT * FROM crime_scene_reports;

-- querying street columns in crime_scene_reports table to find more info --
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street';
-- ID 295 Year 2021 Month 7 Day 28, theft occured at 10:15 am. Three Witnesses

-- querying interview table with date of theft to find more information on robbery
SELECT * FROM interviews
WHERE year = 2021
  AND month = 7
  AND day = 28;
-- Ruth: Sometime within 10 minutes of theft saw thief get into car in bakery parking lot and drive away. Check security logs around that time
-- Eugene: Someone he recognised. Saw the theif earlier that morning withdrawing money from ATM on Leggett Street
-- Raymond: As thief left bakery they called someone who talked to them for less than a minute. Thief said they were planning to take earliest flight out of fiftyville tomorrow.
-- Thief asked person to purchase ticket.
-- Emma: Bakery owner. Says someone came in suspiciously whispering into phone for half an hour and didn't buy anything.

-- querying bakery_security_logs to see if I can identify any details of the getaway car
SELECT * FROM bakery_security_logs
WHERE year = 2021
  AND month = 7
  AND day = 28 AND hour = 10
  AND minute BETWEEN 15 AND 25;
-- license plates: 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- querying atm_transactions to see if I can find any information on thief's withdrawal
SELECT * FROM atm_transactions
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND atm_location = 'Leggett Street';
-- account numbers: 28500762, 28296815, 76054385, 49610011, 16153065, 86363979 (deposit), 25506511, 81061156, 26013199

-- querying phone calls on the day of robbery to see if I can find any information regarding the phone call
SELECT * FROM phone_calls
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND duration < 60;
-- potential phone numbers: (130) 555-0289, (499) 555-9472, (367) 555-5533, (499) 555-9472, (286) 555-6063, (770) 555-1861, (031) 555-6622, (826) 555-1652, (338) 555-6650

-- querying to find list of potential suspects based on bank account, phone number and license plates
SELECT * FROM people
INNER JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE account_number
  IN(28500762, 28296815, 76054385, 49610011, 16153065, 86363979, 25506511, 81061156, 26013199)
  AND phone_number
  IN('(130) 555-0289', '(499) 555-9472', '(367) 555-5533', '(499) 555-9472', '(286) 555-6063', '(770) 555-1861', '(031) 555-6622', '(826) 555-1652', '(338) 555-6650')
  AND license_plate
  IN('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55');
-- potential suspects: Bruce ((367) 555-5533, 5773159633), Diana ((770) 555-1861, 3592750733)

-- querying airports to find information on Fiftyville airport
SELECT * FROM airports;
-- ID: 8, abbreviation = CSF

-- querying all flights from Fiftyville on the day after the robbery to find first flight out
SELECT * FROM flights
WHERE year = 2021
  AND month = 7
  AND day = 29
  AND origin_airport_id = 8
ORDER BY hour;
-- first flight out is 8:20 going to LaGuardia Airport, New York City (ID: 4)

-- finding person that took the first flight to New York City based on passport number
SELECT passport_number FROM flights
INNER JOIN airports ON airports.id = flights.destination_airport_id
INNER JOIN passengers on flights.id = flight_id
WHERE city = 'New York City'
  AND year = 2021
  AND month = 7
  AND day = 29
  AND passport_number IN(5773159633, 3592750733);
-- this returns one row which is Bruce. Bruce is the thief

-- querying phone_calls table to find receiver of phone call bruce made on the day of the robery that lasted less then a minute
SELECT receiver FROM phone_calls
WHERE caller = '(367) 555-5533'
  AND year = 2021
  AND month = 7
  AND day = 28
  AND duration < 60;
-- This returns (375) 555-8161

-- Finding name of accomplice
SELECT * FROM people
WHERE phone_number = '(375) 555-8161';
