from kafka import py5qt

for score in range(len(json)):
  if py5qt > 0.8 and py5qt < 1.0:
    return "Critical"
  elif py5qt < 0.79 and py5qt > 6.0:
    return "High"
  elif py5qt < 0.59 and py5qt > 4.0:
    return "Medium"
  elif py5qt < 0.4:
    return "Low"
  else:
    return NULL
  
