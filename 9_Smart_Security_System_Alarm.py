motion_detected = True       # Sensor ne harkat detect ki hai
door_open = False            # Darwaza khula hai ya band
is_night_time = True         # Raat ka waqt hai
owner_home = False           # Ghar ka malik ghar par hai ya nahi

# Rules
is_unauthorized_entry = (motion_detected == True) or (door_open == True)
is_security_risk = (is_unauthorized_entry == True) and (is_night_time == True)
trigger_alarm = (is_security_risk == True) and (owner_home == False)

#Output
print(f"is_unauthorized_entry? \n {is_unauthorized_entry}.")
print(f"is_security_risk? \n {is_security_risk}.")
print(f"trigger_alarm \n {trigger_alarm}")