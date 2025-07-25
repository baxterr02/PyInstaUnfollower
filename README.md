# PyInstaUnfollower
Mass Instagram Unfollower Automation Script

---

````markdown
# InstaUnfollowerBot

> A lightweight Instagram automation script that unfollows accounts from your following list using Python and Selenium.

---

## 📌 Features

- Automatically logs into Instagram
- Opens your profile and loads the "Following" list
- Unfollows up to a specified number of accounts per session
- Safe daily limit (e.g. 100/day, under Instagram's unfollow/day cap)
- Works on Firefox (can be adapted for Chrome)

---

## ⚠️ Disclaimer

This script is intended for educational and personal use only.  
Automating actions on Instagram may violate their [Terms of Service](https://help.instagram.com/581066165581870).  
Use at your own risk. I am not responsible for any account issues caused by misuse.

---

## 🔧 Requirements

- Python 3.7+
- [geckodriver](https://github.com/mozilla/geckodriver) (for Firefox)
- A clean virtual environment (recommended)

Install dependencies:

```bash
sudo pacman -S geckodriver
````

---

## 🚀 Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/baxterr02/PyInstaUnfollower.git
   cd PyInstaUnfollower
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install selenium
   ```

3. Edit `script.py` and replace your Instagram credentials:

   ```python
   USERNAME = 'your_username'
   PASSWORD = 'your_password'
   UNFOLLOW_COUNT = 100  # recommended max per day
   ```

4. Run the script:

   ```bash
   python script.py
   ```

---

## 🖥️ Platform

Tested on:

* Arch Linux
* Firefox with `geckodriver`

You can modify the script to use Chrome by replacing:

```python
from selenium.webdriver.firefox.options import Options
driver = webdriver.Firefox(options=options)
```

with:

```python
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(options=options)
```

---

## ✅ To-Do / Ideas

* [ ] Add random delays to simulate human behavior
* [ ] Store and skip previously unfollowed users
* [ ] Add Chrome compatibility toggle
* [ ] GUI for easier use
* [ ] Upload unfollow logs to CSV

---

## 📂 License

MIT License

---

## 🙋‍♂️ Want to Contribute?

Feel free to fork, open issues, or improve the script! PRs welcome.

