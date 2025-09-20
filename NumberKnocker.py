#!/usr/bin/env python3
"""
Welcome to Number Knocker.  A Phone Number Protection Tool.
This script helps mitigate and manage some aspects of phone number privacy protection.
"""
import requests  #Implementing the WWW into the program.
import json  
#(JaveScript Object Notation) Most Web APIs will return in JavaScript format.  
#JSON converts strings into Python Objects.  Theoretically, this program calls--
#--for JScript.  However, I do not know that language, yet.
import time
from typing import List, Dict #Specifies what type of Data is expected to be Returned.
import webbrowser #Opens URLs.

class PhonePrivacyTool:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.removal_sites = [
            {
                'name': 'National Do Not Call Registry',
                'url': 'https://www.donotcall.gov/',
                'automated': False,
                'description': 'Register to reduce telemarketing calls'
            },
            {
                'name': 'Whitepages',
                'url': 'https://www.whitepages.com/suppression_requests',
                'automated': False,
                'description': 'Request removal from Whitepages directory'
            },
            {
                'name': 'Spokeo',
                'url': 'https://www.spokeo.com/optout',
                'automated': False,
                'description': 'Opt out of Spokeo people search'
            },
            {
                'name': 'BeenVerified',
                'url': 'https://www.beenverified.com/app/optout/search',
                'automated': False,
                'description': 'Remove from BeenVerified database'
            },
            {
                'name': 'PeopleFinder',
                'url': 'https://www.peoplefinder.com/manage/',
                'automated': False,
                'description': 'Manage PeopleFinder listing'
            }
        ]
    
    def display_welcome(self):
        print("=" * 60)
        print("WELCOME TO NUMBER-KNOCKER")
        print("=" * 60)
        print(f"Enter phone number: {self.phone_number}")
        print("\nThis tool will assist you to:")
        print("✓ Register with Do Not Call registries")
        print("✓ Remove number from people search sites")
        print("✓ Set up call blocking on device")
        print("✓ Monitor for future appearances")
        print()
    
    def register_do_not_call(self):
        print("STEP 1: DO NOT CALL REGISTRIES")
        print("-" * 40)
        
        registries = [
            {
                'name': 'National Do Not Call Registry (US)',
                'url': 'https://www.donotcall.gov/',
                'phone': '1-888-382-1222'
            },
            {
                'name': 'Canadian Do Not Call List',
                'url': 'https://www.lnnte-dncl.gc.ca/en',
                'phone': '1-866-580-3625'
            }
        ]
        
        for registry in registries:
            print(f"\n• {registry['name']}")
            print(f"  Website: {registry['url']}")
            print(f"  Phone: {registry['phone']}")
            
        print("\nAction required: Visit these websites or call to register your number.")
        input("Press Enter when completed...")
    
    def remove_from_data_brokers(self):
        print("\nSTEP 2: DATA BROKER REMOVAL")
        print("-" * 40)
        print("Opening removal pages for major data brokers...")
        
        for site in self.removal_sites:
            print(f"\n• {site['name']}")
            print(f"  Description: {site['description']}")
            print(f"  URL: {site['url']}")
            
            choice = input("  Open Site? (y/n): ").lower()
            if choice == 'y':
                webbrowser.open(site['url'])
                time.sleep(2)  # Brief pause between openings
    
    def setup_call_blocking(self):
        print("\nSTEP 3: CALL BLOCKING SETUP")
        print("-" * 40)
        
        blocking_options = {
            'iOS': [
                'Settings > Phone > Silence Unknown Callers',
                'Settings > Phone > Blocked Contacts',
                'Download apps like RoboKiller, Hiya, or Truecaller'
            ],
            'Android': [
                'Phone app > Settings > Blocked numbers',
                'Enable Google spam protection',
                'Download apps like Truecaller, RoboKiller, or Call Control'
            ],
            'Landline': [
                'Contact your phone provider about call blocking services',
                'Consider devices like CPR V5000 Call Blocker',
                'Use *77 (varies by provider) to block anonymous calls'
            ]
        }
        
        print("Set up call blocking on devices:")
        for device, steps in blocking_options.items():
            print(f"\n{device}:")
            for step in steps:
                print(f"  • {step}")
    
    def create_monitoring_checklist(self):
        print("\nSTEP 4: ONGOING MONITORING")
        print("-" * 40)
        
        checklist = [
            "Monthly Googles searchs for your Number",
            "Check major people search sites quarterly",
            "Be cautious with sharing your number online",
            "Use alternative numbers for online accounts, when possible",
            "Consider a Google Voice number for non-essential uses",
            "Report persistent spam to FTC (reportfraud.ftc.gov)"
        ]
        
        print("Monthly monitoring checklist:")
        for i, item in enumerate(checklist, 1):
            print(f"{i}. {item}")
        
        # Save checklist to file
        with open('phone_privacy_checklist.txt', 'w') as f:
            f.write("PHONE PRIVACY MONITORING CHECKLIST\n")
            f.write("="*40 + "\n\n")
            for i, item in enumerate(checklist, 1):
                f.write(f"{i}. {item}\n")
        
        print(f"\nChecklist saved to 'phone_privacy_checklist.txt'")
    
    def generate_removal_emails(self):
        print("\nSTEP 5: EMAIL TEMPLATES")
        print("-" * 40)
        
        email_template = f"""Subject: Request for Phone Number Removal

Dear Privacy Team,

I am requesting the immediate removal of my phone number from your database and any associated services.

Phone Number: {self.phone_number}

I do not consent to my phone number being:
- Listed in your directory
- Sold or shared with third parties
- Used for marketing purposes
- Displayed in search results

Please confirm in writing that my number has been removed from all your systems within 10 business days as required by applicable privacy laws.

Thank you for your prompt attention to this matter.

Best regards,
[Your Name]
[Date]
"""
        
        with open('removal_email_template.txt', 'w') as f:
            f.write(email_template)
        
        print("Template Created: 'removal_email_template.txt'")
        print("Send to data brokers that don't have online opt-out forms.")
    
    def run_full_process(self):
        self.display_welcome()
        
        try:
            self.register_do_not_call()
            self.remove_from_data_brokers()
            self.setup_call_blocking()
            self.create_monitoring_checklist()
            self.generate_removal_emails()
            
            print("\n" + "="*60)
            print("Number => Knocked")
            print("="*60)
            print("Remember:")
            print("• This process may take several weeks to show full effect")
            print("• Some sites require manual verification")
            print("• Regularly monitor and repeat removals as needed")
            print("• Consider using a secondary number for online accounts")
            
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user.")
        except Exception as e:
            print(f"\nError occurred: {e}")
        
def main():
    print("Phone Number Privacy Protection Tool")
    print("Note: This tool helps automate but does not directly")
    print("access or modify external databases due to security restrictions.\n")
    
    phone_number = input("Enter your phone number (for reference): ")
    
    if not phone_number:
        print("Phone number is required.")
        return
    
    tool = PhonePrivacyTool(phone_number)
    tool.run_full_process()


if __name__ == "__main__":
    main()

