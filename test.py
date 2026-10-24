from tools.tavily_tool import tavily_search
from backend import run_travel_agent
import airportsdata
import json

# res = tavily_search("Best hotels in India")
# print(res)


# res = airportsdata.load("IATA")
# print(json.dumps(res, indent=4))
# print(len(res))


# Sample Input : 
# Plan a complete 7 days India trip from Bangladesh including flights, Hotels and Sightseeing under 2 lakhs.

user_input = input("Enter travel request: ")
res = run_travel_agent(user_input=user_input, thread_id="test_user")
print(res["answer"])
