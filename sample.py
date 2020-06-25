import sublime, sublime_plugin
import os
from os import listdir
from os.path import dirname

class SampleCommand(sublime_plugin.TextCommand):
  def run(self, edit, action=None):
    def on_done(input_string):
      # self.view.run_command("move_to", {"to": "bof"})
      # self.view.run_command("insert", {"characters": input_string})
      print(input_string)

    def on_change(input_string):
      print("Input changed: %s" % input_string)

    def on_cancel():
      print("User cancelled the input")

    window = self.view.window()
    window.show_input_panel("Text to Insert:", "Hello, World!",on_done, on_change, on_cancel)
    print("This Works")

