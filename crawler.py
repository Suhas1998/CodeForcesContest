import requests
import re

def getproblem(contest_id, problem_id):
  url = "https://codeforces.com/contest/{contest_id}/problem/{problem_id}"
  response = requests.get(url.format(contest_id= contest_id, problem_id = problem_id))
  # print(response.content)

  inp_pat = re.compile('<div class="input"><div class="title">Input</div><pre>([^<]+)</pre>')
  otp_pat = re.compile('<div class="output"><div class="title">Output</div><pre>([^<]+)</pre>')

  input_cases = [ inp.strip() for inp in re.findall(inp_pat, response.text)]

  output_cases = [ otp.strip() for otp in re.findall(otp_pat, response.text)]

  data = {'input' : input_cases, 'output' : output_cases}


  return data

# d = getproblem('1427','C')

# for i in range(len(d['input'])):
#   print('Input:\n', d['input'][i])
#   print('Output:\n', d['output'][i])
