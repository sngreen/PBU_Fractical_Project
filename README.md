# PBU Final (Practical) Project



#### Purpose

The implementation of the Practical Project for Python Bottom Up session series.

See description in `helper_data/Python_Bottom_Up_Practical_Project_Specification.pdf` for more detail.



#### Prerequisites

Even though the other choices were possible, for output formatting and file-type verification I did resort to using 3rd party libraries instead. See `settings/requirements.txt` file.

```bash
# if the pip config is not set already
pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"
pip config set global.retries 15
pip config set global.timeout 60

# set virtual env (Linux)
pip install virtualenv
virtualenv venv
. venv/bin/activate

# install required libraries
pip install pip --upgrade
pip install -r settings/requirements.txt
```



#### Project Directory Structure

Self-intuitive, I hope, structure.

```bash
.
├── config
│   └── menu_file.yaml
├── data_ops
│   ├── csv_op.py
│   ├── json_op.py
│   └── txt_op.py
├── datetime_ops
│   └── datetime_op.py
├── format_ops
│   └── jinja_format.py
├── helper-data
│   ├── Python_Bottom_Up_Practical_Project_Specification.pdf
│   ├── user_0_root_elements.json
│   ├── user_6_root_elements.json
│   ├── users_0_columns_0_rows.csv
│   ├── users_0_words.txt
│   ├── users_27_words.txt
│   ├── users_5_columns_10_rows.csv
│   └── users_wront_format_words.json
├── main.py
├── README.md
├── settings
│   ├── .env
│   ├── requirements.txt
│   └── settings.py
└── templates
    └── template.j2
```



#### Running the script

As always, start with help (-h) option.

```bash
python3 main.py -h
usage: main.py [arg] | -h

options:
  -h, --help               show this help message and exit
  --file_name <file_name>  required: True, default: None
```



Generating report from a single file (examples)

```bash
# Ex.
python3 main.py --file_name helper-data/user_6_root_elements.json
python3 main.py --file_name helper-data/users_27_words.txt
python3 main.py --file_name helper-data/users_5_columns_10_rows.csv
```



Generating reports from all available in helper-data directory inputs

```bash
for fname in helper-data/*
do 
	echo "--> $fname <--"
	python3 main.py --file_name $fname
done
```



#### Note

- The project was written entirely in Linux, and I did not try to run it in either of the IDEs nor Git Bash. I think it should work regardless.

- I removed docstrings, as I think those are just polluting the code. It's quite obvious what the code is doing anyway.
