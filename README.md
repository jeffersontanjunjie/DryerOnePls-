NUS Orbital 2025 - Milestone 1

**Proposed Level of Achievement:** Apollo 11

---

### Motivation:
Students in Temasek Hall (or any hall for that matter) often face uncertainty when using shared laundry dryers. It is unclear whether a dryer is available, how long until the dryer is available, or who is next in the queue. This often results in wasted time and effort.

---

### Aim:
To streamline the process of accessing dryers by providing a Telegram bot that allows users to check dryer status and join a queue. 

---

### User Stories:
1. As a student who wants to use a dryer, I want to check whether a dryer is available so that I don’t waste time checking in person.
2. As a student who finds it confusing to coordinate turns, I want to join a digital queue to make the system more efficient and easy for me to plan my schedule.

---

### Scope of Project:
This project is a Telegram bot that allows users to:
- Join the queue for either Dryer 1 or Dryer 2
- Check the current status of both dryers
- View their own position in the queue

---

### Features to be completed by the end of May:
1. **Queueing system**  
   a. Users can join the queue for Dryer 1 or 2  
   b. Users can check the queue status

2. **Database backend**  
   a. SQLite database using SQLAlchemy stores queue state

---

### Features to be completed by mid-July:
1. **Drying cycle management**  
   a. Users can start their cycle and receive reminders

2. **Chat system**  
   a. Users in the same queue can send public/private messages

3. **Notifications**  
   a. Users get notified when their turn is up

---

### Tech Stack:
- **Python 3**
- **Telegram Bot API (python-telegram-bot v20.7)**
- **SQLAlchemy + SQLite**
- **dotenv for token management**

---

### How are we different from similar platforms?
This bot is designed for specialized usage in NUS halls, unlike commercial laundromat apps. It also uses Telegram — a platform students already use daily — and supports minimal, chat-based interaction.

---

### Development Plan


#### **Milestone 1**
- Implemented basic functions:  
  - `/start`, `/join`, `/status`  
- Prepare README, poster, and demo video  

---

#### **Milestone 2**
- Implement core prototype features:  
  - `/start_drying` command with timer  
  - Drying cycle management (30 min default)  
  - Timed notifications (10 min left, 5 min left, finished)  
  - `/time` to check remaining drying time  
  - `/leave` to leave one or all queues  
- Perform system testing (single-user and multi-user scenarios)  

---

#### **Milestone 3**
- Add advanced features:  
  - `/chat` for public messages with others in the same dryer queue  
  - `/message` to privately message next user  
  - Live user notifications   
 - Conduct system and user testing 
