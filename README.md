# WhatsAppWeb-MsgSender

Set of simple python scripts to send messages in WhatsApp Web

# Scripts

1. whatsapp.py - Python script to send a whatsapp message to a particular person
2. whatsapp2.py - Python script to send a whatsapp message to a particular group
3. whatsapp3.py - Python script to send whatsapp message to a particular person according to the count given by the user

## Libraries used

- `pywhatkit`
- `PyAutoGUI`

## Run Locally

You will need to install Python on  you system. Head over to https://www.python.org/downloads/ to download python.
(Dont Forget to Tick Add to Path while installing Python)

Once you have downloaded Python on your system, 
run the following command inside your terminal

```bash
  git clone https://github.com/milan-sony/WhatsAppWeb-MsgSender.git
```

Then go to the project folder

```bash
  cd WhatsAppWeb-MsgSender
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy Unrestricted
```

Install the dependencies needed for this project

```bash
  pip install -r requirement.txt
```

Now run the script you want 

```bash
  python whatsapp.py
```

or

```bash
  python whatsapp2.py
```

or

```bash
  python whatsapp3.py
```
