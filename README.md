# 🤖 Auto Reply Chatbot (Desktop Automation + OpenAI)

> An automated desktop-based auto-reply chatbot that reads chat messages from the screen, generates replies using OpenAI, and sends them automatically.

This project is a **Python-based automation chatbot** that:
- Reads chat text directly from a chat window on your screen
- Uses OpenAI to generate a human-like reply
- Automatically pastes and sends the reply back

It combines **desktop automation + clipboard handling + AI-generated responses**, making it a practical example of real-world automation.

---

## 🚀 What This Project Does

This script acts as an **auto-reply assistant** for chat applications (such as WhatsApp Web, Telegram Web, or any desktop chat interface).

It works by:
1. Selecting chat text from the screen  
2. Copying it to the clipboard  
3. Sending it to OpenAI for response generation  
4. Automatically pasting and sending the AI-generated reply  

No direct integration with chat platforms is required — the automation works entirely through **screen interaction**.

---

## 🧠 How the Chatbot Works (Step-by-Step)

1. **Safety delay**  
   Provides time to switch to the target chat window before automation starts.

2. **Mouse automation**  
   - Clicks on the chat application  
   - Drags the mouse to select chat text  

3. **Clipboard handling**  
   - Copies selected chat content  
   - Stores it as `chat_history`

4. **AI response generation**  
   - Sends chat history to OpenAI  
   - Generates a reply using a defined personality and language style  

5. **Auto reply**  
   - Copies the AI response to the clipboard  
   - Pastes it into the chat input field  
   - Sends the message automatically  

This process closely mimics how a human reads and replies to messages — but in an automated way.

---

## 🛠 Technologies & Libraries Used

- **Python**
- **pyautogui** – mouse and keyboard automation  
- **pyperclip** – clipboard read/write operations  
- **time** – delays for safe execution  
- **openai** – AI-powered text generation  
- **os** – environment variable handling  

---

## 🧠 AI Behavior Customization

The chatbot’s behavior is controlled using a **system prompt**.

Current behavior:
- Responds as a person named **Mahir**
- Uses **Gujarati and English**
- Acts like a coder from India
- Generates replies based on chat context  

You can change personality, language, or tone by editing the system message.

---

## 📌 Requirements & Assumptions

- Python 3.x installed  
- OpenAI API key available as an environment variable  
- Chat application open and visible on screen  
- Screen resolution consistent with mouse coordinates  

---
## ▶️ How to Run the Project

1. Install the required dependencies:
   ```bash
   pip install pyautogui pyperclip openai
2. Set your OpenAI API key as an environment variable.
3. Open the chat application (WhatsApp Web, Telegram Web, or any chat UI) on your screen.
4. Ensure the chat window layout and screen resolution match the mouse coordinates used in the script.
5. Run the Python script:
    ```bash
    python 03_bot.py
6. Switch to the target chat window within the safety delay time.

The script will automatically select the chat text, generate a reply using OpenAI, and send the response.
---
## ⚠️ Important Notes

- Mouse coordinates are **system- and resolution-dependent**  
- You must adjust `pyautogui.click()` and `dragTo()` values for your screen  
- Do not move the mouse during execution  
- This approach uses UI automation, not official APIs  

---

## 🎯 Who Should Use This Project?

This project is ideal for:
- Python learners exploring automation  
- Developers combining AI with scripting  
- Students building unique portfolio projects  
- Anyone curious about auto-reply systems  

Basic Python knowledge is sufficient.

---

## 🌱 Learning Outcomes

After working with this project, you will:
- Understand desktop automation using Python  
- Learn clipboard-based data transfer techniques  
- Practice prompt engineering basics  
- Integrate OpenAI into automation workflows  
- Build real-world automation logic  

---

## 🚧 Limitations

- Relies on fixed screen coordinates  
- Requires the chat window layout to remain unchanged  
- Not suitable for background or headless execution  

These limitations are acceptable for learning and experimentation.

---

## 📌 Future Improvements

- Dynamic coordinate detection  
- Continuous message monitoring (loop-based logic)  
- Platform-specific integrations  
- Error handling and safety checks  
- GUI-based configuration  

---

## 📌 Final Note

This project is designed for **learning and experimentation**, not production use.  
It demonstrates how **AI + automation** can be combined using simple Python logic.

**Use responsibly and ethically.**

Happy Automating 🤖🚀
