# PublicOutreachApplication

# 🛠️ IT Helpdesk Automator: The Triage Bot

**Built for the Public Outreach Internal IT Team**

Triaging helpdesk tickets manually when half your team is working remote? It's kind of a nightmare. 

When a fundraiser is locked out of their workspace five minutes before a shift, they don't have time to wait for someone to read an email, assign a category, and route it to the right person. Every minute counts. Since I'm currently on the fundraising floor myself, I know firsthand what that panic feels like and why fixing it fast is so crucial for hitting campaign targets.

I threw this quick Python project together to show how we can automate the boring stuff. 

What this actually does:
It's a lightweight script that scans incoming, messy support requests and instantly figures out what to do with them. 
- Flags whether the user is crying over a Windows, Mac, iOS, Android, or Chromebook issue.
- Uses keyword mapping to figure out if it's a busted VPN, a locked account, or a hardware crash.
- If someone drops words like "ASAP", "locked out", or "5 mins"—it bumps the ticket to HIGH priority so it doesn't get buried in the queue.

### Running it
No massive frameworks or weird dependencies to install. It’s just pure, out-of-the-box Python. 

Clone the repo, open your terminal, and run:
```bash
python ticket_parser.py
