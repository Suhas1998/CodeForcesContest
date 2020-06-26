import sublime
import sublime_plugin

import os
from os import listdir
from os.path import dirname

from .codeforcesAPI import ContestItem

def Window(window=None):
    return window if window else sublime.active_window()


class CreateContestCommand(sublime_plugin.WindowCommand):
  contest_id = ''
  problem_id = ''

  def run(self, paths=[], name=""):
    import functools
    Window().run_command("hide_panel")
    Window().show_input_panel(
        "(Make sure you are registered if this is a Live Contest) Enter the Problem/Contest Id:",
        name,
        functools.partial(self.on_done, paths),
        None,
        None,
    )

  def on_done(self, paths,name):
    self.contest_id = ''
    self.problem_id = ''

    name.replace(" ", "")
    for i in name:
      if i.isdigit() and len(self.problem_id) == 0:
        self.contest_id = self.contest_id + i
      elif  (i.isalpha() and len(self.contest_id) != 0) or len(self.problem_id) != 0:
        self.problem_id = self.problem_id + i

    if len(self.problem_id) == 0:
      self.create_structure(paths, self.contest_id, True)
    else:
      self.create_structure(paths, self.contest_id + self.problem_id, False)

  def create_structure(self, paths, name, is_contest):
    _path = paths[0]

    if os.path.isdir(_path):
      print("\nIt is a directory")
    elif os.path.isfile(_path):
      branch, leaf = os.path.split(_path)
      print("That was a file " + branch)
      _path = branch
    else:
      print("It is a special file (socket, FIFO, device file)" )

    print("Final path: " + _path)

    try:
        os.mkdir(str(_path) + "/" + name)
        contest = ContestItem(str(_path) + "/" + name, name)
        print("Done Bro")
    except FileExistsError:
        # directory already exists
        print("Couldnt create")
        pass

    sublime.active_window().run_command("refresh_folder_list")



