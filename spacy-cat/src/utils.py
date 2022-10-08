# parts of a description that shouldn't factor into the model
countryCodes = ["aus", "nsw", "usa", "act", "ca"]
locations = ["braddon", "kingston"]
verbs = ["purchase", "transfer", "withdraw", "deposit", "direct",
  "credit", "debit", "withdrawal", "payment", "refund", "cross border fee", 
  "paypal"]

def replaceEnding(description, target, replacement):
  if description.endswith(target):
    return description[:-len(target)] + replacement
  return description

# format the description for training
def prepareDescription(description):
  # lowercase
  description = description.lower()

  # remove country codes from the end
  for countryCode in countryCodes:
    description = replaceEnding(description, countryCode, "")
  # remove verbs
  for verb in verbs:
    description = description.replace(verb, "")
  # remove location
  for location in locations:
    description = description.replace(location, "")
  
  return description
