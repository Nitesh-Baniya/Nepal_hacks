import re
from textwrap import dedent

def parse_report(text):
    """
    Parse a text report of the form:
    
    *Requirement*:
    ...
    *Status*: ...
    *Reason*:
    ...
    *Target Policy*: ...
    
    into a list of dicts:
    [
      {
        "Requirement": "...",
        "Status": "...",
        "Reason": "...",
        "Target Policy": "..."
      },
      ...
    ]
    """
    entries = []
    
    # Split on each "*Requirement*:" (skip any leading text)
    blocks = re.split(r'\**Requirement\**:', text)[1:]
    
    for blk in blocks:
        # Requirement: up to *Status*:
        req, rest = re.split(r'\**Status\**:', blk, maxsplit=1)
        
        # Status: up to *Reason*:
        status, rest = re.split(r'\**Reason\**:', rest, maxsplit=1)
        
        # # Reason: up to *Target Policy*:
        # reason, rest = re.split(r'\*Target Policy\*[:]? ', rest, maxsplit=1)
        if '*Target Policy*' in rest:
            reason_text, target_text = re.split(r'\**Target Policy\**[:]? ?', rest, maxsplit=1)
        else:
            reason_text, target_text = rest, '' 
        # Target Policy: up to end of block (or next *Requirement*, but split took care)
        # target = rest
        
        # Clean up whitespace and newlines
        clean = lambda s: dedent(s).strip().replace('\n', ' ').replace('  ', ' ')
        
        entries.append({
            "Requirement": clean(req),
            "Status": clean(status),
            "Reason": clean(reason_text),
            "Target Policy": clean(target_text)
        })
    
    return entries