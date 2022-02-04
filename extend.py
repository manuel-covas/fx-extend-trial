from time import time

DATE_INCREMENT = 7 * 24 * 60 * 60 * 1000

shared_preferences_xml = open("nextapp.fx_preferences.xml", "r")

new_file = ""
for line in shared_preferences_xml:
    try:
        line.index("\"trialPlusExpiration\"")
        
        new_date = int(time() * 1000 + DATE_INCREMENT)
        new_file += "    <long name=\"trialPlusExpiration\" value=\"" + str(new_date) + "\" />\n"
    except:
        new_file += line

shared_preferences_xml.close()
shared_preferences_xml = open("nextapp.fx_preferences.xml", "w")

shared_preferences_xml.write(new_file)