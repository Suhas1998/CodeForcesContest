import sublime
import os
import re

class ContestItem:
  def __init__(self, path, contest_id):
    self._path = path
    self._contest_id = contest_id

  def get_path(self):
    return self._path

  def get_contest_id(self):
    return self._contest_id

  def update_path(self, new_path):
    self._path = new_path
