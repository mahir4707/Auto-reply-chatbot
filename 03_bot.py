import pyautogui
import pyperclip
import time
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("")
)

# Safety delay so you can switch to the target window
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(1269, 1055)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(707, 205)
pyautogui.dragTo(1183, 927, duration=1, button='left')


# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click()

# Step 4: Get text from clipboard into variable
chat_history = pyperclip.paste()

# Debug output
print("Copied Text:")
print(chat_history)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a person named mahir who speaks gujarati as well as english. You are from India and you are a coder. You analyze chat history and respond like Mahir. output should be the next chat response as mahir"
        },
        {
            "role": "user",
            "content": chat_history 
        }
    ]
)
response = completion.choices[0].message.content
pyperclip.copy(response)

# ------------------ STEP 5: Click at paste location ------------------
pyautogui.click(1184, 974)
time.sleep(1)

# ------------------ STEP 6: Paste the response ------------------
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# ------------------ STEP 7: Press Enter ------------------
pyautogui.press('enter')


