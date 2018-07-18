## _howto_pay_college_fee
* howto_pay_college_fee
    - action_answer

## _ask_weather_location
* ask_weather_location{"location": "Toronto"}
    - slot{"location": "Toronto"}
    - action_weather
    - slot{"location": "Toronto"}

## _howto_print
* howto_print{"location": "Toronto"}
    - slot{"location": "Toronto"}
    - utter_howto_print

## _greet
* greet
    - utter_greet

## _goodbye
* goodbye
    - utter_goodbye
    - export
    - action_restart

## _are_you_bot
* are_you_bot
    - utter_are_you_bot

## _are_you_ready
* are_you_ready
    - utter_are_you_ready

## _are_you_real
* are_you_real
    - utter_are_you_real

## _are_you_there
* are_you_there
    - utter_are_you_there

## _hug_me
* hug_me
    - utter_hug_me

## _you_are_funny
* you_are_funny
    - utter_you_are_funny

## _utter_ask_program
* I want to check my schedule
    - utter_ask_program
* inform_program[program=QEMT]
    - slot{"program":"QEMT"}
    - utter_inform_schedule

## check_program_schedule
* check_program_schedule[program=QEMT]
    - slot{"program": "QEMT"}
    - utter_inform_schedule

## _inform_program
* ask_schedule
    - utter_ask_program
* inform_program[program=MADT]
    - slot{"program":"MADT"}
    - utter_inform_schedule

## _inform_name
* inform_name[username=Bupandir]
    - slot{"username":"Bupandir"}

## _inform_name
* inform_name[username=Manjot]
    - slot{"username":"Manjot"}

## _inform_name
* inform_name[username=Sai Ram Charam]
    - slot{"username":"Sai Ram Charam"}

## _inform_name
* inform_name[username=Siddartha]
    - slot{"username":"Siddartha"}

## _inform_name
* inform_name[username=Leo]
    - slot{"username":"Leo"}

## _inform_program
* inform_program[program=MADT]
    - slot{"program":"MADT"}

## _inform_program
* inform_program[program=CCBT]
    - slot{"program":"CCBT"}

## _inform_program
* inform_program[program=CSAT]
    - slot{"program":"CSAT"}

## _inform_program
* inform_program[program=LAQT]
    - slot{"program":"LAQT"}

## _inform_program
* inform_program[program=PMLT]
    - slot{"program":"PMLT"}

## _inform_program
* inform_program[program=CPMT]
    - slot{"program":"CPMT"}

## _inform_program
* inform_program[program=EMBT]
    - slot{"program":"EMBT"}

## _inform_program
* inform_program[program=FPWT]
    - slot{"program":"FPWT"}

## _inform_program
* inform_program[program=MMDT]
    - slot{"program":"MMDT"}

## _inform_program
* inform_program[program=OHST]
    - slot{"program":"OHST"}

## _inform_program
* inform_program[program=SCMT]
    - slot{"program":"SCMT"}

## _ask_weather_location
* ask_weather_location[location=Barcelona]
    - slot{"location":"Barcelona"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Toronto]
    - slot{"location":"Toronto"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Mississauga]
    - slot{"location":"Mississauga"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=London]
    - slot{"location":"London"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=New York]
    - slot{"location":"New York"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Brampton]
    - slot{"location":"Brampton"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Ottawa]
    - slot{"location":"Ottawa"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Sao Paulo]
    - slot{"location":"Sao Paulo"}
    - action_weather
    - export

## _ask_weather_location
* ask_weather_location[location=Mumbai]
    - slot{"location":"Mumbai"}
    - action_weather
    - export
