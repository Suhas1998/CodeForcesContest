import sublime
import os
import requests
import sys
from . import crawler
# Codeforces requests

def get_problems_list(contest_id, problems=''):
  url = "https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=1".format(
         contest_id = contest_id
  )

  contest_obj = requests.get(url)
  if contest_obj.json()['status'] == "OK" :
    problems_list = (contest_obj.json())['result']['problems']

    if problems == '':
      return problems_list
    else:
      for i in problems_list:
        if i['index'] == problems:
          return i
  else:
    print("Dude seems like it doesnt exist")
    sys.exit(1)

def correct_path(path):
  if os.path.isdir(path):
    print("\nIt is a directory")
  elif os.path.isfile(path):
    branch, leaf = os.path.split(path)
    print("That was a file " + branch)
    path = branch
  else:
    path = os.path.expanduser("~/Desktop")
    print("It is a special file (socket, FIFO, device file). Folder has been created on desktop" )
  return path


def fill_data(file, data):
  inputs = ""
  for inp in data:
    inputs = inputs + "\n" + inp
  file.write(inputs)
  # print(data)


def make_files(problems, path):
  for problem in problems:
    data = crawler.getproblem(problem['contestId'], problem['index'])
    input_path = path + "/" + problem['index'] + "_input.txt"
    cpp_path = path + "/" + problem['index'] + ".cpp"
    inp_file = open(input_path, 'w')
    cpp_file = open(cpp_path, 'w')
    fill_data(inp_file, data['input'] )
    # print(data)
    inp_file.close()
    cpp_file.close()

  output_path = path + "/" + "output.txt"
  os.mknod(output_path)
# Each problem Item

class ProblemItem:
  def __init__(self, problem_details):
    self._contest_id = problem_details["contestId"]
    self._problem_id = problem_details["index"]
    self._name = problem_details["name"]

# Each Contest Item

class ContestItem:
  def __init__(self, path, contest_id):
    self._path = correct_path(path)
    self._contest_id = contest_id[0]
    if len(contest_id) > 1:
      self._problems = get_problems_list(contest_id[0], contest_id[1])
    else:
      self._problems = get_problems_list(contest_id[0])


  def get_path(self):
    return self._path

  def get_contest_id(self):
    return self._contest_id

  def update_path(self, new_path):
    self._path = correct_path(new_path)

  def get_final_path(self, file_name ):
    return (str(self._path) + "/" + str(file_name))

  def make_folder(self):
    folder_path = self.get_final_path(self._contest_id)
    try:
        os.mkdir(folder_path)
        print("Done Bro")
    except FileExistsError:
        # directory already exists
        print("Couldnt create")
        pass
    make_files(self._problems, folder_path)
    print("Made the files")






