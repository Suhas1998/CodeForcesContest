import sublime, sublime_plugin
import os
from os import listdir
from os.path import dirname

def getNumber(input_string):
  pos = 0
  number_string = ""
  for i in input_string:
    if i.isdigit():
      number_string = number_string + i

  return number_string

class SampleCommand(sublime_plugin.TextCommand):
  def run(self, edit, action=None):
    if action == None:
      def on_done(input_string):
        # self.view.run_command("move_to", {"to": "bof"})
        # self.view.run_command("insert", {"characters": input_string})
        contestId = int(getNumber(input_string))
        print(contestId+1)

      def on_change(input_string):
        pass

      def on_cancel():
        print("User cancelled the input")

      window = self.view.window()
      window.show_input_panel("Text to Insert:", "(Make Sure You Registered For The Contest) Enter Contest Id : ",on_done, on_change, on_cancel)
      print("This Works")

