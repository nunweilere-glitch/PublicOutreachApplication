import json

def grab_tickets(filepath):
    # just a helper to load the dummy data 
    # Will crash if the file is missing
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Yikes. Couldn't find {filepath}. Did you move it?")
        return []

def triage_issue(ticket):
    # Mash the subject and description together so we don't miss anything
    dump = (ticket.get('subject', '') + " " + ticket.get('description', '')).lower()
    
    # 1. Figure out what broke (using a dirty keyword match for now)
    cat = "General / Unsorted"
    if any(w in dump for w in ['mfa', 'locked', 'reset', 'password', 'authenticator']):
        cat = "Account Access & Security"
    elif any(w in dump for w in ['vpn', 'wi-fi', 'dropping', 'connection', 'internet']):
        cat = "Network/VPN"
    elif any(w in dump for w in ['install', 'app', 'software', 'admin']):
        cat = "Software Config"
    elif any(w in dump for w in ['freezes', 'brick', 'screen', 'restart']):
        cat = "Hardware/OS Crash"

    # 2. How mad is the user? (Priority level)
    urgency = "Low"
    if any(w in dump for w in ['asap', '5 mins', 'help!!', 'urgent', 'locked out']):
        urgency = "HIGH - Drop everything"
    elif any(w in dump for w in ['keeps dropping', 'freezing', 'stopped']):
        urgency = "Medium - Annoying but workable"
    
    # 3. Where should this go?
    route_to = "Tier 1 Helpdesk (Standard Queue)"
    if cat == "Account Access & Security":
         route_to = "Self-Service Portal -> Tier 1 Auth Reset"
    elif urgency == "HIGH - Drop everything" and "Network" in cat:
         route_to = "Escalate -> Tier 2 IT Specialist"

    return {
        "id": ticket['ticket_id'],
        "os": ticket['platform'],
        "category": cat,
        "priority": urgency,
        "action": route_to
    }

def main():
    print(">>> Firing up the IT Ticket Router...\n")
    
    tix = grab_tickets('sample_tickets.json')
    if not tix:
        return
        
    for t in tix:
        res = triage_issue(t)
        print(f"[{res['id']}] Device: {res['os']}")
        print(f" -> Issue Type: {res['category']}")
        print(f" -> Urgency:    {res['priority']}")
        print(f" -> Next Step:  {res['action']}\n")
        print("-" * 40)

if __name__ == "__main__":
    main()
