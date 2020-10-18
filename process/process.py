def strQ2B(usstring):
  #全角转半角
  rstring = ''
  for unchar in usstring:
    inside_code = ord(unchar)
    if inside_code == 12288:
      inside_code = 32
    elif inside_code >= 65281 and inside_code <= 65374:
      inside_code -= 65248
      
    rstring += chr(inside_code)
  return rstring
      
