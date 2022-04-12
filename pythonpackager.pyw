# Copyright 2022 @Tyler887
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tkinter as tk
from tkinter import ttk
import os
import sys

file = ""

gui = tk.Tk()
gui.geometry("300x300")
gui.title("Python-Packager with Cython/GCC")
def select_file():
    filetypes = (
        ('Python script with console', '*.py'),
        ('Windowed Python script', '*.pyw')
    )

    filename = fd.askopenfilename(
        title='Select Script',
        filetypes=filetypes)
select = text=tk.Label(text=f"Selected File: {os.path.basename(file)}" if file != "" else "No File Selected"), ttk.Button(gui, text="...", command=select_file)
select.pack()

gui.mainloop()
