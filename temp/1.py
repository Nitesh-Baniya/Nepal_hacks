import pandas as pd


def create_cybersecurity_csv():
    """Create a CSV file with cybersecurity concepts and explanations"""

    cybersecurity_data = [
        ["Phishing", "A social engineering attack where attackers send fraudulent messages to trick individuals into revealing sensitive information or installing malware. Common indicators include urgent language, suspicious links, and requests for personal information."],
        ["Ransomware", "A type of malicious software that encrypts a victim's files and demands payment for the decryption key. Ransomware often spreads through phishing emails, malicious downloads, or exploiting system vulnerabilities."],
        ["Two-Factor Authentication (2FA)", "A security method that requires users to provide two different authentication factors: something they know (password) and something they have (mobile device) or something they are (biometric). This significantly increases account security."],
        ["SQL Injection", "A code injection technique that exploits vulnerabilities in database-driven websites. Attackers insert malicious SQL statements into entry fields, allowing them to access, modify, or delete data from the database."],
        ["Zero-Day Vulnerability", "A software security flaw unknown to the vendor that hackers can exploit before a patch is created. These vulnerabilities are particularly dangerous as no defense exists at the time of discovery."],
        ["DDoS Attack", "Distributed Denial of Service attack overwhelms a target system with traffic from multiple compromised computers. This renders the target system unavailable to legitimate users and can cause significant service disruption."],
        ["Man-in-the-Middle Attack", "An attack where the attacker secretly intercepts and possibly alters communications between two parties who believe they're directly communicating with each other. It can be used to steal login credentials or personal information."],
        ["VPN", "Virtual Private Network creates an encrypted connection over a less secure network. VPNs provide privacy, anonymity, and security by creating a private network from a public internet connection."],
        ["Social Engineering", "Psychological manipulation techniques that trick people into making security mistakes or giving away sensitive information. Types include phishing, pretexting, baiting, and tailgating."],
        ["Firewall", "A network security device that monitors and filters incoming and outgoing network traffic based on an organization's security policies. Firewalls establish a barrier between trusted internal networks and untrusted external networks."],
        ["Encryption", "The process of encoding information so that only authorized parties can access it. Encryption uses mathematical algorithms to convert data into a coded format that appears random without the decryption key."],
        ["Malware", "Short for malicious software, it refers to any software designed to harm or exploit devices, services, or networks. Types include viruses, trojans, worms, ransomware, spyware, and adware."],
        ["Brute Force Attack", "A method of trial and error used to decode encrypted data such as passwords by systematically checking all possible combinations until the correct one is found. Protection includes complex passwords and account lockouts."],
        ["Penetration Testing", "An authorized simulated attack on a computer system to evaluate security. Penetration testers use the same tools and techniques as attackers to find and demonstrate business impacts of vulnerabilities."],
        ["Cross-Site Scripting (XSS)", "A web security vulnerability that allows attackers to inject client-side scripts into web pages viewed by other users. This can be used to bypass access controls and impersonate users."],
        ["Spyware", "Software that secretly gathers user information through their internet connection without their knowledge, usually for advertising purposes. It can track internet activity, harvest data, and monitor keystrokes."],
        ["Hashing", "The process of converting data of any size into a fixed-size string. Unlike encryption, hashing is one-way and cannot be reversed. It's commonly used to verify data integrity and store passwords securely."],
        ["Botnet", "A network of infected computers controlled remotely by attackers, often used for DDoS attacks or spam distribution. Users are typically unaware their computer is part of a botnet."],
        ["Cyber Threat Intelligence", "Evidence-based knowledge about existing or emerging threats that helps organizations make informed security decisions. It includes context, mechanisms, indicators, implications, and action-oriented advice."],
        ["CSRF Attack", "Cross-Site Request Forgery tricks users into submitting unwanted requests to websites where they're authenticated. This can force users to execute actions without their consent or knowledge."],
        ["Zero Trust Security", "A security model that requires strict identity verification for every person and device trying to access resources, regardless of whether they're inside or outside the network perimeter."],
        ["APT", "Advanced Persistent Threat is a prolonged, targeted cyber attack where an attacker establishes an undetected presence in a network to steal sensitive data. APTs are typically conducted by nation-states or state-sponsored groups."],
        ["Security Misconfigurations", "Improperly configured security settings that leave systems vulnerable. Common examples include default credentials, error messages revealing too much information, and unnecessary features enabled."],
        ["Privilege Escalation", "A type of attack that exploits bugs, design flaws, or configuration oversights to gain elevated access to resources that are normally protected. It allows attackers to gain higher-level permissions than intended."],
        ["DNS Spoofing", "A type of cyber attack where corrupted DNS data is introduced into a DNS resolver's cache, causing the resolver to return an incorrect IP address. This diverts traffic to the attacker's computer."],
        ["Supply Chain Attack", "A cyber attack that targets less-secure elements in the supply chain, such as third-party vendors or software. The SolarWinds attack of 2020 is a notable example that affected thousands of organizations."],
        ["Defense in Depth", "A cybersecurity approach that uses multiple layers of security controls throughout a system. If one defense fails, others still provide protection, making it harder for attackers to reach valuable assets."],
        ["Digital Forensics", "The process of uncovering and interpreting electronic data to preserve evidence in a way that is suitable for presentation in a court of law. Used to investigate cyber crimes and security incidents."],
        ["Fileless Malware", "A type of malicious software that exists exclusively in a computer's RAM, making it difficult to detect using traditional security tools that scan for files on disk. It often leverages legitimate system tools."],
        ["SIEM", "Security Information and Event Management systems combine security information management and security event management. They provide real-time analysis of security alerts generated by applications and network hardware."]
    ]

    # Create DataFrame and save to CSV
    df = pd.DataFrame(cybersecurity_data, columns=['Concept', 'Description'])
    df.to_csv('cybersecurity_knowledge.csv', index=False)
    print(f"Created CSV with {len(df)} cybersecurity concepts")
    return df